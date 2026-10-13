#!/usr/bin/env python3
"""Download the curated ontology/standards catalog. Python 3.9+, standard library only.

No remote code is executed. Manual/licensed resources are never downloaded by this
program. Success means bytes saved and checked, NOT a complete imports closure or
proof of conformance to a standard. See README.md before redistributing content.
"""
from __future__ import annotations
import argparse, concurrent.futures, contextlib, datetime as dt, hashlib, io, json
import os, re, shutil, socket, stat, sys, threading, time, urllib.error, urllib.parse
import urllib.request, xml.etree.ElementTree as ET, zipfile
from html.parser import HTMLParser
from pathlib import Path, PurePosixPath
from typing import Any

ROOT = Path(__file__).resolve().parent
MIB = 1024 * 1024
UA = 'OntologyResourceCollector/1.0 (personal archival; no recursive crawl)'
ACCEPT = {'rdfxml': 'application/rdf+xml', 'turtle': 'text/turtle, application/x-turtle;q=0.9',
          'json': 'application/ld+json, application/json', 'pdf': 'application/pdf',
          'document': 'text/html, application/pdf;q=0.8'}
EXT = {'.ttl':'turtle','.n3':'text','.nt':'text','.rdf':'rdfxml','.owl':'rdfxml',
       '.json':'json','.jsonld':'json','.xsd':'xml','.xml':'xml','.ofn':'text',
       '.omn':'text','.obo':'obo','.pdf':'pdf','.zip':'zip'}
class DownloadError(Exception): pass
class BudgetError(DownloadError): pass

def now() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat(timespec='seconds')

def sha256(path: Path) -> str:
    h=hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda:f.read(1024*1024),b''): h.update(chunk)
    return h.hexdigest()

def atomic_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True,exist_ok=True)
    tmp=path.with_name(path.name+'.tmp')
    tmp.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    os.replace(tmp,path)

def safe_name(text: str) -> str:
    return (re.sub(r'[^A-Za-z0-9._-]+','_',text).strip('._') or 'resource')[:160]

def reject_bad_html(data: bytes) -> None:
    text=data[:65536].decode('utf-8','replace')
    m=re.search(r'<title[^>]*>(.*?)</title>',text,re.I|re.S)
    title=m.group(1) if m else ''
    if re.search(r'access denied|just a moment|attention required|page not found|^\s*404\b|403 forbidden|sign in to',title,re.I):
        raise DownloadError('Server returned a login/block/error HTML page: '+title[:100])

