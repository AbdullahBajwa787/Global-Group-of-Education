import urllib.request
import re

for country in ['hungary', 'uae']:
    url = f'https://www.globalgroupofeducation.com/study-in-{country}'
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=8) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', html)
            print(f"Images in {country}:", imgs[:5])
    except Exception as e:
        print(f"Error {country}:", e)
