import re

home_files = ['index.html', 'public/index.html', 'public/pages/home.html', 'public/pages/index.html']

for fpath in home_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # In footer foot-contct-dtl, add the full UK address if not present
    old_contact = '''                        <ul>
                            <li><i class="fa fa-phone"></i> <a href="tel:+447586589659">+44 7586589659</a></li>
                            <li><i class="fa fa-envelope-o"></i> <a href="mailto:london@globalgroupofeducation.com">london@globalgroupofeducation.com</a></li>
                            <li><i class="fa fa-globe"></i> <a href="https://www.globalgroupofeducation.com/" target="_blank">Global Group of Education</a></li>
                        </ul>'''

    new_contact = '''                        <ul>
                            <li><i class="fa fa-map-marker"></i> 126 East Ferry Road, Canary Wharf, London, United Kingdom, E14 9FP</li>
                            <li><i class="fa fa-phone"></i> <a href="tel:+447586589659">+44 7586589659</a></li>
                            <li><i class="fa fa-envelope-o"></i> <a href="mailto:london@globalgroupofeducation.com">london@globalgroupofeducation.com</a></li>
                            <li><i class="fa fa-globe"></i> <a href="https://www.globalgroupofeducation.com/" target="_blank">Global Group of Education</a></li>
                        </ul>'''

    if old_contact in content:
        content = content.replace(old_contact, new_contact)
        print(f"[{fpath}] Updated footer with full UK address!")

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Footer address check completed!")
