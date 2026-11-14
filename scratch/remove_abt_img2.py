import os

files = [
    'index.html',
    'public/index.html',
    'public/pages/home.html',
    'public/pages/index.html'
]

target_line = '<img src="/assets/images/about/abt-img2.png" alt="University Campus" class="about-img-2">\n'

for fpath in files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Try both with and without leading spaces
        if target_line in content:
            content = content.replace(target_line, '')
            print(f"Removed exact line from {fpath}")
        else:
            lines = content.splitlines(True)
            new_lines = [l for l in lines if 'abt-img2.png' not in l]
            if len(new_lines) != len(lines):
                content = ''.join(new_lines)
                print(f"Filtered out abt-img2 line from {fpath}")
            else:
                print(f"abt-img2 not found in {fpath}")
                
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)

print("Done removing abt-img2.")
