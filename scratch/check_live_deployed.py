import urllib.request

url = 'https://global-group-of-education-new-2.vercel.app/'
try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=10) as resp:
        html = resp.read().decode('utf-8')
        print("Live site contains abt-img2.png:", 'abt-img2.png' in html)
        print("Live site contains map.png:", 'map.png' in html)
        print("Live site contains image-2:", 'class="image-2"' in html)
except Exception as e:
    print("Error:", e)
