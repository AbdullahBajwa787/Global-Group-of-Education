import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

print("Sections currently in index.html:")
for s in re.finditer(r'<section[^>]*>', text):
    tag = s.group(0)
    print("  TAG:", tag[:100])

print("\nHeadings (H1, H2, H3):")
for h in re.finditer(r'<(h[1-3])[^>]*>(.*?)</\1>', text, re.DOTALL):
    clean = re.sub(r'<[^>]+>', '', h.group(2)).strip().replace('\n', ' ')
    print(f"  {h.group(1)}: {clean}")
