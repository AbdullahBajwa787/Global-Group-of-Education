import os

files = [
    'index.html',
    'public/index.html',
    'public/pages/home.html',
    'public/pages/index.html'
]

widget_html = '''
    <!-- 9.5 2ND LAST PART: FOOTER QUICK LINKS & UNIVERSITIES (EXACT MATCH TO USER SCREENSHOT) -->
    <section class="gge-footer-links-widget">
        <div class="container-fluid" style="max-width: 1320px; margin: 0 auto; padding: 0 30px;">
            <div class="row">
                <!-- Column 1: QUICK LINKS -->
                <div class="col-lg-3 col-md-6 col-12 gge-fl-col">
                    <h4 class="gge-fl-title">QUICK LINKS</h4>
                    <ul class="gge-fl-list">
                        <li><a href="/contact-us">Career counselling</a></li>
                        <li><a href="#about">Our Staff</a></li>
                        <li><a href="#about">Why GGE abroad?</a></li>
                        <li><a href="#services">Scholarship advice</a></li>
                        <li><a href="https://www.globalgroupofeducation.com/" target="_blank" rel="noopener">Blog</a></li>
                        <li><a href="/contact-us">Contact Us</a></li>
                    </ul>
                </div>

                <!-- Column 2: LIVING ABROAD -->
                <div class="col-lg-3 col-md-6 col-12 gge-fl-col">
                    <h4 class="gge-fl-title">LIVING ABROAD</h4>
                    <ul class="gge-fl-list">
                        <li><a href="#universities">Top Ranking Universities</a></li>
                        <li><a href="#destinations">Choose your destinations</a></li>
                        <li><a href="https://www.globalgroupofeducation.com/" target="_blank" rel="noopener">Guide for parents</a></li>
                        <li><a href="https://www.globalgroupofeducation.com/" target="_blank" rel="noopener">Students intakes</a></li>
                        <li><a href="#about">Our expertise</a></li>
                        <li><a href="https://www.globalgroupofeducation.com/" target="_blank" rel="noopener">Cost of studying abroad</a></li>
                    </ul>
                </div>

                <!-- Column 3 & 4: TRENDING UNIVERSITIES (2 SUB-COLUMNS) -->
                <div class="col-lg-6 col-md-12 col-12 gge-fl-col">
                    <h4 class="gge-fl-title">TRENDING UNIVERSITIES</h4>
                    <div class="row">
                        <div class="col-sm-6 col-12">
                            <ul class="gge-fl-list">
                                <li><a href="https://www.globalgroupofeducation.com/all-universities" target="_blank" rel="noopener">University of Chichester</a></li>
                                <li><a href="https://www.globalgroupofeducation.com/all-universities" target="_blank" rel="noopener">University of Sunderland</a></li>
                                <li><a href="https://www.globalgroupofeducation.com/all-universities" target="_blank" rel="noopener">University of Bolton</a></li>
                                <li><a href="https://www.globalgroupofeducation.com/all-universities" target="_blank" rel="noopener">Falmouth University</a></li>
                            </ul>
                        </div>
                        <div class="col-sm-6 col-12">
                            <ul class="gge-fl-list">
                                <li><a href="https://www.globalgroupofeducation.com/all-universities" target="_blank" rel="noopener">Queen's University Belfast</a></li>
                                <li><a href="https://www.globalgroupofeducation.com/all-universities" target="_blank" rel="noopener">University of Surrey</a></li>
                                <li><a href="https://www.globalgroupofeducation.com/all-universities" target="_blank" rel="noopener">South Bank University</a></li>
                                <li><a href="https://www.globalgroupofeducation.com/all-universities" target="_blank" rel="noopener">University of Portsmouth</a></li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
'''

target_tag = '<!-- 10. CLEAN OFFICIAL FOOTER (MATCHING media_1794644004430_01e7fe27.png) -->'

for fpath in files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        if target_tag in content:
            if 'gge-footer-links-widget' not in content:
                content = content.replace(target_tag, widget_html + '\n    ' + target_tag)
                print(f"Added 2nd last part to {fpath}")
            else:
                print(f"Already had 2nd last part in {fpath}")
        else:
            print(f"target_tag not found in {fpath}")

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)

# CSS additions
css_code = '''
/* ========================================================================== */
/* 2ND LAST PART: FOOTER LINKS WIDGET (QUICK LINKS, LIVING ABROAD, TRENDING)  */
/* ========================================================================== */
.gge-footer-links-widget {
    background: #0d2568 !important;
    padding: 65px 0 55px 0 !important;
    color: #ffffff !important;
    border-bottom: 1px solid rgba(255, 255, 255, 0.12) !important;
    position: relative !important;
    z-index: 10 !important;
}

.gge-fl-title {
    color: #ffffff !important;
    font-size: 16px !important;
    font-weight: 800 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.6px !important;
    margin-bottom: 22px !important;
    line-height: 1.3 !important;
}

.gge-fl-list {
    list-style: none !important;
    padding: 0 !important;
    margin: 0 !important;
}

.gge-fl-list li {
    margin-bottom: 12px !important;
}

.gge-fl-list li a {
    color: rgba(255, 255, 255, 0.88) !important;
    font-size: 14.5px !important;
    font-weight: 400 !important;
    text-decoration: none !important;
    transition: all 0.22s ease !important;
    display: inline-block !important;
}

.gge-fl-list li a:hover {
    color: #eca411 !important;
    transform: translateX(4px) !important;
    text-decoration: none !important;
}

@media (max-width: 991px) {
    .gge-fl-col {
        margin-bottom: 35px !important;
    }
}
'''

css_files = [
    'assets/css/custom.css',
    'public/assets/css/custom.css'
]

for csspath in css_files:
    if os.path.exists(csspath):
        with open(csspath, 'r', encoding='utf-8') as f:
            css_content = f.read()
        css_content += css_code
        with open(csspath, 'w', encoding='utf-8') as f:
            f.write(css_content)
        print(f"Appended widget CSS to {csspath}")

print("Done inserting 2nd last part.")
