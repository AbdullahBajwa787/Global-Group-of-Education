from playwright.sync_api import sync_playwright
import http.server
import socketserver
import threading
import time

PORT = 8092

class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        super().end_headers()

def run_server():
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        httpd.serve_forever()

t = threading.Thread(target=run_server, daemon=True)
t.start()
time.sleep(1)

with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=True,
        args=['--no-sandbox', '--disable-setuid-sandbox', '--disable-gpu']
    )
    page = browser.new_page(viewport={"width": 1440, "height": 900})
    
    page.goto(f'http://localhost:{PORT}/index.html', wait_until='domcontentloaded')
    page.wait_for_timeout(2500)
    
    # 1. Top Hero
    page.screenshot(path='scratch/verified_new_hero.png', animations='disabled')
    print("Saved scratch/verified_new_hero.png")
    
    # 2. About section
    about = page.locator('#about')
    if about.count() > 0:
        about.scroll_into_view_if_needed()
        page.wait_for_timeout(1000)
        page.screenshot(path='scratch/verified_new_about.png', animations='disabled')
        print("Saved scratch/verified_new_about.png")

    # 3. Services section
    services = page.locator('#services')
    if services.count() > 0:
        services.scroll_into_view_if_needed()
        page.wait_for_timeout(1000)
        page.screenshot(path='scratch/verified_new_services.png', animations='disabled')
        print("Saved scratch/verified_new_services.png")

    # 4. Footer & bottom CTA
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    page.wait_for_timeout(1000)
    page.screenshot(path='scratch/verified_new_footer.png', animations='disabled')
    print("Saved scratch/verified_new_footer.png")

    browser.close()
