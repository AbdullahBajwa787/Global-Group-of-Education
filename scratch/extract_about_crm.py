with open('scratch/crm_page.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m = re.search(r'(<section[^>]*about-section-ten.*?</section>)', text, re.DOTALL)
if m:
    with open('scratch/crm_about_extracted.html', 'w', encoding='utf-8') as out:
        out.write(m.group(1))
    print("Length:", len(m.group(1)))
else:
    print("Not found")
