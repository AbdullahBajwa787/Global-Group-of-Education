import os
import sys
import json
import re
import time
from urllib.parse import urljoin, urlparse, urldefrag
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.globalgroupofeducation.com/"
ALLOWED_HOSTS = {"globalgroupofeducation.com", "www.globalgroupofeducation.com"}

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
}

OUTPUT_DIR = os.path.join(os.getcwd(), "fetched_data")
HTML_DIR = os.path.join(OUTPUT_DIR, "html_pages")
os.makedirs(HTML_DIR, exist_ok=True)

session = requests.Session()
session.headers.update(HEADERS)

visited_urls = set()
# Start with priority core URLs
priority_urls = [
    "https://www.globalgroupofeducation.com/",
    "https://www.globalgroupofeducation.com/about-us",
    "https://www.globalgroupofeducation.com/our-services",
    "https://www.globalgroupofeducation.com/contact-us",
    "https://www.globalgroupofeducation.com/why-gge-abroad",
    "https://www.globalgroupofeducation.com/faq",
    "https://www.globalgroupofeducation.com/our-staff",
    "https://www.globalgroupofeducation.com/all-universities",
    "https://www.globalgroupofeducation.com/choose-your-destination",
    "https://www.globalgroupofeducation.com/study-in-uk",
    "https://www.globalgroupofeducation.com/study-in-usa",
    "https://www.globalgroupofeducation.com/study-in-canada",
    "https://www.globalgroupofeducation.com/study-in-australia",
    "https://www.globalgroupofeducation.com/study-in-hungary",
    "https://www.globalgroupofeducation.com/study-in-uae",
    "https://www.globalgroupofeducation.com/doctorate-courses",
    "https://www.globalgroupofeducation.com/postgraduate-courses",
    "https://www.globalgroupofeducation.com/undergraduate-courses",
    "https://www.globalgroupofeducation.com/pre-master-courses",
    "https://www.globalgroupofeducation.com/foundation-courses",
    "https://www.globalgroupofeducation.com/english-language-courses",
    "https://www.globalgroupofeducation.com/scholarship-advice",
    "https://www.globalgroupofeducation.com/career-counselling",
    "https://www.globalgroupofeducation.com/guide-for-parents",
    "https://www.globalgroupofeducation.com/cost-of-studing-abroad",
    "https://www.globalgroupofeducation.com/student-intakes",
    "https://www.globalgroupofeducation.com/university-rankings",
    "https://www.globalgroupofeducation.com/privacy",
    "https://www.globalgroupofeducation.com/term-of-use",
]

urls_to_visit = list(priority_urls)
pages_data = []

def clean_filename(url):
    path = urlparse(url).path.strip("/")
    if not path:
        return "home.html"
    sanitized = re.sub(r'[^a-zA-Z0-9_\-]', '_', path)
    return f"{sanitized[:120]}.html"

def categorize_url(url):
    path = urlparse(url).path.lower()
    if path in ["", "/"]:
        return "home"
    if path.startswith("/universities/"):
        return "university"
    if path.startswith("/course/"):
        return "course"
    if "study-in-" in path or path == "/choose-your-destination":
        return "destination"
    if any(k in path for k in ["courses", "doctorate", "postgraduate", "undergraduate", "pre-master", "foundation"]):
        return "course_category"
    if any(k in path for k in ["about", "service", "contact", "staff", "why-gge", "faq", "all-universities"]):
        return "core"
    return "guide_or_policy"

print(f"Total starting queue: {len(urls_to_visit)}")
crawl_limit = 120

while urls_to_visit and len(visited_urls) < crawl_limit:
    current_url = urls_to_visit.pop(0)
    current_url, _ = urldefrag(current_url)

    # Normalize url to www
    p = urlparse(current_url)
    if p.netloc == "globalgroupofeducation.com":
        current_url = current_url.replace("://globalgroupofeducation.com", "://www.globalgroupofeducation.com")
        p = urlparse(current_url)

    if current_url in visited_urls:
        continue

    if p.netloc not in ALLOWED_HOSTS:
        continue

    # Skip files
    if any(p.path.lower().endswith(ext) for ext in [
        '.jpg', '.jpeg', '.png', '.gif', '.svg', '.webp', '.pdf', '.css', '.js', '.zip', '.mp4'
    ]):
        continue

    print(f"[{len(visited_urls)+1}/{crawl_limit}] Fetching: {current_url}")
    visited_urls.add(current_url)

    try:
        resp = session.get(current_url, timeout=12)
        if resp.status_code != 200:
            print(f"  Status code: {resp.status_code}")
            continue

        if "text/html" not in resp.headers.get("Content-Type", ""):
            continue

        html = resp.text
        filename = clean_filename(current_url)
        with open(os.path.join(HTML_DIR, filename), "w", encoding="utf-8") as f:
            f.write(html)

        soup = BeautifulSoup(html, "html.parser")

        title = soup.title.string.strip() if soup.title and soup.title.string else ""
        meta_desc = ""
        desc_el = soup.find("meta", attrs={"name": "description"}) or soup.find("meta", attrs={"property": "og:description"})
        if desc_el and desc_el.get("content"):
            meta_desc = desc_el["content"].strip()

        # Extract headings
        h1s = [h.get_text(strip=True) for h in soup.find_all("h1") if h.get_text(strip=True)]
        h2s = [h.get_text(strip=True) for h in soup.find_all("h2") if h.get_text(strip=True)]
        h3s = [h.get_text(strip=True) for h in soup.find_all("h3") if h.get_text(strip=True)]

        # Extract main text
        for s in soup(["script", "style", "nav", "footer"]):
            s.decompose()

        body_text_blocks = [
            t.get_text(" ", strip=True) for t in soup.find_all(["p", "li", "article", "blockquote"]) 
            if len(t.get_text(strip=True)) > 20
        ]
        
        # Deduplicate blocks while preserving order
        seen_blocks = set()
        clean_text_blocks = []
        for b in body_text_blocks:
            if b not in seen_blocks:
                seen_blocks.add(b)
                clean_text_blocks.append(b)

        # Collect outgoing internal links to add to crawl
        # Re-parse original html to get nav/footer links
        soup_links = BeautifulSoup(html, "html.parser")
        for a in soup_links.find_all("a", href=True):
            href = a["href"].strip()
            full_url = urljoin(current_url, href)
            full_url, _ = urldefrag(full_url)
            parsed_full = urlparse(full_url)
            if parsed_full.netloc in ALLOWED_HOSTS:
                if full_url not in visited_urls and full_url not in urls_to_visit:
                    urls_to_visit.append(full_url)

        cat = categorize_url(current_url)
        page_record = {
            "url": current_url,
            "category": cat,
            "filename": filename,
            "title": title,
            "meta_description": meta_desc,
            "headings": {
                "h1": h1s,
                "h2": h2s,
                "h3": h3s[:20]
            },
            "content": clean_text_blocks,
            "raw_text_summary": "\n\n".join(clean_text_blocks[:15])
        }
        pages_data.append(page_record)

    except Exception as e:
        print(f"  Error on {current_url}: {e}")

