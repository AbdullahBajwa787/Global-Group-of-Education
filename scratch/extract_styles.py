import re

with open('scratch/crm_style.css', 'r', encoding='utf-8') as f:
    css = f.read()

terms = [
    'about-section-ten',
    'sec-title',
    'abt-txt',
    'image-1',
    'image-2',
    'experience',
    'call-info-box',
    'service-sctn',
    'service-block',
    'copyrgt-sctn',
    'bttn-bx'
]

print("Extracting style definitions...")
extracted = []
for line in css.split('\n'):
    for t in terms:
        if f'.{t}' in line:
            extracted.append(line)
            break

print("Total relevant lines:", len(extracted))
with open('scratch/extracted_crm.css', 'w', encoding='utf-8') as f:
    f.write('\n'.join(extracted))
print("Saved to scratch/extracted_crm.css")
