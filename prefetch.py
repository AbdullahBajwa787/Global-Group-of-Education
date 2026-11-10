import os
import sys
import json
import re
from urllib.parse import urljoin, urlparse, urldefrag
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://globalgroupofeducation.com/"
DOMAIN = urlparse(BASE_URL).netloc

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
}

OUTPUT_DIR = os.path.join(os.getcwd(), "fetched_data")
HTML_DIR = os.path.join(OUTPUT_DIR, "html_pages")
os.makedirs(HTML_DIR, exist_ok=True)

session = requests.Session()
session.headers.update(HEADERS)

visited_urls = set()
urls_to_visit = [BASE_URL]
site_pages_data = []

def clean_filename(url):
    path = urlparse(url).path.strip("/")
    if not path:
        return "index.html"
    sanitized = re.sub(r'[^a-zA-Z0-9_\-]', '_', path)
    return f"{sanitized[:100]}.html"

print(f"Starting crawl of {BASE_URL}...")

while urls_to_visit and len(visited_urls) < 60:
    current_url = urls_to_visit.pop(0)
    current_url, _ = urldefrag(current_url)

    if current_url in visited_urls:
        continue

    parsed = urlparse(current_url)
    if parsed.netloc != DOMAIN:
        continue

    # Skip obvious asset files from being treated as HTML pages
    if any(parsed.path.lower().endswith(ext) for ext in [
        '.jpg', '.jpeg', '.png', '.gif', '.svg', '.webp', '.pdf', '.css', '.js', '.zip', '.mp4'
    ]):
        continue

    print(f"[{len(visited_urls)+1}] Fetching: {current_url}")
    visited_urls.add(current_url)

    try:
        resp = session.get(current_url, timeout=15)
        if resp.status_code != 200:
            print(f"  -> Status code: {resp.status_code}")
            continue

        content_type = resp.headers.get("Content-Type", "")
        if "text/html" not in content_type:
            continue

        html_content = resp.text
        # Save raw HTML
        filename = clean_filename(current_url)
        with open(os.path.join(HTML_DIR, filename), "w", encoding="utf-8") as f:
            f.write(html_content)

        soup = BeautifulSoup(html_content, "html.parser")

        # Extract meta details
        title = soup.title.string.strip() if soup.title and soup.title.string else ""
        meta_desc = ""
        meta_keywords = ""
        desc_tag = soup.find("meta", attrs={"name": "description"}) or soup.find("meta", attrs={"property": "og:description"})
        if desc_tag and desc_tag.get("content"):
            meta_desc = desc_tag["content"].strip()
        
        keywords_tag = soup.find("meta", attrs={"name": "keywords"})
        if keywords_tag and keywords_tag.get("content"):
            meta_keywords = keywords_tag["content"].strip()

        # Headings
        headings = {
            "h1": [h.get_text(strip=True) for h in soup.find_all("h1") if h.get_text(strip=True)],
            "h2": [h.get_text(strip=True) for h in soup.find_all("h2") if h.get_text(strip=True)],
            "h3": [h.get_text(strip=True) for h in soup.find_all("h3") if h.get_text(strip=True)],
        }

        # Text paragraphs
        paragraphs = [p.get_text(strip=True) for p in soup.find_all(["p", "li"]) if p.get_text(strip=True)]
        
        # Images
        images = []
        for img in soup.find_all("img"):
            src = img.get("src")
            if src:
                images.append({
                    "src": urljoin(current_url, src),
                    "alt": img.get("alt", "").strip()
                })

        # Links
        page_links = []
        for a in soup.find_all("a", href=True):
            href = a["href"].strip()
            full_url = urljoin(current_url, href)
            full_url, _ = urldefrag(full_url)
            text = a.get_text(strip=True)
            page_links.append({"text": text, "url": full_url})

            parsed_link = urlparse(full_url)
            if parsed_link.netloc == DOMAIN and full_url not in visited_urls and full_url not in urls_to_visit:
                urls_to_visit.append(full_url)

        page_data = {
            "url": current_url,
            "filename": filename,
            "title": title,
            "meta_description": meta_desc,
            "meta_keywords": meta_keywords,
            "headings": headings,
            "paragraphs_count": len(paragraphs),
            "content_sample": paragraphs[:30],
            "all_text": "\n".join(paragraphs),
            "images": images,
            "internal_links_count": len([l for l in page_links if urlparse(l['url']).netloc == DOMAIN]),
            "external_links": [l for l in page_links if urlparse(l['url']).netloc != DOMAIN and l['url'].startswith('http')]
        }
        site_pages_data.append(page_data)

    except Exception as e:
        print(f"  Error fetching {current_url}: {e}")

# Save full structured json
json_path = os.path.join(OUTPUT_DIR, "website_data.json")
with open(json_path, "w", encoding="utf-8") as f:
    json.dump({
        "base_url": BASE_URL,
        "total_pages_fetched": len(site_pages_data),
        "pages": site_pages_data
    }, f, indent=2, ensure_ascii=False)

print(f"\nFinished crawling! Fetched {len(site_pages_data)} pages.")
print(f"Saved structured JSON data to: {json_path}")
print(f"Saved HTML files to: {HTML_DIR}")