# Separate into structured collections
universities = [p for p in pages_data if p["category"] == "university"]
destinations = [p for p in pages_data if p["category"] == "destination"]
courses = [p for p in pages_data if p["category"] == "course"]
course_categories = [p for p in pages_data if p["category"] == "course_category"]
core_pages = [p for p in pages_data if p["category"] in ["core", "home", "guide_or_policy"]]

# Save master data
with open(os.path.join(OUTPUT_DIR, "site_data.json"), "w", encoding="utf-8") as f:
    json.dump({
        "site_name": "Global Group of Education",
        "base_url": BASE_URL,
        "total_crawled": len(pages_data),
        "pages": pages_data
    }, f, indent=2, ensure_ascii=False)

with open(os.path.join(OUTPUT_DIR, "universities.json"), "w", encoding="utf-8") as f:
    json.dump(universities, f, indent=2, ensure_ascii=False)

with open(os.path.join(OUTPUT_DIR, "destinations.json"), "w", encoding="utf-8") as f:
    json.dump(destinations, f, indent=2, ensure_ascii=False)

with open(os.path.join(OUTPUT_DIR, "courses.json"), "w", encoding="utf-8") as f:
    json.dump(courses, f, indent=2, ensure_ascii=False)

# Create a clean Markdown overview document
md_summary = f"""# Global Group of Education - Website Data Prefetch Report

**Source Website:** [{BASE_URL}]({BASE_URL})  
**Total Pages Prefetched:** {len(pages_data)}  
**Categories:**
- **Core & Information Pages:** {len(core_pages)}
- **Study Destinations:** {len(destinations)}
- **Universities:** {len(universities)}
- **Courses & Programs:** {len(courses) + len(course_categories)}

---

## 1. Company / Agency Profile
- **Organization:** Global Group of Education (GGE)
- **Primary Function:** International Student Recruitment, Admissions & Educational Consultancy
- **UK Head Office:** Level 18, 40 Bank Street, Canary Wharf, London, E14 5NR, United Kingdom
- **Phone:** +44 7586589659
- **Email:** london@globalgroupofeducation.com
- **Core Mission:** Assisting students globally in course selection, university placement, scholarship acquisition, visa clearance, and pre-departure settlement.

---

## 2. Study Destinations
"""
for d in destinations:
    md_summary += f"\n### {d['title'] or d['url']}\n- **URL:** {d['url']}\n"
    if d['headings']['h1']:
        md_summary += f"- **Headline:** {', '.join(d['headings']['h1'])}\n"
    if d['content']:
        sample = d['content'][:3]
        for s in sample:
            md_summary += f"  - {s[:200]}...\n"

md_summary += "\n---\n\n## 3. Partner Universities\n"
for u in universities:
    title = u['title'].replace(" - Global Group of Education", "").strip()
    md_summary += f"- **{title}** ([Link]({u['url']}))\n"
    if u['content']:
        md_summary += f"  - *Summary:* {u['content'][0][:250]}...\n"

md_summary += "\n---\n\n## 4. Course Categories\n"
for c in course_categories:
    md_summary += f"- **{c['title']}** ({c['url']})\n"

md_summary += f"""
---

## 5. Storage Structure
- `fetched_data/site_data.json`: Complete scraped data with all text and headings.
- `fetched_data/universities.json`: List of partner universities and details.
- `fetched_data/destinations.json`: Comprehensive data for all target study destinations.
- `fetched_data/courses.json`: Catalog of individual courses.
- `fetched_data/html_pages/`: Raw static HTML copies of all {len(pages_data)} crawled web pages.
"""

with open(os.path.join(OUTPUT_DIR, "site_summary.md"), "w", encoding="utf-8") as f:
    f.write(md_summary)

print(f"\n[DONE] Crawl finished! {len(pages_data)} pages downloaded and processed.")
print(f"Summary written to {os.path.join(OUTPUT_DIR, 'site_summary.md')}")
