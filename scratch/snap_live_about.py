import time
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 1440, "height": 900})
    url = "https://global-group-of-education-new-2.vercel.app/"
    print(f"Loading {url}...")
    page.goto(url, wait_until="domcontentloaded", timeout=60000)
    time.sleep(4)
    
    about = page.locator("#about")
    about.scroll_into_view_if_needed()
    time.sleep(2)
    
    about.screenshot(path="scratch/live_about_verified_crm.png")
    print("Screenshot saved to scratch/live_about_verified_crm.png")
    browser.close()
