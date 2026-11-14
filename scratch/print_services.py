import re

with open('scratch/crm_page.html', 'r', encoding='utf-8') as f:
    crm = f.read()

m = re.search(r'(<section class="service-sctn".*?</section>)', crm, re.DOTALL)
if m:
    print(m.group(1))