def validate_file(path: Path, fmt: str, content_type: str='', rdf_validate: bool=False,
                  max_unpacked: int=4096*MIB) -> dict[str, Any]:
    """Format probes are intentionally not described as OWL semantic validation."""
    size=path.stat().st_size
    if not size: raise DownloadError('Empty response')
    with path.open('rb') as f: head=f.read(65536)
    stripped=head.lstrip(b'\xef\xbb\xbf \r\n\t')
    htmlish=bool(re.match(br'(?is)(<!doctype\s+html|<html\b)',stripped)) or 'text/html' in content_type.lower()
    if fmt != 'document' and htmlish:
        raise DownloadError('HTML was returned instead of '+fmt+'; NOT saved as an ontology')
    result={'validation':'basic_format_probe','bytes':size}
    if fmt=='document':
        if stripped.startswith(b'%PDF-'): result['detected_format']='pdf'
        elif htmlish or b'<html' in head.lower():
            reject_bad_html(head); result['detected_format']='html'
        else: raise DownloadError('Expected an HTML or PDF documentation page')
    elif fmt=='pdf':
        if not stripped.startswith(b'%PDF-'): raise DownloadError('Not a PDF signature')
    elif fmt=='zip':
        if not zipfile.is_zipfile(path): raise DownloadError('Not a ZIP archive')
        with zipfile.ZipFile(path) as z:
            info=z.infolist()
            if len(info)>100000: raise DownloadError('ZIP member count exceeds safety limit')
            unpacked=sum(x.file_size for x in info)
            if unpacked>max_unpacked: raise DownloadError('ZIP expanded size exceeds configured safety limit')
            for x in info: validate_zip_member(x)
        result.update(zip_members=len(info),uncompressed_bytes=unpacked)
    elif fmt in ('xml','rdfxml'):
        try:
            # Reject external/internal entity declarations rather than fetching any resources.
            if b'<!DOCTYPE' in head.upper() or b'<!ENTITY' in head.upper():
                result['validation']='xml_signature_only_doctype_not_expanded'
                if b'RDF' not in head and b'Ontology' not in head and fmt=='rdfxml':
                    raise DownloadError('RDF/XML signature not found')
            else:
                event,element=next(ET.iterparse(str(path),events=('start',)))
                if fmt=='rdfxml' and element.tag not in ('{http://www.w3.org/1999/02/22-rdf-syntax-ns#}RDF','{http://www.w3.org/2002/07/owl#}Ontology'):
                    raise DownloadError('XML is not recognisable RDF/XML or OWL/XML')
                result['root_element']=element.tag
        except (ET.ParseError,StopIteration) as e: raise DownloadError('Invalid XML header: '+str(e)) from e
    elif fmt=='json':
        try: json.loads(path.read_text(encoding='utf-8-sig'))
        except (UnicodeError,ValueError) as e: raise DownloadError('Invalid JSON: '+str(e)) from e
        result['validation']='json_syntax'
    elif fmt=='turtle':
        text=head.decode('utf-8-sig','replace')
        if not re.search(r'@prefix\s|@base\s|\bPREFIX\s|\bBASE\s|<https?://',text,re.I):
            raise DownloadError('Turtle markers not found; content requires manual review')
    elif fmt=='obo':
        if b'format-version:' not in head: raise DownloadError('OBO format-version marker missing')
    elif fmt=='text':
        try: head.decode('utf-8-sig')
        except UnicodeError as e: raise DownloadError('Expected UTF-8 text') from e
    else: raise DownloadError('Unknown format: '+fmt)
    if rdf_validate and fmt in ('rdfxml','turtle'):
        if size>100*MIB: raise DownloadError('RDF syntax validation capped at 100 MiB; use a dedicated local tool for this file')
        try: import rdflib
        except ImportError as e: raise DownloadError('--rdf-validate needs rdflib (install it yourself with pip)') from e
        if b'<!DOCTYPE' in head.upper():
            raise DownloadError('DTD-bearing RDF requires separate offline review; parser expansion is disabled')
        try:
            graph=rdflib.Graph()
            # Parse a file, not a URL; no imports or JSON-LD contexts are fetched.
            graph.parse(str(path),format='xml' if fmt=='rdfxml' else 'turtle')
            result.update(validation='rdf_syntax_only',triples=len(graph))
        except Exception as e: raise DownloadError('RDF parse failed: '+str(e)) from e
    return result

def validate_zip_member(info: zipfile.ZipInfo) -> None:
    name=info.filename
    p=PurePosixPath(name)
    if '\\' in name or p.is_absolute() or '..' in p.parts or (p.parts and ':' in p.parts[0]):
        raise DownloadError('Unsafe ZIP path: '+name[:100])
    mode=info.external_attr >> 16
    if stat.S_ISLNK(mode): raise DownloadError('ZIP symlinks are not extracted: '+name[:100])

def extract_zip(path: Path, target: Path, max_unpacked: int) -> int:
    """Two-pass validation: no traversal/symlink members are ever written."""
    with zipfile.ZipFile(path) as z:
        infos=z.infolist()
        if len(infos)>100000 or sum(i.file_size for i in infos)>max_unpacked:
            raise DownloadError('ZIP extraction exceeds safety limits')
        for i in infos: validate_zip_member(i)
        count=0
        for i in infos:
            dest=target.joinpath(*PurePosixPath(i.filename).parts)
            resolved=dest.resolve()
            if target.resolve() not in resolved.parents and resolved != target.resolve():
                raise DownloadError('Existing path redirects ZIP extraction outside the target')
            if dest.is_symlink():
                raise DownloadError('Refusing to overwrite an existing symbolic link')
            if i.is_dir(): dest.mkdir(parents=True,exist_ok=True);continue
            dest.parent.mkdir(parents=True,exist_ok=True)
            with z.open(i) as src,dest.open('wb') as out: shutil.copyfileobj(src,out,1024*1024)
            count+=1
        return count

