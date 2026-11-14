import re

with open('scratch/official_site.html', 'r', encoding='utf-8') as f:
    text = f.read()

print("HTML Length:", len(text))

# Search for services in official site
matches = re.findall(r'<section[^>]*>.*?</section>', text, re.DOTALL)
print("Total sections found:", len(matches))
for i, m in enumerate(matches):
    first_line = m.strip().split('\n')[0]
    h2 = re.findall(r'<h[1-4][^>]*>(.*?)</h[1-4]>', m, re.DOTALL)
    h2_clean = [re.sub(r'<[^>]+>', '', h).strip() for h in h2]
    print(f"Section {i}: {first_line[:80]} | Headings: {h2_clean}")
