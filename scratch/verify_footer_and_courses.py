import urllib.request

url = 'https://global-group-of-education-new-2.vercel.app/'
try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=10) as resp:
        html = resp.read().decode('utf-8')
        print("Live site contains UK address (should be False):", '126 East Ferry Road' in html)
        print("Live site contains course direct redirect script (should be True):", 'Direct redirect for all course cards' in html)
except Exception as e:
    print("Error:", e)