class Budget:
    def __init__(self,limit:int): self.limit=limit;self.used=0;self.lock=threading.Lock()
    def consume(self,n:int) -> None:
        with self.lock:
            if self.used+n>self.limit: raise BudgetError('Per-run network transfer budget exceeded')
            self.used+=n

class SafeRedirect(urllib.request.HTTPRedirectHandler):
    def __init__(self,check): super().__init__();self.check=check
    def redirect_request(self,req,fp,code,msg,headers,newurl):
        self.check(newurl)
        result=super().redirect_request(req,fp,code,msg,headers,newurl)
        if result is not None and urllib.parse.urlparse(req.full_url).netloc!=urllib.parse.urlparse(newurl).netloc:
            result.remove_header('Authorization');result.remove_header('authorization')
        return result

class Links(HTMLParser):
    def __init__(self): super().__init__();self.urls=[]
    def handle_starttag(self,tag,attrs):
        if tag.lower() not in ('a','link'): return
        d=dict(attrs)
        if d.get('href'): self.urls.append(d['href'])

class Collector:
    def __init__(self,root:Path,catalog:dict[str,Any],args:argparse.Namespace):
        self.root=root;self.catalog=catalog;self.args=args;self.lock=threading.RLock()
        self.records={r['id']:r for r in catalog['resources']}
        self.state_path=root/'reports/download-state.json'
        self.state=json.loads(self.state_path.read_text(encoding='utf-8')) if self.state_path.exists() else {}
        for k in ('files','task_results','resolved_repositories'): self.state.setdefault(k,{})
        self.state['schema_version']=1
        self.budget=Budget(int(args.total_mb*MIB))
        urls=[x.get('url','') for x in catalog['tasks']]+[r['canonical_url'] for r in catalog['resources']]
        self.hosts={urllib.parse.urlparse(u).hostname for u in urls if u}
        self.hosts.update({'api.github.com','codeload.github.com','github.com','raw.githubusercontent.com',
             'release-assets.githubusercontent.com','objects.githubusercontent.com','www.w3.org','w3.org',
             'www.omg.org','www.etsi.org','saref.etsi.org','forge.etsi.org','ref.gs1.org','www.gs1.org',
             'standards.buildingsmart.org','technical.buildingsmart.org','schemas.opengis.net','www.opengis.net',
             'docs.ogc.org','portal.ogc.org','docs.oasis-open.org','purl.obolibrary.org','ontologydesignpatterns.org',
             'www.ontologydesignpatterns.org','www.loa.istc.cnr.it','loa.istc.cnr.it','ftp.ebi.ac.uk',
             'purl.org','www.heppnetz.de','www.nlm.nih.gov','id.nlm.nih.gov','ftp.ncbi.nlm.nih.gov'})
        self.opener=urllib.request.build_opener(SafeRedirect(self.check_url))
    def check_url(self,url:str) -> None:
        p=urllib.parse.urlparse(url)
        if p.scheme not in ('http','https') or not p.hostname or p.username or p.password:
            raise DownloadError('Non-public HTTP(S) URL rejected')
        if p.hostname not in self.hosts:
            raise DownloadError('Redirect/discovery host not on the curated allow-list: '+p.hostname)
        if p.port not in (None,80,443): raise DownloadError('Nonstandard URL port rejected')
    def save(self) -> None:
        with self.lock:
            self.state['updated_at']=now()
            atomic_json(self.state_path,self.state)
            (self.root/'reports/status.js').write_text('window.DOWNLOAD_STATE='+json.dumps(self.state,ensure_ascii=False)+';\n',encoding='utf-8')
    def say(self,text:str) -> None:
        with self.lock: print(text,flush=True)
    def request(self,url:str,fmt:str='document'):
        self.check_url(url)
        headers={'User-Agent':UA,'Accept':ACCEPT.get(fmt,'*/*')}
        if urllib.parse.urlparse(url).hostname=='api.github.com':
            headers['Accept']='application/vnd.github+json'
            token=os.getenv('GITHUB_TOKEN')
            if token: headers['Authorization']='Bearer '+token
        # Python's standard proxy environment variables are honoured; TLS validation stays enabled.
        return self.opener.open(urllib.request.Request(url,headers=headers),timeout=self.args.timeout)
    def read_small(self,url:str,fmt:str='document') -> tuple[bytes,str,str]:
        last=None
        for attempt in range(self.args.retries+1):
            try:
                with self.request(url,fmt) as r:
                    self.check_url(r.geturl())
                    data=r.read(10*MIB+1);self.budget.consume(len(data))
                    if len(data)>10*MIB: raise DownloadError('Metadata/discovery page exceeds 10 MiB')
                    return data,r.geturl(),r.headers.get('Content-Type','')
            except BudgetError: raise
            except (OSError,urllib.error.URLError,DownloadError) as e:
                last=e
                if isinstance(e,urllib.error.HTTPError) and e.code in (401,403,404,410): break
                if attempt<self.args.retries:time.sleep(min(2**attempt,10))
        raise DownloadError(str(last))
    def file(self,task:dict[str,Any],url:str,name:str,fmt:str,kind:str='asset') -> dict[str,Any]:
        rid=task['resource_id'];key=task['id']+'::'+url
        cat=self.records[rid]['categories'][0]
        dest=self.root/'resources'/cat/rid/safe_name(name)
        with self.lock: old=self.state['files'].get(key)
        if old and not self.args.refresh:
            oldpath=self.root/old['path']
            if oldpath.is_file() and sha256(oldpath)==old['sha256']:
                return dict(old,reused=True)
        dest.parent.mkdir(parents=True,exist_ok=True)
        part=dest.with_name(dest.name+'.part')
        last=None
        for attempt in range(self.args.retries+1):
            try:
                with self.request(url,fmt) as response:
                    final_url=response.geturl();self.check_url(final_url)
                    content_type=response.headers.get('Content-Type','')
                    length=response.headers.get('Content-Length')
                    if length and int(length)>self.args.max_mb*MIB: raise DownloadError('File exceeds --max-mb')
                    total=0
                    with part.open('wb') as f:
                        while True:
                            chunk=response.read(128*1024)
                            if not chunk: break
                            self.budget.consume(len(chunk));total+=len(chunk)
                            if total>self.args.max_mb*MIB: raise DownloadError('File exceeds --max-mb')
                            f.write(chunk)
                    if length and int(length)!=total: raise DownloadError('Incomplete Content-Length transfer')
                    info=validate_file(part,fmt,content_type,self.args.rdf_validate,int(self.args.max_unpacked_mb*MIB))
                    if fmt=='document' and info.get('detected_format')=='pdf': dest=dest.with_suffix('.pdf')
                    os.replace(part,dest)
                    item={'resource_id':rid,'task_id':task['id'],'requested_url':url,'resolved_url':final_url,
                          'path':str(dest.relative_to(self.root)),'kind':kind,'format':fmt,'sha256':sha256(dest),
                          'retrieved_at':now(),'content_type':content_type,'etag':response.headers.get('ETag'),
                          'last_modified':response.headers.get('Last-Modified'),**info}
                if self.args.extract and fmt=='zip':
                    target=dest.with_suffix('')
                    item['extracted_files']=extract_zip(dest,target,int(self.args.max_unpacked_mb*MIB))
                    item['extracted_path']=str(target.relative_to(self.root))
                with self.lock:self.state['files'][key]=item;self.save()
                self.say(f"  SAVED {rid}: {dest.name} ({total/1024:.1f} KiB)")
                return item
            except BudgetError: raise
            except (OSError,ValueError,urllib.error.URLError,DownloadError,zipfile.BadZipFile) as e:
                last=e
                if isinstance(e,urllib.error.HTTPError) and e.code in (401,403,404,410): break
                if isinstance(e,DownloadError) and not isinstance(e,urllib.error.URLError): break
                if attempt<self.args.retries:time.sleep(min(2**attempt,10))
            finally:
                with contextlib.suppress(FileNotFoundError): part.unlink()
        raise DownloadError(str(last))
    def github(self,task:dict[str,Any]) -> list[dict[str,Any]]:
        repo=task['repository'];key=task['id']
        with self.lock: resolved=self.state['resolved_repositories'].get(key)
        if not resolved or self.args.refresh:
            raw,_,_=self.read_small('https://api.github.com/repos/'+repo,'json');meta=json.loads(raw)
            # Respect an upstream rename; don't guess master/main or reuse a made-up commit.
            actual=meta['full_name'];branch=meta['default_branch']
            raw,_,_=self.read_small('https://api.github.com/repos/'+actual+'/commits/'+urllib.parse.quote(branch,safe=''),'json')
            commit=json.loads(raw)['sha']
            if not re.fullmatch(r'[0-9a-f]{40}',commit): raise DownloadError('Invalid GitHub commit SHA')
            resolved={'repository':actual,'default_branch':branch,'commit_sha':commit,'resolved_at':now(),
                      'license':(meta.get('license') or {}).get('spdx_id'),'snapshot_type':'default_branch_commit_not_release'}
            with self.lock:self.state['resolved_repositories'][key]=resolved;self.save()
        commit=resolved['commit_sha'];repo=resolved['repository']
        item=self.file(task,'https://codeload.github.com/'+repo+'/zip/'+commit,
                       repo.replace('/','_')+'-'+commit[:12]+'.zip','zip','repository')
        item.update(repository=repo,commit_sha=commit)
        with self.lock:self.state['files'][task['id']+'::'+item['requested_url']].update(repository=repo,commit_sha=commit);self.save()
        return [item]
    def discover(self,task:dict[str,Any]) -> list[dict[str,Any]]:
        data,final,ctype=self.read_small(task['url'])
        if data.lstrip().startswith(b'%PDF-'):
            return [self.file(task,task['url'],task['id']+'.pdf','pdf','document')]
        reject_bad_html(data)
        parser=Links();parser.feed(data.decode('utf-8','replace'))
        choices=[]
        for href in parser.urls:
            u=urllib.parse.urldefrag(urllib.parse.urljoin(final,href))[0]
            try:self.check_url(u)
            except DownloadError:continue
            suffix=Path(urllib.parse.urlparse(u).path).suffix.lower()
            if suffix not in EXT:continue
            if task.get('pattern') and not re.search(task['pattern'],u,re.I):continue
            if u not in choices:choices.append(u)
        choices.sort(key=lambda u: (Path(urllib.parse.urlparse(u).path).suffix.lower()=='.pdf',u))
        selected=choices[:self.args.discover_limit]
        cat=self.records[task['resource_id']]['categories'][0]
        evidence=self.root/'resources'/cat/task['resource_id']/(task['id']+'-discovery.json')
        atomic_json(evidence,{'source_url':task['url'],'resolved_url':final,'discovered_at':now(),
                             'matching_links':choices,'selected_links':selected,'omitted_due_to_limit':len(choices)-len(selected)})
        if not selected:raise DownloadError('No matching direct files found; portal retained for manual selection')
        successes=[];errors=[]
        for i,u in enumerate(selected,1):
            name=urllib.parse.unquote(Path(urllib.parse.urlparse(u).path).name)
            fmt=EXT[Path(urllib.parse.urlparse(u).path).suffix.lower()]
            try:successes.append(self.file(task,u,task['id']+'-'+str(i)+'-'+name,fmt,'document' if fmt=='pdf' else 'discovered_asset'))
            except (DownloadError,OSError) as e:errors.append({'url':u,'error':str(e)})
        if errors or len(choices)>len(selected):
            with self.lock:
                self.state['task_results'][task['id']]={'status':'partial','at':now(),'resource_id':task['resource_id'],
                     'saved_files':len(successes),'errors':errors,'omitted_due_to_limit':len(choices)-len(selected)}
                self.save()
        if not successes:raise DownloadError('All discovered files failed: '+json.dumps(errors,ensure_ascii=False)[:1500])
        return successes
    def run_task(self,task:dict[str,Any]) -> dict[str,Any]:
        result={'resource_id':task['resource_id'],'at':now()}
        # A successful retry must not inherit a previous discovery's partial status.
        with self.lock:
            self.state['task_results'].pop(task['id'],None)
        try:
            if task['kind']=='github':items=self.github(task)
            elif task['kind']=='discover':items=self.discover(task)
            else:items=[self.file(task,task['url'],task['filename'],task['format'],
                                 'document' if task['kind']=='document' else 'asset')]
            with self.lock: partial=self.state['task_results'].get(task['id'],{})
            if partial.get('status')=='partial' and task['kind']=='discover':result=partial
            else:result.update(status='saved',saved_files=len(items))
        except Exception as e:
            result.update(status='failed',error=f'{type(e).__name__}: {e}')
            self.say(f"  FAILED {task['id']}: {result['error'][:300]}")
        with self.lock:self.state['task_results'][task['id']]=result;self.save()
        return result

