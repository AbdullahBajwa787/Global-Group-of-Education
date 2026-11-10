import os
import re
import sys
import mimetypes
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, unquote
import requests

PORT = 8080
PUBLIC_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "public")
PAGES_DIR = os.path.join(PUBLIC_DIR, "pages")
REMOTE_HOST = "https://www.globalgroupofeducation.com"

# Prepare mimetypes
mimetypes.init()
mimetypes.add_type("application/javascript", ".js")
mimetypes.add_type("text/css", ".css")
mimetypes.add_type("image/svg+xml", ".svg")
mimetypes.add_type("font/woff", ".woff")
mimetypes.add_type("font/woff2", ".woff2")
mimetypes.add_type("font/ttf", ".ttf")
mimetypes.add_type("font/eot", ".eot")

def sanitize_page_name(path):
    path = path.strip("/")
    if not path:
        return "home.html"
    sanitized = re.sub(r'[^a-zA-Z0-9_\-]', '_', path)
    return f"{sanitized[:120]}.html"

class LocalEducationServer(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        path = unquote(parsed.path)

        # 1. Handle root / home
        if path in ["", "/"]:
            self.serve_html_file(os.path.join(PAGES_DIR, "home.html"))
            return

        # 2. Check direct static files in public directory (assets, uploads, etc.)
        direct_file_path = os.path.join(PUBLIC_DIR, path.lstrip("/"))
        if os.path.isfile(direct_file_path):
            self.serve_static_file(direct_file_path)
            return

        # 3. Check if it's a page route (e.g. /about-us, /universities/...)
        clean_name = sanitize_page_name(path)
        page_file_path = os.path.join(PAGES_DIR, clean_name)
        if os.path.isfile(page_file_path):
            self.serve_html_file(page_file_path)
            return

        # Also try path with .html directly
        alt_page_path = os.path.join(PAGES_DIR, f"{path.strip('/')}.html")
        if os.path.isfile(alt_page_path):
            self.serve_html_file(alt_page_path)
            return

        # 4. Fallback: Proxy from live site and cache locally
        remote_url = REMOTE_HOST + path
        try:
            r = requests.get(remote_url, headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            }, timeout=8)
            if r.status_code == 200:
                content_type = r.headers.get("Content-Type", "text/plain")
                body = r.content
                if "text/html" in content_type:
                    text_html = r.text
                    text_html = text_html.replace("https://www.globalgroupofeducation.com/", "/")
                    text_html = text_html.replace("https://globalgroupofeducation.com/", "/")
                    body = text_html.encode("utf-8")
                    with open(page_file_path, "wb") as f:
                        f.write(body)
                else:
                    os.makedirs(os.path.dirname(direct_file_path), exist_ok=True)
                    with open(direct_file_path, "wb") as f:
                        f.write(body)

                self.send_response(200)
                self.send_header("Content-Type", content_type)
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)
                return
        except Exception as e:
            sys.stderr.write(f"Proxy fallback error for {remote_url}: {e}\n")

        # 404 Not Found
        self.send_response(404)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        not_found_html = f"""
        <!DOCTYPE html>
        <html>
        <head><title>404 - Page Not Found</title></head>
        <body style="font-family:sans-serif;text-align:center;padding:50px;">
          <h1>404 - Page Not Found</h1>
          <p>Requested URL: <code>{path}</code></p>
          <p><a href="/" style="color:#007bff;text-decoration:none;font-weight:bold;">&larr; Back to Home</a></p>
        </body>
        </html>
        """
        self.wfile.write(not_found_html.encode("utf-8"))

    def serve_html_file(self, file_path):
        try:
            with open(file_path, "rb") as f:
                content = f.read()
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(content)))
            self.end_headers()
            self.wfile.write(content)
        except Exception as e:
            self.send_error(500, f"Error reading file: {e}")

    def serve_static_file(self, file_path):
        try:
            mime_type, _ = mimetypes.guess_type(file_path)
            if not mime_type:
                mime_type = "application/octet-stream"
            with open(file_path, "rb") as f:
                content = f.read()
            self.send_response(200)
            self.send_header("Content-Type", mime_type)
            self.send_header("Content-Length", str(len(content)))
            self.send_header("Cache-Control", "public, max-age=86400")
            self.end_headers()
            self.wfile.write(content)
        except Exception as e:
            self.send_error(500, f"Error reading static file: {e}")

    def log_message(self, format, *args):
        sys.stderr.write(f"[{self.log_date_time_string()}] {format % args}\n")
        sys.stderr.flush()

if __name__ == "__main__":
    server_address = ("0.0.0.0", PORT)
    httpd = ThreadingHTTPServer(server_address, LocalEducationServer)
    print("=" * 60, flush=True)
    print(f"  GLOBAL GROUP OF EDUCATION - LOCALHOST SERVER RUNNING", flush=True)
    print(f"  Open in Browser: http://localhost:{PORT}", flush=True)
    print(f"  Network Address: http://127.0.0.1:{PORT}", flush=True)
    page_count = len(os.listdir(PAGES_DIR)) if os.path.exists(PAGES_DIR) else 0
    print(f"  Serving: {page_count} prefetched pages + local static assets", flush=True)
    print("=" * 60, flush=True)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server.", flush=True)
        httpd.server_close()
