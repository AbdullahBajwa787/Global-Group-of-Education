from playwright.sync_api import sync_playwright
import time

def verify_live():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            args=['--no-sandbox', '--disable-setuid-sandbox', '--disable-gpu']
        )
        page = browser.new_page(viewport={"width": 1440, "height": 900})
        
        url = 'https://global-group-of-education-new-2.vercel.app/'
        print(f"Loading live URL: {url}")
        page.goto(url, wait_until='domcontentloaded', timeout=45000)
        page.wait_for_timeout(3500)
        
        # 1. Top Hero
        page.screenshot(path='scratch/verified_live_top.png', animations='disabled')
        print("Saved scratch/verified_live_top.png")
        
        # 2. About section
        about = page.locator('#about')
        if about.count() > 0:
            about.scroll_into_view_if_needed()
            page.wait_for_timeout(1000)
            page.screenshot(path='scratch/verified_live_about.png', animations='disabled')
            print("Saved scratch/verified_live_about.png")

        # 3. Services section
        services = page.locator('#services')
        if services.count() > 0:
            services.scroll_into_view_if_needed()
            page.wait_for_timeout(1000)
            page.screenshot(path='scratch/verified_live_services.png', animations='disabled')
            print("Saved scratch/verified_live_services.png")

        # 4. Bottom of page
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        page.wait_for_timeout(1000)
        page.screenshot(path='scratch/verified_live_footer.png', animations='disabled')
        print("Saved scratch/verified_live_footer.png")
        
        browser.close()

if __name__ == '__main__':
    verify_live()
