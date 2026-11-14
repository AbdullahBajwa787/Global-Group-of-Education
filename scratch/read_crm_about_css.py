with open('scratch/crm_style.css', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'(\.about-section-ten[^{]*\{[^}]*\})', text)
for m in matches[:25]:
    print(m)
    print('-'*40)
