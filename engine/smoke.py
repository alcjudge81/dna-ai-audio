import sys
from playwright.sync_api import sync_playwright
errs = []
with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--no-sandbox"])
    pg = b.new_page(viewport={"width": 390, "height": 844})
    pg.on("pageerror", lambda e: errs.append("PAGEERROR " + str(e)))
    pg.on("console", lambda m: errs.append(m.text) if m.type == "error" and "ERR_" not in m.text and "Failed to load" not in m.text else None)
    pg.goto("file://" + sys.argv[1]); pg.wait_for_timeout(1200)
    n = pg.evaluate("document.querySelectorAll('.row').length")
    pg.click("#item-2-3 summary"); pg.wait_for_timeout(200)
    has = pg.evaluate("!!document.querySelector('#item-2-3 .panel textarea') && !!document.querySelector('#item-2-3 .panel a.btn')")
    pg.click("#v-core"); pg.wait_for_timeout(100)
    vis = pg.evaluate("Array.from(document.querySelectorAll('.row')).filter(r=>!r.hidden).length")
    w = pg.evaluate("[document.documentElement.scrollWidth, window.innerWidth]")
    txt = pg.evaluate("[document.getElementById('t-core').textContent, document.getElementById('lede').textContent, document.getElementById('next-t').textContent]")
    pg.click("#v-all"); pg.screenshot(path=sys.argv[2]); b.close()
print("rows", n, "| panel ok", has, "| core-only rows", vis, "| width", w, "| errors", errs[:4]); print(txt)
