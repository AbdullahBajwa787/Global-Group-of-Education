import time
import subprocess
import sys
from playwright.sync_api import sync_playwright

def verify():
    # Use standard python http.server
    server = subprocess.Popen([sys.executable, "-m", "http.server", "8095"])
    time.sleep(2)
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page(viewport={"width": 1440, "height": 900})
            
            url = "http://localhost:8095/index.html"
            page.goto(url, wait_until="domcontentloaded", timeout=15000)
            time.sleep(2)
            
            about_section = page.locator("#about")
            about_section.scroll_into_view_if_needed()
            time.sleep(1)
            
            page.screenshot(path="scratch/verified_about_exact.png")
            about_section.screenshot(path="scratch/verified_about_section_exact.png")
            print("Screenshots saved successfully!")
            browser.close()
    finally:
        server.terminate()

if __name__ == "__main__":
    verify()
