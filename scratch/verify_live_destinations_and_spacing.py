import time
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 1440, "height": 900})
    url = "https://global-group-of-education-new-2.vercel.app/"
    print(f"Loading {url}...")
    page.goto(url, wait_until="domcontentloaded", timeout=60000)
    time.sleep(4)
    
    # 1. Snap courses section spacing
    courses = page.locator("#courses")
    courses.scroll_into_view_if_needed()
    time.sleep(1)
    courses.screenshot(path="scratch/verified_courses_spacing.png")
    print("Saved scratch/verified_courses_spacing.png")
    
    # 2. Snap destinations marquee
    dest = page.locator("#destinations")
    dest.scroll_into_view_if_needed()
    time.sleep(1)
    dest.screenshot(path="scratch/verified_destinations_alt.png")
    print("Saved scratch/verified_destinations_alt.png")
    
    # 3. Test redirection for Canada
    canada_link = page.locator(".gge-dest-card-item[href*='study-in-canada']").first
    href = canada_link.get_attribute("href")
    print("Canada link href:", href)
    
    browser.close()
