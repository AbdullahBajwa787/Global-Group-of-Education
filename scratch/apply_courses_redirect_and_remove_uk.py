import os

files = [
    'index.html',
    'public/index.html',
    'public/pages/home.html',
    'public/pages/index.html'
]

# 1. Target UK address line in footer to remove
uk_address_target = '<li><i class="fa fa-map-marker"></i> 126 East Ferry Road, Canary Wharf, London, United Kingdom, E14 9FP</li>\n'
uk_address_target_alt = '<li><i class="fa fa-map-marker"></i> 126 East Ferry Road, Canary Wharf, London, United Kingdom, E14 9FP</li>'

for fpath in files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Remove UK address line
        if uk_address_target in content:
            content = content.replace(uk_address_target, '')
            print(f"Removed UK address from {fpath}")
        elif uk_address_target_alt in content:
            content = content.replace(uk_address_target_alt, '')
            print(f"Removed UK address (alt) from {fpath}")
        else:
            lines = content.splitlines(True)
            new_lines = [l for l in lines if '126 East Ferry Road' not in l]
            if len(new_lines) != len(lines):
                content = ''.join(new_lines)
                print(f"Filtered out UK address line from {fpath}")
            else:
                print(f"UK address line not found in {fpath}")

        # Remove target="_blank" from course cards and dropdown links so it redirects directly
        old_course_cards = [
            '<a href="https://www.globalgroupofeducation.com/doctorate-courses" target="_blank" rel="noopener" class="gge-course-card">',
            '<a href="https://www.globalgroupofeducation.com/postgraduate-courses" target="_blank" rel="noopener" class="gge-course-card">',
            '<a href="https://www.globalgroupofeducation.com/undergraduate-courses" target="_blank" rel="noopener" class="gge-course-card">',
            '<a href="https://www.globalgroupofeducation.com/pre-master-courses" target="_blank" rel="noopener" class="gge-course-card">',
            '<a href="https://www.globalgroupofeducation.com/foundation-courses" target="_blank" rel="noopener" class="gge-course-card">',
            '<a href="https://www.globalgroupofeducation.com/english-language-courses" target="_blank" rel="noopener" class="gge-course-card">'
        ]
        new_course_cards = [
            '<a href="https://www.globalgroupofeducation.com/doctorate-courses" class="gge-course-card">',
            '<a href="https://www.globalgroupofeducation.com/postgraduate-courses" class="gge-course-card">',
            '<a href="https://www.globalgroupofeducation.com/undergraduate-courses" class="gge-course-card">',
            '<a href="https://www.globalgroupofeducation.com/pre-master-courses" class="gge-course-card">',
            '<a href="https://www.globalgroupofeducation.com/foundation-courses" class="gge-course-card">',
            '<a href="https://www.globalgroupofeducation.com/english-language-courses" class="gge-course-card">'
        ]
        for old_c, new_c in zip(old_course_cards, new_course_cards):
            content = content.replace(old_c, new_c)

        # In dropdown
        old_dropdown_links = [
            '<li><a href="https://www.globalgroupofeducation.com/doctorate-courses" target="_blank"><i class="fa fa-certificate"></i> Doctorate Courses</a></li>',
            '<li><a href="https://www.globalgroupofeducation.com/postgraduate-courses" target="_blank"><i class="fa fa-graduation-cap"></i> Postgraduate Courses</a></li>',
            '<li><a href="https://www.globalgroupofeducation.com/undergraduate-courses" target="_blank"><i class="fa fa-book"></i> Undergraduate Courses</a></li>',
            '<li><a href="https://www.globalgroupofeducation.com/pre-master-courses" target="_blank"><i class="fa fa-university"></i> Pre-Master Courses</a></li>',
            '<li><a href="https://www.globalgroupofeducation.com/foundation-courses" target="_blank"><i class="fa fa-cubes"></i> Foundation Courses</a></li>',
            '<li><a href="https://www.globalgroupofeducation.com/english-language-courses" target="_blank"><i class="fa fa-language"></i> English Language Courses</a></li>'
        ]
        new_dropdown_links = [
            '<li><a href="https://www.globalgroupofeducation.com/doctorate-courses"><i class="fa fa-certificate"></i> Doctorate Courses</a></li>',
            '<li><a href="https://www.globalgroupofeducation.com/postgraduate-courses"><i class="fa fa-graduation-cap"></i> Postgraduate Courses</a></li>',
            '<li><a href="https://www.globalgroupofeducation.com/undergraduate-courses"><i class="fa fa-book"></i> Undergraduate Courses</a></li>',
            '<li><a href="https://www.globalgroupofeducation.com/pre-master-courses"><i class="fa fa-university"></i> Pre-Master Courses</a></li>',
            '<li><a href="https://www.globalgroupofeducation.com/foundation-courses"><i class="fa fa-cubes"></i> Foundation Courses</a></li>',
            '<li><a href="https://www.globalgroupofeducation.com/english-language-courses"><i class="fa fa-language"></i> English Language Courses</a></li>'
        ]
        for old_d, new_d in zip(old_dropdown_links, new_dropdown_links):
            content = content.replace(old_d, new_d)

        # View all courses button
        content = content.replace(
            '<a href="https://www.globalgroupofeducation.com/undergraduate-courses" target="_blank" class="gge-line-view-all">View All Courses &rarr;</a>',
            '<a href="https://www.globalgroupofeducation.com/undergraduate-courses" class="gge-line-view-all">View All Courses &rarr;</a>'
        )

        # Ensure direct click redirect JS is in the script
        redirect_js_snippet = '''
    // Direct redirect for all course cards and dropdown links
    var courseActionLinks = document.querySelectorAll('.gge-mk-nav-dropdown a, .gge-course-card, .gge-line-view-all');
    courseActionLinks.forEach(function(el) {
        el.addEventListener('click', function(e) {
            var targetUrl = this.getAttribute('href');
            if (targetUrl && targetUrl !== '#' && !targetUrl.startsWith('javascript:')) {
                e.preventDefault();
                window.location.href = targetUrl;
            }
        });
    });
'''
        if 'Direct redirect for all course cards' not in content:
            content = content.replace(
                '// Close on Escape key',
                redirect_js_snippet + '    // Close on Escape key'
            )
            print(f"Added direct redirect JS to {fpath}")

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)

print("All files updated successfully.")
