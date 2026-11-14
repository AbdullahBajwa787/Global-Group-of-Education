import re

NEW_HERO = '''    <!-- 2. HERO SECTION WITH CRM BACKGROUND VIDEO & CRM-STYLE BUTTONS (MATCHING IMAGE 2) -->
    <section class="gge-mk-hero-section">
        <div class="gge-mk-video-wrapper">
            <video autoplay loop muted playsinline preload="auto" poster="/assets/images/banner1.jpg" class="gge-mk-hero-video">
                <source src="/assets/videos/crm_video.mp4" type="video/mp4">
                <source src="https://globalgroupofeducationportal.com/images/video.mp4" type="video/mp4">
                Your browser does not support HTML5 video.
            </video>
            <div class="gge-mk-video-overlay"></div>
        </div>
        <div class="gge-mk-hero-grid gge-mk-hero-fullwidth">
            <!-- Left Hero Content -->
            <div class="gge-mk-hero-left">
                <span class="gge-mk-hero-tag">Welcome and <span class="gge-tag-gold">Join Us for Success</span></span>
                <h1 class="gge-mk-hero-title">Your Gateway to<br>Studying Abroad</h1>
                <p class="gge-mk-hero-desc">
                    We provide a complete admissions services for Australia, Canada, Europe, UK, USA and other countries.
                </p>
                
                <!-- Buttons matching Image 2 exactly -->
                <div class="bttn-bx gge-hero-btn-row">
                    <a href="https://globalgroupofeducationportal.com/partner-registration" class="innr-bnr-bttn colrd-bttn" target="_blank" rel="noopener">
                        <i class="fa fa-user"></i> Be a Partner
                    </a>
                    <a href="https://globalgroupofeducationportal.com/student-registration" class="innr-bnr-bttn trns-bttn" target="_blank" rel="noopener">
                        <i class="fa fa-graduation-cap"></i> Be a Student
                    </a>
                </div>

                <!-- Trust Badges with gold icons -->
                <div class="gge-mk-hero-trust">
                    <div class="gge-mk-trust-item">
                        <i class="fa fa-shield gge-mk-trust-icon"></i>
                        <span>British Council Certified Consultants</span>
                    </div>
                    <div class="gge-mk-trust-item">
                        <i class="fa fa-institution gge-mk-trust-icon"></i>
                        <span>Official Representatives of Top Universities</span>
                    </div>
                    <div class="gge-mk-trust-item">
                        <i class="fa fa-users gge-mk-trust-icon"></i>
                        <span>Trusted by Students Worldwide</span>
                    </div>
                </div>
            </div>
        </div>
    </section>'''

