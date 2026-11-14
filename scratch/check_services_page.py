import urllib.request
import re

url = 'https://www.globalgroupofeducation.com/our-services'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
        print("our-services length:", len(html))
        h2s = re.findall(r'<h[1-4][^>]*>(.*?)</h[1-4]>', html, re.DOTALL)
        print("Headings on our-services:", [re.sub(r'<[^>]+>', '', h).strip() for h in h2s[:15]])
except Exception as e:
    print("Error:", e)
