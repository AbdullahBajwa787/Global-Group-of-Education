import urllib.request
import re

with open('scratch/crm_page.html', 'r', encoding='utf-8') as f:
    text = f.read()

css_links = re.findall(r'<link[^>]+rel=["\']stylesheet["\'][^>]+href=["\']([^"\']+)["\']', text, re.IGNORECASE)
print('CSS Links:', css_links)

for css in css_links:
    if not css.startswith('http'):
        css_url = 'https://globalgroupofeducationportal.com/' + css
    else:
        css_url = css
    print('Checking:', css_url)
    try:
        req = urllib.request.Request(css_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as r:
            css_content = r.read().decode('utf-8', errors='ignore')
            for term in ['bnnr-video', 'bttn-bx', 'innr-bnr-bttn', 'colrd-bttn', 'trns-bttn', 'bnn-content']:
                matches = re.findall(rf'[^{{}}]*?\.{term}[^{{}}]*?\{{[^}}]*\}}', css_content)
                if matches:
                    print(f'Matches for {term}:')
                    for m in matches[:3]:
                        print('  ', m.strip())
    except Exception as e:
        print('Error:', e)