NEW_DEST = '''    <!-- 5. TOP STUDY DESTINATIONS (FULL-WIDTH CONTINUOUS RUNNING LINE / MARQUEE) -->
    <section class="gge-dest-line-section" id="destinations">
        <div class="gge-line-container">
            <div class="gge-line-header">
                <div class="gge-line-header-left">
                    <span class="gge-line-eyebrow">GLOBAL CAMPUSES</span>
                    <h2 class="gge-line-title">Top Study Destinations</h2>
                    <p class="gge-line-subtitle">Explore world-class education and high visa success in your dream country.</p>
                </div>
                <div class="gge-line-header-right">
                    <a href="#destinations" class="gge-line-view-all">View All Destinations &rarr;</a>
                </div>
            </div>

            <!-- Continuous Running Line Viewport -->
            <div class="gge-dest-marquee-viewport" id="ggeDestMarqueeWrap">
                <div class="gge-dest-line-track">
                    <!-- Set 1 -->
                    <a href="/study-in-uk" class="gge-dest-card-item" style="background-image: url('/assets/images/destinations/uk.jpg');">
                        <div class="gge-dest-card-overlay"></div>
                        <span class="gge-dest-card-tag">400+ Universities</span>
                        <div class="gge-dest-card-bottom">
                            <div class="gge-dest-card-info">
                                <span class="gge-dest-card-flag">🇬🇧</span>
                                <strong class="gge-dest-card-name">United Kingdom</strong>
                            </div>
                            <span class="gge-dest-card-arrow"><i class="fa fa-arrow-right"></i></span>
                        </div>
                    </a>

                    <a href="/study-in-europe" class="gge-dest-card-item" style="background-image: url('/assets/images/destinations/europe.jpg');">
                        <div class="gge-dest-card-overlay"></div>
                        <span class="gge-dest-card-tag">Schengen Route</span>
                        <div class="gge-dest-card-bottom">
                            <div class="gge-dest-card-info">
                                <span class="gge-dest-card-flag">🇪🇺</span>
                                <strong class="gge-dest-card-name">Europe</strong>
                            </div>
                            <span class="gge-dest-card-arrow"><i class="fa fa-arrow-right"></i></span>
                        </div>
                    </a>

                    <a href="/study-in-australia" class="gge-dest-card-item" style="background-image: url('/assets/images/destinations/australia.jpg');">
                        <div class="gge-dest-card-overlay"></div>
                        <span class="gge-dest-card-tag">Post-Study Work</span>
                        <div class="gge-dest-card-bottom">
                            <div class="gge-dest-card-info">
                                <span class="gge-dest-card-flag">🇦🇺</span>
                                <strong class="gge-dest-card-name">Australia</strong>
                            </div>
                            <span class="gge-dest-card-arrow"><i class="fa fa-arrow-right"></i></span>
                        </div>
                    </a>

                    <a href="/study-in-canada" class="gge-dest-card-item" style="background-image: url('/assets/images/destinations/canada.jpg');">
                        <div class="gge-dest-card-overlay"></div>
                        <span class="gge-dest-card-tag">PGWP &amp; PR Route</span>
                        <div class="gge-dest-card-bottom">
                            <div class="gge-dest-card-info">
                                <span class="gge-dest-card-flag">🇨🇦</span>
                                <strong class="gge-dest-card-name">Canada</strong>
                            </div>
                            <span class="gge-dest-card-arrow"><i class="fa fa-arrow-right"></i></span>
                        </div>
                    </a>

                    <a href="/study-in-new-zealand" class="gge-dest-card-item" style="background-image: url('/assets/images/destinations/newzealand.jpg');">
                        <div class="gge-dest-card-overlay"></div>
                        <span class="gge-dest-card-tag">High Visa Ratio</span>
                        <div class="gge-dest-card-bottom">
                            <div class="gge-dest-card-info">
                                <span class="gge-dest-card-flag">🇳🇿</span>
                                <strong class="gge-dest-card-name">New Zealand</strong>
                            </div>
                            <span class="gge-dest-card-arrow"><i class="fa fa-arrow-right"></i></span>
                        </div>
                    </a>

                    <a href="/study-in-usa" class="gge-dest-card-item" style="background-image: url('/assets/images/destinations/usa.jpg');">
                        <div class="gge-dest-card-overlay"></div>
                        <span class="gge-dest-card-tag">Ivy &amp; STEM Optics</span>
                        <div class="gge-dest-card-bottom">
                            <div class="gge-dest-card-info">
                                <span class="gge-dest-card-flag">🇺🇸</span>
                                <strong class="gge-dest-card-name">United States</strong>
                            </div>
                            <span class="gge-dest-card-arrow"><i class="fa fa-arrow-right"></i></span>
                        </div>
                    </a>

                    <a href="#destinations" class="gge-dest-card-item gge-dest-card-more">
                        <div class="gge-dest-more-content">
                            <div class="gge-dest-more-icon-wrap"><i class="fa fa-globe"></i></div>
                            <strong>Explore All 10+ Destinations</strong>
                            <span>View All Countries &rarr;</span>
                        </div>
                    </a>

                    <!-- Set 2 (Duplicate for continuous infinite marquee loop) -->
                    <a href="/study-in-uk" class="gge-dest-card-item" style="background-image: url('/assets/images/destinations/uk.jpg');">
                        <div class="gge-dest-card-overlay"></div>
                        <span class="gge-dest-card-tag">400+ Universities</span>
                        <div class="gge-dest-card-bottom">
                            <div class="gge-dest-card-info">
                                <span class="gge-dest-card-flag">🇬🇧</span>
                                <strong class="gge-dest-card-name">United Kingdom</strong>
                            </div>
                            <span class="gge-dest-card-arrow"><i class="fa fa-arrow-right"></i></span>
                        </div>
                    </a>

                    <a href="/study-in-europe" class="gge-dest-card-item" style="background-image: url('/assets/images/destinations/europe.jpg');">
                        <div class="gge-dest-card-overlay"></div>
                        <span class="gge-dest-card-tag">Schengen Route</span>
                        <div class="gge-dest-card-bottom">
                            <div class="gge-dest-card-info">
                                <span class="gge-dest-card-flag">🇪🇺</span>
                                <strong class="gge-dest-card-name">Europe</strong>
                            </div>
                            <span class="gge-dest-card-arrow"><i class="fa fa-arrow-right"></i></span>
                        </div>
                    </a>

                    <a href="/study-in-australia" class="gge-dest-card-item" style="background-image: url('/assets/images/destinations/australia.jpg');">
                        <div class="gge-dest-card-overlay"></div>
                        <span class="gge-dest-card-tag">Post-Study Work</span>
                        <div class="gge-dest-card-bottom">
                            <div class="gge-dest-card-info">
                                <span class="gge-dest-card-flag">🇦🇺</span>
                                <strong class="gge-dest-card-name">Australia</strong>
                            </div>
                            <span class="gge-dest-card-arrow"><i class="fa fa-arrow-right"></i></span>
                        </div>
                    </a>

                    <a href="/study-in-canada" class="gge-dest-card-item" style="background-image: url('/assets/images/destinations/canada.jpg');">
                        <div class="gge-dest-card-overlay"></div>
                        <span class="gge-dest-card-tag">PGWP &amp; PR Route</span>
                        <div class="gge-dest-card-bottom">
                            <div class="gge-dest-card-info">
                                <span class="gge-dest-card-flag">🇨🇦</span>
                                <strong class="gge-dest-card-name">Canada</strong>
                            </div>
                            <span class="gge-dest-card-arrow"><i class="fa fa-arrow-right"></i></span>
                        </div>
                    </a>

                    <a href="/study-in-new-zealand" class="gge-dest-card-item" style="background-image: url('/assets/images/destinations/newzealand.jpg');">
                        <div class="gge-dest-card-overlay"></div>
                        <span class="gge-dest-card-tag">High Visa Ratio</span>
                        <div class="gge-dest-card-bottom">
                            <div class="gge-dest-card-info">
                                <span class="gge-dest-card-flag">🇳🇿</span>
                                <strong class="gge-dest-card-name">New Zealand</strong>
                            </div>
                            <span class="gge-dest-card-arrow"><i class="fa fa-arrow-right"></i></span>
                        </div>
                    </a>

                    <a href="/study-in-usa" class="gge-dest-card-item" style="background-image: url('/assets/images/destinations/usa.jpg');">
                        <div class="gge-dest-card-overlay"></div>
                        <span class="gge-dest-card-tag">Ivy &amp; STEM Optics</span>
                        <div class="gge-dest-card-bottom">
                            <div class="gge-dest-card-info">
                                <span class="gge-dest-card-flag">🇺🇸</span>
                                <strong class="gge-dest-card-name">United States</strong>
                            </div>
                            <span class="gge-dest-card-arrow"><i class="fa fa-arrow-right"></i></span>
                        </div>
                    </a>

                    <a href="#destinations" class="gge-dest-card-item gge-dest-card-more">
                        <div class="gge-dest-more-content">
                            <div class="gge-dest-more-icon-wrap"><i class="fa fa-globe"></i></div>
                            <strong>Explore All 10+ Destinations</strong>
                            <span>View All Countries &rarr;</span>
                        </div>
                    </a>
                </div>
            </div>
        </div>
    </section>'''

