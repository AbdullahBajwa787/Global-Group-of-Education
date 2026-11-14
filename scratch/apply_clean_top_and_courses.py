import json
import re

# 1. Update vercel.json
vercel_config = {
    "version": 2,
    "cleanUrls": True,
    "trailingSlash": False,
    "redirects": [
        {
            "source": "/courses",
            "destination": "https://www.globalgroupofeducation.com/undergraduate-courses",
            "permanent": False
        },
        {
            "source": "/doctorate-courses",
            "destination": "https://www.globalgroupofeducation.com/doctorate-courses",
            "permanent": False
        },
        {
            "source": "/postgraduate-courses",
            "destination": "https://www.globalgroupofeducation.com/postgraduate-courses",
            "permanent": False
        },
        {
            "source": "/undergraduate-courses",
            "destination": "https://www.globalgroupofeducation.com/undergraduate-courses",
            "permanent": False
        },
        {
            "source": "/pre-master-courses",
            "destination": "https://www.globalgroupofeducation.com/pre-master-courses",
            "permanent": False
        },
        {
            "source": "/foundation-courses",
            "destination": "https://www.globalgroupofeducation.com/foundation-courses",
            "permanent": False
        },
        {
            "source": "/english-language-courses",
            "destination": "https://www.globalgroupofeducation.com/english-language-courses",
            "permanent": False
        }
    ],
    "rewrites": [
        {
            "source": "/student-registration",
            "destination": "/contact-us.html"
        },
        {
            "source": "/student-registration/(.*)",
            "destination": "/contact-us.html"
        }
    ]
}

with open('vercel.json', 'w', encoding='utf-8') as f:
    json.dump(vercel_config, f, indent=2)
print("Updated vercel.json with course redirects!")

# 2. Update CSS to permanently eliminate all rewind / classic buttons and top bars
hide_css = """
/* Permanently remove Classic View, Rewind buttons, and Top announcement bar */
.gge-rewind-btn,
.gge-rewind-mini-btn,
.gge-footer-switch-btn,
.gge-top-announcement-bar,
.gge-crm-top-hdr,
.gge-mf-actions-wrap,
[data-gge-footer-toggle],
button[onclick*="toggleGGEView"],
a[href*="classic"],
.banner-slider {
    display: none !important;
    visibility: hidden !important;
    opacity: 0 !important;
    pointer-events: none !important;
    height: 0 !important;
    width: 0 !important;
    margin: 0 !important;
    padding: 0 !important;
    border: none !important;
    overflow: hidden !important;
}
"""

for path in ['assets/css/custom.css', 'public/assets/css/custom.css']:
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()
    c += "\n" + hide_css
    with open(path, 'w', encoding='utf-8') as f:
        f.write(c)
    print(f"Updated CSS: {path}")

# 3. Update HTML files: Remove top bar completely and verify courses links
home_files = ['index.html', 'public/index.html', 'public/pages/home.html', 'public/pages/index.html']

for fpath in home_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove gge-crm-top-hdr
    content = re.sub(
        r'<div class="gge-crm-top-hdr">.*?</div>\s*</div>\s*</div>',
        '',
        content,
        flags=re.DOTALL
    )
    content = re.sub(
        r'<div class="gge-crm-top-hdr">.*?</div>',
        '',
        content,
        flags=re.DOTALL
    )

    # Remove gge-top-announcement-bar if any
    content = re.sub(
        r'<div class="gge-top-announcement-bar">.*?</div>\s*</div>\s*</div>',
        '',
        content,
        flags=re.DOTALL
    )
    content = re.sub(
        r'<div class="gge-top-announcement-bar">.*?</div>',
        '',
        content,
        flags=re.DOTALL
    )

    # Ensure main Courses dropdown link points directly to courses
    content = content.replace(
        '<a href="#courses" class="gge-mk-nav-link"><i class="fa fa-graduation-cap"></i> Courses <i class="fa fa-angle-down"></i></a>',
        '<a href="https://www.globalgroupofeducation.com/undergraduate-courses" class="gge-mk-nav-link"><i class="fa fa-graduation-cap"></i> Courses <i class="fa fa-angle-down"></i></a>'
    )
    content = content.replace(
        '<a href="#courses" class="gge-drawer-sub-toggle"><i class="fa fa-graduation-cap"></i> Courses <i class="fa fa-angle-down"></i></a>',
        '<a href="https://www.globalgroupofeducation.com/undergraduate-courses" class="gge-drawer-sub-toggle"><i class="fa fa-graduation-cap"></i> Courses <i class="fa fa-angle-down"></i></a>'
    )

    # Remove any leftover rewind button
    content = re.sub(r'<button[^>]*toggleGGEView[^>]*>.*?</button>', '', content, flags=re.DOTALL)
    content = re.sub(r'<button[^>]*gge-rewind[^>]*>.*?</button>', '', content, flags=re.DOTALL)
    content = re.sub(r'<div class="gge-mf-actions-wrap">.*?</div>', '', content, flags=re.DOTALL)

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated HTML file: {fpath}")

print("All updates applied successfully!")
