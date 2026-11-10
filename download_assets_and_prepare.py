import os
import glob
import re
from urllib.parse import urlparse, urljoin
import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    )
}

session = requests.Session()
session.headers.update(HEADERS)

PUBLIC_DIR = os.path.join(os.getcwd(), "public")
PAGES_DIR = os.path.join(PUBLIC_DIR, "pages")
os.makedirs(PAGES_DIR, exist_ok=True)

# 1. Discover all assets from the HTML files
assets_to_download = set()

html_files = glob.glob("fetched_data/html_pages/*.html")
print(f"Scanning {len(html_files)} HTML files for assets...")

for fpath in html_files:
    with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
        soup = BeautifulSoup(f.read(), "html.parser")

    for tag, attr in [("link", "href"), ("script", "src"), ("img", "src"), ("source", "src")]:
        for el in soup.find_all(tag):
            val = el.get(attr)
            if not val:
                continue
            if val.startswith("//"):
                val = "https:" + val
            p = urlparse(val)
            if "globalgroupofeducation.com" in p.netloc or val.startswith("/"):
                # Normalize full url
                full_url = urljoin("https://www.globalgroupofeducation.com", val)
                assets_to_download.add(full_url)

print(f"Total assets to download: {len(assets_to_download)}")

# Download assets
downloaded_count = 0
for asset_url in sorted(assets_to_download):
    p = urlparse(asset_url)
    rel_path = p.path.lstrip("/")
    if not rel_path:
        continue
    local_path = os.path.join(PUBLIC_DIR, rel_path)
    os.makedirs(os.path.dirname(local_path), exist_ok=True)

    if os.path.exists(local_path) and os.path.getsize(local_path) > 0:
        continue

    try:
        r = session.get(asset_url, timeout=10)
        if r.status_code == 200:
            with open(local_path, "wb") as f:
                f.write(r.content)
            downloaded_count += 1
            if downloaded_count % 20 == 0:
                print(f"  Downloaded {downloaded_count}/{len(assets_to_download)}: {rel_path}")
        else:
            print(f"  Failed ({r.status_code}): {asset_url}")
    except Exception as e:
        print(f"  Error downloading {asset_url}: {e}")

print(f"Finished downloading {downloaded_count} new assets.")

# Also scan downloaded CSS files for fonts/images referenced inside CSS
css_files = glob.glob(os.path.join(PUBLIC_DIR, "**/*.css"), recursive=True)
print(f"Scanning {len(css_files)} CSS files for sub-assets (fonts/images)...")
css_url_pattern = re.compile(r'url\s*\((?:[\'"]?)([^\'")]+)(?:[\'"]?)\)', re.IGNORECASE)

sub_assets = set()
for cpath in css_files:
    try:
        with open(cpath, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
        matches = css_url_pattern.findall(content)
        for m in matches:
            m = m.strip()
            if m.startswith("data:") or m.startswith("#"):
                continue
            # Resolve relative to css file
            css_dir_rel = os.path.relpath(os.path.dirname(cpath), PUBLIC_DIR).replace("\\", "/")
            full_sub_url = urljoin(f"https://www.globalgroupofeducation.com/{css_dir_rel}/", m)
            sub_assets.add((m, full_sub_url, cpath))
    except Exception as e:
        pass

print(f"Found {len(sub_assets)} sub-assets in CSS files.")
for orig_m, full_sub_url, cpath in sub_assets:
    p = urlparse(full_sub_url)
    rel_path = p.path.lstrip("/")
    local_path = os.path.join(PUBLIC_DIR, rel_path)
    os.makedirs(os.path.dirname(local_path), exist_ok=True)
    if not os.path.exists(local_path) or os.path.getsize(local_path) == 0:
        try:
            r = session.get(full_sub_url, timeout=8)
            if r.status_code == 200:
                with open(local_path, "wb") as f:
                    f.write(r.content)
        except Exception:
            pass

# Now copy and rewrite all HTML pages into public/pages/
print("Rewriting and copying HTML pages to public/pages/...")
for hpath in html_files:
    fname = os.path.basename(hpath)
    with open(hpath, "r", encoding="utf-8", errors="ignore") as f:
        html = f.read()

    # Rewrite absolute domain links to root-relative links
    # https://www.globalgroupofeducation.com/ -> /
    # https://globalgroupofeducation.com/ -> /
    html = html.replace("https://www.globalgroupofeducation.com/", "/")
    html = html.replace("https://globalgroupofeducation.com/", "/")
    html = html.replace("http://www.globalgroupofeducation.com/", "/")
    html = html.replace("http://globalgroupofeducation.com/", "/")

    dest_path = os.path.join(PAGES_DIR, fname)
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(html)

print("Setup complete! Public folder ready.")
