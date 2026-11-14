with open('scratch/crm_page.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
print("TITLE:", re.findall(r'<title>(.*?)</title>', text, re.IGNORECASE))
# Print first 1500 characters of body
body_match = re.search(r'<body[^>]*>(.*?)</body>', text, re.DOTALL | re.IGNORECASE)
if body_match:
    body = body_match.group(1)
    print("BODY START:")
    print(body[:2000])