files = ['index.html', 'public/index.html', 'public/pages/home.html', 'public/pages/index.html']

for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Replace Hero section in Mockup
    hero_pattern = re.compile(
        r'<!-- 2\. HERO SECTION WITH BACKGROUND VIDEO & COMPACT CONSULTATION CARD -->.*?<!-- 3\. FLOATING FEATURES PILL BAR -->',
        re.DOTALL
    )
    if hero_pattern.search(content):
        content = hero_pattern.sub(NEW_HERO + '\n\n    <!-- 3. FLOATING FEATURES PILL BAR -->', content)
        print(f"[{fpath}] Successfully replaced Hero Section!")
    else:
        print(f"[{fpath}] Hero pattern not matched, attempting looser pattern...")
        hero_pattern2 = re.compile(
            r'<section class="gge-mk-hero-section">.*?</section>\s*(<!-- 3\. FLOATING FEATURES PILL BAR -->)',
            re.DOTALL
        )
        if hero_pattern2.search(content):
            content = hero_pattern2.sub(NEW_HERO + '\n\n    \\1', content)
            print(f"[{fpath}] Looser Hero pattern matched!")
        else:
            print(f"[{fpath}] ERROR: Hero pattern failed to match!")

    # 2. Replace Destinations section
    dest_pattern = re.compile(
        r'<!-- 5\. TOP STUDY DESTINATIONS.*?<!-- 6\. WORLD-CLASS UNIVERSITIES',
        re.DOTALL
    )
    if dest_pattern.search(content):
        content = dest_pattern.sub(NEW_DEST + '\n\n    <!-- 6. WORLD-CLASS UNIVERSITIES', content)
        print(f"[{fpath}] Successfully replaced Destinations Section with Continuous Line Marquee!")
    else:
        print(f"[{fpath}] Destinations pattern not matched, checking looser...")
        dest_pattern2 = re.compile(
            r'<section class="gge-dest-line-section" id="destinations">.*?</section>\s*(<!-- 6\. WORLD-CLASS UNIVERSITIES)',
            re.DOTALL
        )
        if dest_pattern2.search(content):
            content = dest_pattern2.sub(NEW_DEST + '\n\n    \\1', content)
            print(f"[{fpath}] Looser Destinations pattern matched!")
        else:
            print(f"[{fpath}] ERROR: Destinations pattern failed to match!")

    # 3. Update Classic Video hero to crm_video.mp4
    content = content.replace(
        '<source src="/assets/videos/hero-video.mp4" type="video/mp4"/>',
        '<source src="/assets/videos/crm_video.mp4" type="video/mp4"/><source src="https://globalgroupofeducationportal.com/images/video.mp4" type="video/mp4"/>'
    )
    content = content.replace(
        '<source src="/assets/videos/hero-video.mp4" type="video/mp4">',
        '<source src="/assets/videos/crm_video.mp4" type="video/mp4"><source src="https://globalgroupofeducationportal.com/images/video.mp4" type="video/mp4">'
    )

    # 4. In Classic view, update buttons to Image 2 style
    content = re.sub(
        r'<div class="gge-video-actions">.*?</div>',
        '''<div class="gge-video-actions bttn-bx">
<a class="innr-bnr-bttn colrd-bttn" href="https://globalgroupofeducationportal.com/partner-registration" target="_blank" rel="noopener">
<i class="fa fa-user"></i> Be a Partner
</a>
<a class="innr-bnr-bttn trns-bttn" href="https://globalgroupofeducationportal.com/student-registration" target="_blank" rel="noopener">
<i class="fa fa-graduation-cap"></i> Be a Student
</a>
</div>''',
        content,
        flags=re.DOTALL
    )

    # 5. Remove slide2 and slide3 from banner-slider if present
    content = re.sub(
        r'<div class="slide2">.*?<div class="slide3">.*?</div>\s*</div>\s*</div>',
        '',
        content,
        flags=re.DOTALL
    )

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"[{fpath}] Written successfully!")

print("All HTML files updated successfully!")
