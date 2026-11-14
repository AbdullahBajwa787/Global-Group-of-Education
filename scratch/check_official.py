import urllib.request
import re

url = 'https://www.globalgroupofeducation.com/'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
        print('globalgroupofeducation.com length:', len(html))
        with open('scratch/official_site.html', 'w', encoding='utf-8') as f:
            f.write(html)
        
        # Extract sections or headings
        h1s = re.findall(r'<h1[^>]*>(.*?)</h1>', html, re.DOTALL | re.IGNORECASE)
        h2s = re.findall(r'<h2[^>]*>(.*?)</h2>', html, re.DOTALL | re.IGNORECASE)
        h3s = re.findall(r'<h3[^>]*>(.*?)</h3>', html, re.DOTALL | re.IGNORECASE)
        print('H1s:', [re.sub(r'<[^>]+>', '', h).strip() for h in h1s[:5]])
        print('H2s:', [re.sub(r'<[^>]+>', '', h).strip() for h in h2s[:10]])
except Exception as e:
    print('Error:', e)
