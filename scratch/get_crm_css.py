import urllib.request
import re

css_url = 'https://globalgroupofeducationportal.com/css/style.css'
req = urllib.request.Request(css_url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req, timeout=10) as r:
        css = r.read().decode('utf-8', errors='ignore')
        
        with open('scratch/crm_style.css', 'w', encoding='utf-8') as f:
            f.write(css)
        print("Downloaded crm_style.css, length:", len(css))
        
        # Search for about-section-ten and service-sctn
        for kw in ['about-section-ten', 'service-sctn', 'call-info-box']:
            matches = re.findall(rf'[^{{}}]*?\.{kw}[^{{}}]*?\{{[^}}]*\}}', css)
            print(f"Matches for {kw}:", len(matches))
            for m in matches[:3]:
                print("  ", m.strip())
except Exception as e:
    print("Error:", e)
