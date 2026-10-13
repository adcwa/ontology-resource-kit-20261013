"""Optional browser smoke test. Requires preinstalled Playwright + Chromium.
This renders the generated HTML in memory; it does not test publisher downloads.
Run: CHROMIUM_PATH=/usr/bin/chromium python tests/ui_smoke.py
"""
from pathlib import Path
import json, os, tempfile
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parents[1]
checks=[]
def check(name,condition):
    if not condition:raise AssertionError(name)
    checks.append(name)
with sync_playwright() as p:
    options={'headless':True}
    if os.environ.get('CHROMIUM_PATH'):options['executable_path']=os.environ['CHROMIUM_PATH']
    browser=p.chromium.launch(**options)
    page=browser.new_page(viewport={'width':1440,'height':1100},device_scale_factor=1)
    errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
    html=(ROOT/'index.html').read_text(encoding='utf-8').replace('<script src="reports/status.js"></script>','<script>'+(ROOT/'reports/status.js').read_text(encoding='utf-8')+'</script>')
    page.set_content(html)
    check('all 108 cards rendered',page.locator('.card').count()==108)
    check('delivery notice explicitly states no originals', '尚未收录上游原文件' in page.locator('#delivery-notice').inner_text())
    check('zero downloaded count',page.locator('#saved-count').inner_text()=='0')
    page.locator('#search').fill('15926')
    check('search matches 2 ISO15926 resources',page.locator('.card').count()==2)
    page.locator('#reset').click();page.locator('[data-category="03"]').click()
    check('manufacturing category has 6 resources',page.locator('.card').count()==6)
    page.locator('#select-filtered').check()
    check('all 6 visible resources selectable','6' in page.locator('#selection-count').inner_text())
    with page.expect_download() as info:page.locator('#export-selection').click()
    download=info.value
    with tempfile.TemporaryDirectory() as t:
        out=Path(t)/'selected.json';download.save_as(out)
        selected=json.loads(out.read_text())
        check('export contains 6 selected resources',len(selected['resources'])==6)
        check('export includes tasks',len(selected['tasks'])>0)
    page.locator('#clear-selection').click()
    check('clear selection',page.locator('#selection-count').inner_text()=='尚未选择资源')
    page.locator('[data-detail]').first.click()
    check('resource details modal opens',page.locator('#detail').is_visible())
    page.locator('#close-detail').click()
    page.locator('[data-tab="original"]').click()
    check('84 original rows',page.locator('#original tr').count()==84)
    page.locator('[data-tab="audit"]').click()
    check('15 audit items',page.locator('#audit > *').count()==15)
    page.locator('[data-tab="resources"]').click();page.locator('#reset').click()
    page.locator('#policy').select_option('review')
    check('3 unverified resources',page.locator('.card').count()==3)
    page.locator('#reset').click();page.locator('#help').click()
    check('help modal opens',page.locator('#detail').is_visible())
    page.locator('#close-detail').click()
    page.wait_for_timeout(3500)
    page.screenshot(path=str(ROOT/'reports/preview-desktop.png'))
    page.set_viewport_size({'width':390,'height':844})
    check('mobile has no document horizontal overflow',page.evaluate('document.documentElement.scrollWidth<=window.innerWidth'))
    page.screenshot(path=str(ROOT/'reports/preview-mobile.png'))
    check('no JavaScript errors',not errors)
    browser.close()
report={'type':'offline_DOM_smoke_test','mode':'HTML in-memory rendering with local status.js inlined; not a file:// launch or live download test','checks_passed':len(checks),'checks':checks,'javascript_errors':errors}
(ROOT/'reports/ui-test-results.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,ensure_ascii=False,indent=2))
