import re

with open('scratch/crm_style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Normalize
rules = re.findall(r'([^{}]+)\{([^{}]+)\}', css)
targets = ['about-section-ten', 'service-sctn', 'service-block', 'call-info-box', 'copyrgt-sctn', 'abt-txt']

with open('scratch/crm_formatted_rules.css', 'w', encoding='utf-8') as out:
    for sel, body in rules:
        sel_clean = sel.strip()
        if any(t in sel_clean for t in targets):
            out.write(f"{sel_clean} {{\n  {body.strip()}\n}}\n\n")

print("Formatted rules saved to scratch/crm_formatted_rules.css")
