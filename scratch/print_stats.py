import re

with open('scratch/crm_page.html', 'r', encoding='utf-8') as f:
    crm = f.read()

idx = crm.find('fun-fct-sctn')
if idx != -1:
    print(crm[idx-50:idx+1500])

idx2 = crm.find('wwd-sctn')
if idx2 != -1:
    print("\n--- WWD SCTN ---")
    print(crm[idx2-50:idx2+1500])
