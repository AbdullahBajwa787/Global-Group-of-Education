import re

print("Checking CRM page services:")
with open('scratch/crm_page.html', 'r', encoding='utf-8') as f:
    crm = f.read()

services_match = re.search(r'(<section[^>]*service[^>]*>.*?</section>)', crm, re.DOTALL | re.IGNORECASE)
if services_match:
    print("Found CRM services:", services_match.group(1)[:1000])
else:
    # search for services in crm
    for match in re.finditer(r'<section[^>]*>.*?</section>', crm, re.DOTALL):
        sec = match.group(0)
        if 'service' in sec.lower() or 'offer' in sec.lower():
            print("Found section with service in CRM:", sec[:500])

print("\nChecking official_site services:")
with open('scratch/official_site.html', 'r', encoding='utf-8') as f:
    off = f.read()

for match in re.finditer(r'<section[^>]*>.*?</section>', off, re.DOTALL):
    sec = match.group(0)
    if 'service' in sec.lower() or 'importance' in sec.lower() or 'offer' in sec.lower():
        print("Found section with service in official site:", sec[:600])
