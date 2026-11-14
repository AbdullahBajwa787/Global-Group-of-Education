import time
import subprocess
import sys
from playwright.sync_api import sync_playwright

def test_dropdown():
    server = subprocess.Popen([sys.executable, "-m", "http.server", "8099"])
    time.sleep(2)
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page(viewport={"width": 1440, "height": 900})
            
            url = "http://localhost:8099/index.html"
            print(f"Loading {url}...")
            page.goto(url, wait_until="domcontentloaded", timeout=20000)
            time.sleep(2)
            
            courses_item = page.locator(".gge-mk-nav-item.gge-has-dropdown").nth(1)
            courses_link = courses_item.locator(".gge-mk-nav-link")
            courses_dropdown = courses_item.locator(".gge-mk-nav-dropdown")
            
            dest_item = page.locator(".gge-mk-nav-item.gge-has-dropdown").first
            dest_link = dest_item.locator(".gge-mk-nav-link")
            dest_dropdown = dest_item.locator(".gge-mk-nav-dropdown")
            
            # 1. Hover test: hover over Courses
            print("1. Hovering over Courses...")
            courses_link.hover()
            time.sleep(0.5)
            is_courses_visible_on_hover = courses_dropdown.is_visible()
            print("Courses visible on hover (expected False):", is_courses_visible_on_hover)
            page.screenshot(path="scratch/dropdown_hover_test.png")
            
            # 2. Click test: click Courses
            print("2. Clicking on Courses...")
            courses_link.click()
            time.sleep(0.5)
            is_courses_visible_on_click = courses_dropdown.is_visible()
            print("Courses visible on click (expected True):", is_courses_visible_on_click)
            page.screenshot(path="scratch/dropdown_click_test.png")
            
            # 3. Switch test: click Study Destinations
            print("3. Clicking on Study Destinations...")
            dest_link.click()
            time.sleep(0.5)
            is_dest_visible = dest_dropdown.is_visible()
            is_courses_still_visible = courses_dropdown.is_visible()
            print("Study Destinations visible (expected True):", is_dest_visible)
            print("Courses still visible (expected False):", is_courses_still_visible)
            page.screenshot(path="scratch/dropdown_dest_click_test.png")
            
            # 4. Outside click test: click outside
            print("4. Clicking outside on body...")
            page.locator(".gge-mk-hero-title").click()
            time.sleep(0.5)
            is_dest_after_outside = dest_dropdown.is_visible()
            print("Study Destinations visible after outside click (expected False):", is_dest_after_outside)
            page.screenshot(path="scratch/dropdown_outside_click_test.png")
            
            browser.close()
            print("TEST COMPLETED SUCCESSFULLY!")
    finally:
        server.terminate()

if __name__ == "__main__":
    test_dropdown()
