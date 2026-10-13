#!/usr/bin/env python3
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
c=json.loads((ROOT/'catalog/catalog.json').read_text(encoding='utf-8'))
t=(ROOT/'tools/site-template.html').read_text(encoding='utf-8')
t=t.replace('__CATALOG__',json.dumps(c,ensure_ascii=False,separators=(',',':')).replace('</','<\\/'))
(ROOT/'index.html').write_text(t,encoding='utf-8')
print('index.html',len(t.encode('utf-8')),'bytes')
