import re

with open('scratch/crm_page.html', 'r', encoding='utf-8') as f:
    crm = f.read()

sections = re.findall(r'<section[^>]*class=["\']([^"\']+)["\'][^>]*>', crm)
print("Sections in CRM page:", sections)