def eligibility(task:dict[str,Any],args:argparse.Namespace) -> str|None:
    if task['policy']=='manual':return 'manual_authorisation_or_selection'
    if task['policy']=='review' and not args.include_unverified:return 'unverified_source'
    if task.get('large') and not args.include_large:return 'large_resource_not_enabled'
    if task['kind']=='document' and not args.docs:return 'single_page_snapshot_not_enabled'
    if args.only=='assets' and task['kind'] in ('github','document'):return 'mode_filter'
    if args.only=='repositories' and task['kind']!='github':return 'mode_filter'
    if args.only=='documents' and task['kind']!='document':return 'mode_filter'
    return None

def select_resources(catalog:dict[str,Any],args:argparse.Namespace) -> set[str]:
    ids={r['id'] for r in catalog['resources']}
    if args.ids:
        requested={s.strip() for s in args.ids.split(',') if s.strip()}
        bad=requested-ids
        if bad:raise DownloadError('Unknown resource ids: '+','.join(sorted(bad)))
        ids&=requested
    if args.category:
        cats={c['id'] for c in catalog['categories'] if args.category==c['id'] or args.category==c['name']}
        if not cats:raise DownloadError('Unknown category; use --list for IDs 01–14')
        ids&={r['id'] for r in catalog['resources'] if cats.intersection(r['categories'])}
    return ids

