#!/usr/bin/env python3
import json,html,collections
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
c=json.loads((ROOT/'catalog/catalog.json').read_text(encoding='utf-8'))
policy={'open':'公开下载候选','manual':'需人工选择/确认授权','review':'来源待核验','portal':'入口/生态，非单一资料包'}
summary=['# 本体与标准资源目录','',f'整理日期：{c["created_on"]}。原清单 {c["original_entry_count"]} 条，按资源归并为 {c["original_resource_count"]} 项，另补充 {c["supplement_count"]} 项（共 {c["resource_count"]} 项），保留 {c["category_count"]} 个领域。',
'','**本交付是整理目录与下载工具包，不是已下载齐全的本体资料库。当前包含上游原文件 0 份。**',
'','归并只整理入口，不合并本体语义；不同版本和原始链接均保留。',
'','## 目录','']
for cat in c['categories']:
 summary.append(f'- [{cat["id"]} · {cat["name"]}](#{cat["id"]})')
for cat in c['categories']:
 lines=[f'<a id="{cat["id"]}"></a>',f'## {cat["id"]} · {cat["name"]}','',
 '| ID | 资源 | 类型 | 获取方式 |','|---|---|---|---|']
 relevant=[r for r in c['resources'] if cat['id'] in r['categories']]
 for r in relevant:
  lines.append(f'| `{r["id"]}` | [{r["title"]}]({r["canonical_url"]}) | {r["kind"]} | {policy[r["policy"]]} |')
 for r in relevant:
  lines+=['',f'### {r["title"]}', '',r['summary'],'',f'**典型用途：**{r["use_for"]}','',f'**获取与范围说明：**{r["scope_note"]}','',f'核验范围：{"已访问相关页面/目录，但未取得原始文件" if r["verification"]=="page_checked" else "未逐项确认页面及发行文件，仅保留原始入口和下载计划"}。',
         f'归档标识：`{r["id"]}`；原文件状态：**未下载**。','']
  for e in r['original_entries']:
   lines.append(f'- 原清单第 {e["original_row"]} 条：[{e["name"]}]({e["url"]})（{e["category"]}）')
  if r['issue']:lines+=['',f'**{r["issue"]["type"]}：** {r["issue"]["note"]}',f'来源：{r["issue"]["source_url"]}']
  tasks=[t for t in c['tasks'] if t['resource_id']==r['id'] and t['kind']!='document']
  if tasks:
   lines+=['','下载计划（未执行/未落盘，不等于已验证的发行包）：']
   for t in tasks:
    url=t.get('url','https://github.com/'+t.get('repository',''))
    lines.append(f'- `{t["kind"]}`：{url}'+('（大型，需 --include-large）' if t.get('large') else ''))
  else:lines+=['','本项保留人工入口；不自动抓取付费、登录后内容或整个标准生态。']
 summary+=['']+lines
 (ROOT/'docs'/f'category-{cat["id"]}.md').write_text('\n'.join(['# 分领域目录','']+lines)+'\n',encoding='utf-8')
(ROOT/'docs/01-resource-catalog.md').write_text('\n'.join(summary)+'\n',encoding='utf-8')
issues=[r for r in c['resources'] if r['issue']]
lines=['# 链接、版本与类型检查','',f'检查日期：{c["created_on"]}。记录 {len(issues)} 项问题或澄清，不表示其余全部完成逐项验证。',
'','“本次访问失败”不等于“仓库不存在”；不把无法核实的来源静默替换为名称相近的项目。','']
for r in issues:
 i=r['issue'];lines += [f'## {r["title"]} · {i["type"]}','',i['note'],'',f'核验来源：{i["source_url"]}','', '原始入口：']
 for e in r['original_entries']:lines.append(f'- {e["url"]}')
 lines+=['']
(ROOT/'docs/02-link-and-version-audit.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
manual=['# 人工获取、授权及待核验项','',
'该清单用于安排后续获取，不是法律意见。标准、软件代码、本体文件和实例数据的许可可能各不相同；公开浏览不自动等于可以打包公开分发。',
'','工具不会购买标准、使用你的浏览器登录态、登录网站、同意点击式协议或下载受控账户内容。','']
for r in c['resources']:
 if r['policy'] in ['manual','review','portal']:
  manual += [f'## {r["title"]}','',f'状态：{policy[r["policy"]]}。',r['scope_note'],f'官方/原始入口：{r["canonical_url"]}','']
(ROOT/'docs/03-manual-and-licensing.md').write_text('\n'.join(manual)+'\n',encoding='utf-8')
src=['# 官方获取来源','','每项资源的发布/维护方、权威类型、获取权限和官方入口。优先使用标准组织、发布方官网和官方仓库。','','**来源由整理者依据公开信息选定，未在制作环境逐项访问核验；以发布方页面为准。** 标注付费或需许可的项目不会被工具自动下载。','']
for cat in c['categories']:
 src+=[f'## {cat["id"]} · {cat["name"]}','','| 资源 | 发布/维护方 | 权威类型 | 获取权限 | 官方入口 | 如何取得 |','|---|---|---|---|---|---|']
 for r in c['resources']:
  if cat['id'] not in r['categories']:continue
  s=r['official_sources']
  links='<br>'.join(f'[{l["label"]}]({l["url"]})' for l in s['links'])
  mark=' *(补充)*' if r['origin']=='supplement' else ''
  src.append(f'| {r["title"]}{mark} | {s["publisher"]} | {s["authority"]} | {s["access"]} | {links} | {s["how"]} |')
 src.append('')
(ROOT/'docs/05-official-sources.md').write_text('\n'.join(src)+'\n',encoding='utf-8')
print('Built catalog and',len(issues),'audit entries')
