"""Offline tests with synthetic fixtures. No connection to any upstream publisher."""
from __future__ import annotations
import contextlib, hashlib, importlib.util, io, json, os, stat, tempfile, unittest, zipfile
from pathlib import Path
from unittest.mock import patch, Mock
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('download',ROOT/'download.py')
d=importlib.util.module_from_spec(spec);spec.loader.exec_module(d)

class Response(io.BytesIO):
    def __init__(self,data,url='https://www.w3.org/test.ttl',ctype='text/turtle'):
        super().__init__(data);self.url=url
        self.headers={'Content-Type':ctype,'Content-Length':str(len(data))}
    def geturl(self):return self.url

class Tests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.root=Path(self.tmp.name)/'kit';self.root.mkdir()
        self.args=d.build_parser().parse_args(['--all','--retries','0'])
        self.task={'id':'fixture','resource_id':'test','kind':'asset','policy':'open','url':'https://www.w3.org/test.ttl','filename':'test.ttl','format':'turtle'}
        self.cat={'resources':[{'id':'test','title':'Test','categories':['01'],'canonical_url':'https://www.w3.org/','scope_note':'Synthetic fixture only.'}],
                  'categories':[{'id':'01','name':'Tests'}], 'tasks':[self.task]}
        self.c=d.Collector(self.root,self.cat,self.args)
        self.ttl=b'@prefix ex: <https://example.org/> . ex:a ex:b ex:c .\n'
    def tearDown(self):self.tmp.cleanup()
    def write(self,data,name='fixture'):
        p=self.root/name;p.write_bytes(data);return p
    def test_catalog_integrity(self):
        c=json.loads((ROOT/'catalog/catalog.json').read_text())
        self.assertEqual(len(c['resources']),108);self.assertEqual(len(c['categories']),14)
        self.assertEqual(c['supplement_count'],33);self.assertEqual(c['original_resource_count'],75)
        self.assertTrue(all(r['official_sources']['links'] and r['summary'] for r in c['resources']))
        self.assertEqual(len(c['tasks']),107)
        self.assertEqual(sum(len(r['original_entries']) for r in c['resources']),84)
        self.assertEqual(len({r['id'] for r in c['resources']}),108)
        self.assertEqual(len({t['id'] for t in c['tasks']}),107)
        ids={r['id'] for r in c['resources']}
        self.assertTrue(all(t['resource_id'] in ids for t in c['tasks']))
    def test_turtle_signature(self):self.assertEqual(d.validate_file(self.write(self.ttl),'turtle')['bytes'],len(self.ttl))
    def test_empty_rejected(self):
        with self.assertRaises(d.DownloadError):d.validate_file(self.write(b''),'turtle')
    def test_html_not_ontology(self):
        with self.assertRaises(d.DownloadError):d.validate_file(self.write(b'<html><title>OK</title></html>'),'rdfxml','text/html')
    def test_block_page_not_document(self):
        with self.assertRaises(d.DownloadError):d.validate_file(self.write(b'<html><title>Access denied</title></html>'),'document','text/html')
    def test_json_syntax(self):
        d.validate_file(self.write(b'{"value":1}'),'json')
        with self.assertRaises(d.DownloadError):d.validate_file(self.write(b'{bad}'),'json')
    def test_xml_root(self):
        body=b'<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"></rdf:RDF>'
        self.assertIn('root_element',d.validate_file(self.write(body),'rdfxml'))
        with self.assertRaises(d.DownloadError):d.validate_file(self.write(b'<error/>'),'rdfxml')
    def test_obo_signature(self):
        d.validate_file(self.write(b'format-version: 1.2\n'),'obo')
        with self.assertRaises(d.DownloadError):d.validate_file(self.write(b'not obo'),'obo')
    def test_budget(self):
        b=d.Budget(10);b.consume(7)
        with self.assertRaises(d.BudgetError):b.consume(4)
        self.assertEqual(b.used,7)
    def test_filename(self):
        name=d.safe_name('../../file with spaces.ttl');self.assertNotIn('/',name);self.assertFalse(name.startswith('.'))
    def test_url_security(self):
        self.c.check_url('https://www.w3.org/a')
        for url in ('file:///etc/passwd','https://other.invalid/a','https://user:pass@www.w3.org/a','https://www.w3.org:8080/a'):
            with self.subTest(url=url),self.assertRaises(d.DownloadError):self.c.check_url(url)
    def test_auth_stripped_on_cross_host_redirect(self):
        req=d.urllib.request.Request('https://api.github.com/a',headers={'Authorization':'Bearer test-value'})
        out=d.SafeRedirect(self.c.check_url).redirect_request(req,None,302,'Found',{},'https://codeload.github.com/a')
        self.assertIsNone(out.get_header('Authorization'))
    def test_manual_gate(self):
        self.assertEqual(d.eligibility(dict(self.task,policy='manual'),self.args),'manual_authorisation_or_selection')
        self.args.include_unverified=True;self.args.include_large=True
        self.assertEqual(d.eligibility(dict(self.task,policy='manual'),self.args),'manual_authorisation_or_selection')
    def test_optional_gates(self):
        self.assertIsNotNone(d.eligibility(dict(self.task,policy='review'),self.args))
        self.assertIsNotNone(d.eligibility(dict(self.task,large=True),self.args))
        self.assertIsNotNone(d.eligibility(dict(self.task,kind='document'),self.args))
    def test_selection_validation(self):
        self.assertEqual(d.select_resources(self.cat,self.args),{'test'})
        self.args.ids='missing'
        with self.assertRaises(d.DownloadError):d.select_resources(self.cat,self.args)
    def test_mock_download_and_reuse(self):
        with patch.object(self.c,'request',return_value=Response(self.ttl)) as request,contextlib.redirect_stdout(io.StringIO()):
            saved=self.c.file(self.task,self.task['url'],'test.ttl','turtle')
            reused=self.c.file(self.task,self.task['url'],'test.ttl','turtle')
        self.assertEqual(request.call_count,1);self.assertTrue(reused['reused'])
        self.assertEqual(saved['sha256'],hashlib.sha256(self.ttl).hexdigest())
        self.assertEqual((self.root/saved['path']).read_bytes(),self.ttl)
    def test_corrupt_cached_file_is_retrieved(self):
        with patch.object(self.c,'request',side_effect=lambda *a:Response(self.ttl)) as request,contextlib.redirect_stdout(io.StringIO()):
            saved=self.c.file(self.task,self.task['url'],'test.ttl','turtle')
            (self.root/saved['path']).write_bytes(b'corrupted')
            self.c.file(self.task,self.task['url'],'test.ttl','turtle')
        self.assertEqual(request.call_count,2)
    def test_invalid_download_not_registered(self):
        with patch.object(self.c,'request',return_value=Response(b'<html>error</html>',ctype='text/html')):
            with self.assertRaises(d.DownloadError):self.c.file(self.task,self.task['url'],'test.ttl','turtle')
        self.assertFalse(self.c.state['files']);self.assertFalse(list(self.root.rglob('*.part')))
    def test_content_length_mismatch(self):
        response=Response(self.ttl);response.headers['Content-Length']=str(len(self.ttl)+1)
        with patch.object(self.c,'request',return_value=response),self.assertRaises(d.DownloadError):
            self.c.file(self.task,self.task['url'],'test.ttl','turtle')
        self.assertFalse(self.c.state['files'])
    def test_max_size(self):
        self.args.max_mb=0.000001
        with patch.object(self.c,'request',return_value=Response(self.ttl)),self.assertRaises(d.DownloadError):
            self.c.file(self.task,self.task['url'],'test.ttl','turtle')
    def test_zip_path_safety(self):
        for name in ('../escape','/absolute','C:/windows','folder\\backslash'):
            with self.subTest(name=name),self.assertRaises(d.DownloadError):d.validate_zip_member(zipfile.ZipInfo(name))
        info=zipfile.ZipInfo('link');info.external_attr=(stat.S_IFLNK|0o777)<<16
        with self.assertRaises(d.DownloadError):d.validate_zip_member(info)
    def test_zip_extract(self):
        p=self.root/'normal.zip'
        with zipfile.ZipFile(p,'w') as z:z.writestr('dir/test.txt','test')
        self.assertEqual(d.extract_zip(p,self.root/'out',1000),1)
        self.assertEqual((self.root/'out/dir/test.txt').read_text(),'test')
    def test_zip_existing_symlink_escape(self):
        if not hasattr(os,'symlink'):self.skipTest('platform has no symlinks')
        p=self.root/'normal.zip';target=self.root/'out';target.mkdir();outside=self.root/'elsewhere';outside.mkdir()
        try:(target/'dir').symlink_to(outside,target_is_directory=True)
        except OSError:self.skipTest('symlink permission unavailable')
        with zipfile.ZipFile(p,'w') as z:z.writestr('dir/escaped.txt','bad')
        with self.assertRaises(d.DownloadError):d.extract_zip(p,target,1000)
        self.assertFalse((outside/'escaped.txt').exists())
    def test_discovery_retry_clears_stale_partial(self):
        task=dict(self.task,kind='discover');self.c.state['task_results'][task['id']]={'status':'partial'}
        with patch.object(self.c,'discover',return_value=[{'fixture':True}]):result=self.c.run_task(task)
        self.assertEqual(result['status'],'saved')
    def test_discovery_limit_reports_partial(self):
        self.args.discover_limit=1
        html=b'<a href="a.ttl">A</a><a href="b.ttl">B</a><a href="https://unknown.invalid/c.ttl">C</a>'
        task=dict(self.task,kind='discover')
        with patch.object(self.c,'read_small',return_value=(html,'https://www.w3.org/page','text/html')), \
             patch.object(self.c,'file',return_value={'fixture':True}):
            result=self.c.run_task(task)
        self.assertEqual(result['status'],'partial');self.assertEqual(result['omitted_due_to_limit'],1)
    def test_github_pin_resolution(self):
        task=dict(self.task,kind='github',repository='test/repo');commit='a'*40
        meta=json.dumps({'full_name':'test/renamed','default_branch':'release/stable','license':{'spdx_id':'MIT'}}).encode()
        commitbody=json.dumps({'sha':commit}).encode();calls=[]
        def fakefile(t,u,n,f,k):
            item={'requested_url':u,'path':'fixture.zip'};calls.append((u,n,f,k))
            self.c.state['files'][t['id']+'::'+u]=dict(item);return item
        with patch.object(self.c,'read_small',side_effect=[(meta,'',''),(commitbody,'','')]) as read, \
             patch.object(self.c,'file',side_effect=fakefile):
            self.c.github(task)
        self.assertEqual(calls[0][0],'https://codeload.github.com/test/renamed/zip/'+commit)
        self.assertIn('release%2Fstable',read.call_args_list[1].args[0])
    def test_verify_hash_mismatch(self):
        p=self.write(b'test');state={'files':{'x':{'path':p.name,'sha256':'bad'}}}
        self.assertEqual(d.verify_state(self.root,state)[0]['status'],'hash_mismatch')
    def test_pack_checksums_and_exclusions(self):
        self.write(b'a','file.txt');self.write(b'partial','file.part')
        dest=Path(self.tmp.name)/'bundle.zip';self.assertEqual(d.make_pack(self.root,dest),1)
        with zipfile.ZipFile(dest) as z:self.assertEqual(z.namelist(),['kit/file.txt']);self.assertIsNone(z.testzip())
        self.assertTrue(dest.with_name('bundle.zip.sha256').read_text().startswith(d.sha256(dest)))
        with self.assertRaises(d.DownloadError):d.make_pack(self.root,self.root/'recursive.zip')

if __name__=='__main__':unittest.main(verbosity=2)