def verify_state(root:Path,state:dict[str,Any]) -> list[dict[str,Any]]:
    result=[]
    for item in state.get('files',{}).values():
        p=root/item['path']
        status='missing' if not p.is_file() else ('ok' if sha256(p)==item['sha256'] else 'hash_mismatch')
        result.append({'path':item['path'],'status':status})
    return result

def write_report(root:Path,catalog:dict[str,Any],state:dict[str,Any]) -> None:
    files=list(state.get('files',{}).values())
    # Paths may be reused by two discovery tasks: count physical artifacts once.
    unique={f['path']:f for f in files}
    assets=[f for f in unique.values() if f['kind']!='document']
    docs=[f for f in unique.values() if f['kind']=='document']
    taskcounts={}
    for v in state.get('task_results',{}).values():taskcounts[v['status']]=taskcounts.get(v['status'],0)+1
    lines=['# 下载执行报告','',f'生成时间：{now()}','',
           f'已登记本地原文件：{len(unique)}；其中资料/仓库文件：{len(assets)}；文档快照：{len(docs)}。',
           '','这里只统计真正写入磁盘并记录校验值的文件。下载成功不代表标准符合性、imports 闭包或正式发行版。',
           '',f'任务状态：`{json.dumps(taskcounts,ensure_ascii=False)}`','',
           '| 资源 | 本地文件数 | 资料性质 / 后续要求 |','|---|---:|---|']
    for r in catalog['resources']:
        n=sum(f['resource_id']==r['id'] for f in unique.values())
        lines.append(f"| {r['title']} | {n} | {r['scope_note'].replace('|','/')} |")
    lines+=['','## 失败、部分完成及跳过的任务','']
    for key,r in state.get('task_results',{}).items():
        if r['status']!='saved':lines.append(f"- `{key}` — {r['status']}：{r.get('error',r.get('reason',json.dumps(r,ensure_ascii=False)))}")
    if not state.get('task_results'):lines+=['尚未执行下载。']
    (root/'reports/download-report.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    (root/'reports/SHA256SUMS.downloads.txt').write_text(''.join(f"{v['sha256']}  {p}\n" for p,v in sorted(unique.items())),encoding='utf-8')

def make_pack(root:Path,destination:Path) -> int:
    destination=destination.resolve()
    if root.resolve() in destination.parents:raise DownloadError('Place the ZIP outside the kit folder to avoid packaging itself')
    destination.parent.mkdir(parents=True,exist_ok=True)
    count=0
    with zipfile.ZipFile(destination,'w',zipfile.ZIP_DEFLATED,compresslevel=6,allowZip64=True) as z:
        for p in sorted(root.rglob('*')):
            if not p.is_file() or p.is_symlink():continue
            if any(x in p.parts for x in ('__pycache__','.git','.venv')):continue
            if p.suffix in ('.part','.tmp','.pyc') or p.name in ('.download.lock','.DS_Store'):continue
            z.write(p,Path(root.name)/p.relative_to(root));count+=1
    digest=sha256(destination)
    destination.with_name(destination.name+'.sha256').write_text(digest+'  '+destination.name+'\n',encoding='utf-8')
    return count

def build_parser() -> argparse.ArgumentParser:
    p=argparse.ArgumentParser(description=__doc__,formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument('--all',action='store_true',help='select all 75 resources (manual/review/large gates still apply)')
    p.add_argument('--ids',help='comma-separated resource IDs, e.g. bfo,iof,skos')
    p.add_argument('--category',help='category ID 01–14 or exact Chinese category name')
    p.add_argument('--list',action='store_true',help='list all categories and resource IDs without network access')
    p.add_argument('--dry-run',action='store_true',help='show planned/skipped tasks; no network access')
    p.add_argument('--docs',action='store_true',help='also save optional single-page documentation snapshots')
    p.add_argument('--include-large',action='store_true',help='include large candidate repositories/datasets')
    p.add_argument('--include-unverified',action='store_true',help='attempt the three explicitly unverified original repository URLs')
    p.add_argument('--only',choices=['all','assets','repositories','documents'],default='all')
    p.add_argument('--workers',type=int,default=3)
    p.add_argument('--timeout',type=float,default=35)
    p.add_argument('--retries',type=int,default=2)
    p.add_argument('--max-mb',type=float,default=512,help='max compressed/downloaded size per file')
    p.add_argument('--total-mb',type=float,default=2048,help='max network bytes per run, including retries')
    p.add_argument('--max-unpacked-mb',type=float,default=4096,help='maximum expanded size of a ZIP')
    p.add_argument('--discover-limit',type=int,default=40,help='max direct files per discovery page; omissions reported')
    p.add_argument('--refresh',action='store_true',help='resolve new GitHub commits and re-fetch direct URLs')
    p.add_argument('--extract',action='store_true',help='safely extract ZIPs; never execute their content')
    p.add_argument('--rdf-validate',action='store_true',help='optionally parse RDF syntax using preinstalled rdflib')
    p.add_argument('--verify',action='store_true',help='check hashes of downloaded artifacts, without network access')
    p.add_argument('--pack',nargs='?',const='AUTO',help='ZIP the kit and downloaded files; optional output path outside this folder')
    return p

def main(argv=None) -> int:
    args=build_parser().parse_args(argv)
    if min(args.workers,args.timeout,args.max_mb,args.total_mb,args.max_unpacked_mb,args.discover_limit)<=0 or args.retries<0:
        print('Invalid non-positive limit or retry count',file=sys.stderr);return 2
    catalog=json.loads((ROOT/'catalog/catalog.json').read_text(encoding='utf-8'))
    if args.list:
        for c in catalog['categories']:
            print(c['id'],c['name'])
            for r in catalog['resources']:
                if c['id'] in r['categories']:print('  ',r['id'].ljust(20),r['title'],'['+r['policy']+']')
        return 0
    try:selected=select_resources(catalog,args)
    except DownloadError as e: print(e,file=sys.stderr);return 2
    collector=Collector(ROOT,catalog,args)
    if args.verify:
        results=verify_state(ROOT,collector.state)
        atomic_json(ROOT/'reports/verification.json',{'at':now(),'files':results})
        for r in results:print(r['status'],r['path'])
        print('Verified',len(results),'files; no network access.')
        return int(any(r['status']!='ok' for r in results))
    tasks=[t for t in catalog['tasks'] if t['resource_id'] in selected]
    runnable=[];skipped=[]
    for task in tasks:
        reason=eligibility(task,args)
        if reason:skipped.append((task,reason))
        else:runnable.append(task)
    print(f'Selected resources: {len(selected)} | Runnable tasks: {len(runnable)} | Skipped tasks: {len(skipped)}')
    print('Sources marked manual are never auto-downloaded. A saved page is not an ontology.')
    dry=args.dry_run or not(args.all or args.ids or args.category)
    if dry:
        for t in runnable:print('PLAN',t['id'],t.get('url',t.get('repository','')))
        for t,reason in skipped:print('SKIP',t['id'],reason)
        print('Dry run only. Use --all or --ids or --category to execute.')
        return 0
    lockfile=ROOT/'.download.lock'
    try:
        fd=os.open(lockfile,os.O_CREAT|os.O_EXCL|os.O_WRONLY)
        with os.fdopen(fd,'w') as f:f.write(f'PID={os.getpid()} UTC={now()}\n')
    except FileExistsError:
        print('Another run may be active. If it crashed, inspect and remove .download.lock, then retry.',file=sys.stderr);return 2
    results=[]
    try:
        with collector.lock:
            for t,reason in skipped:
                # Keep previous successful downloads when a later run uses narrower options.
                if collector.state['task_results'].get(t['id'],{}).get('status')=='saved':continue
                collector.state['task_results'][t['id']]={'resource_id':t['resource_id'],'status':'skipped','reason':reason,'at':now()}
            collector.save()
        with concurrent.futures.ThreadPoolExecutor(max_workers=min(args.workers,8)) as pool:
            futures={pool.submit(collector.run_task,t):t for t in runnable}
            for future in concurrent.futures.as_completed(futures): results.append(future.result())
    except KeyboardInterrupt:
        print('\nInterrupted. Completed files are preserved; partial files will be fetched again.',file=sys.stderr)
        return 130
    finally:
        collector.save();write_report(ROOT,catalog,collector.state)
        with contextlib.suppress(FileNotFoundError):lockfile.unlink()
    failed=sum(r['status'] in ('failed','partial') for r in results)
    print(f'Finished: {len(results)-failed} saved tasks, {failed} failed/partial tasks. See reports/download-report.md')
    if args.pack:
        dest=(ROOT.parent/('ontology-resources-'+dt.datetime.now().strftime('%Y%m%d')+'-with-downloads.zip')) if args.pack=='AUTO' else Path(args.pack).expanduser()
        try:n=make_pack(ROOT,dest);print(f'ZIP: {dest.resolve()} ({n} files)')
        except (OSError,DownloadError) as e:print('Packaging failed: '+str(e),file=sys.stderr);return 2
    return 1 if failed else 0

if __name__=='__main__':
    try:sys.exit(main())
    except (OSError,ValueError,KeyError,DownloadError) as e:
        print(f'ERROR: {type(e).__name__}: {e}',file=sys.stderr);sys.exit(2)
