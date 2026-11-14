with open('scratch/crm_page.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
header_end = text.find('</header>')
if header_end != -1:
    print(text[header_end:header_end + 3500])
