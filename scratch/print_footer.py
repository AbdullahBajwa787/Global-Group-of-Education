import re

with open('scratch/crm_page.html', 'r', encoding='utf-8') as f:
    crm = f.read()

foot_match = re.search(r'(<footer.*|.*copyrgt.*)', crm, re.DOTALL)
idx = crm.find('copyrgt-sctn')
if idx != -1:
    print(crm[idx-200:idx+2500])
else:
    print("copyrgt-sctn not found, searching footer...")
    print(crm[-3000:])
