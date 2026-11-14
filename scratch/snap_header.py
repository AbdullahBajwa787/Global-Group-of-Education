import time
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 1440, "height": 900})
    url = "https://global-group-of-education-new-2.vercel.app/"
    print(f"Loading {url}...")
    page.goto(url, wait_until="domcontentloaded", timeout=60000)
    time.sleep(4)
    
    header = page.locator(".gge-mk-header-wrap")
    header.screenshot(path="scratch/verified_fixed_header.png")
    print("Screenshot saved to scratch/verified_fixed_header.png")
    browser.close()
