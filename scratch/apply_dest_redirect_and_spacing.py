import os
import re

html_files = [
    'index.html',
    'public/index.html',
    'public/pages/home.html',
    'public/pages/index.html'
]

# 1. New Study Destinations section HTML with UK, USA, Canada, Australia, Hungary, UAE, Europe, New Zealand
destinations_html = '''    <!-- 5. TOP STUDY DESTINATIONS (FULL-WIDTH CONTINUOUS RUNNING LINE / MARQUEE - ALTERNATIVE DIRECTION) -->
    <section class="gge-dest-line-section" id="destinations">
        <div class="gge-line-header-container">
            <div class="gge-line-header-left">
                <span class="gge-line-badge"><i class="fa fa-plane"></i> Global Gateways</span>
                <h2 class="gge-line-title">Top Study Destinations</h2>
                <p class="gge-line-subtitle">Explore world-leading study destinations with direct university pathways, scholarships, and post-study work rights.</p>
            </div>
            <div class="gge-line-header-right">
                <a href="https://www.globalgroupofeducation.com/study-in-uk" class="gge-line-view-all">View All Destinations &rarr;</a>
            </div>
        </div>

        <div class="gge-dest-line-viewport">
            <div class="gge-dest-line-track">
                <!-- SET 1 -->
                <div class="gge-dest-track-set">
                    <a href="https://www.globalgroupofeducation.com/study-in-uk" class="gge-dest-card-item" style="background-image: url('/assets/images/destinations/uk.jpg');">
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

                    <a href="https://www.globalgroupofeducation.com/study-in-usa" class="gge-dest-card-item" style="background-image: url('/assets/images/destinations/usa.jpg');">
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

                    <a href="https://www.globalgroupofeducation.com/study-in-canada" class="gge-dest-card-item" style="background-image: url('/assets/images/destinations/canada.jpg');">
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

                    <a href="https://www.globalgroupofeducation.com/study-in-australia" class="gge-dest-card-item" style="background-image: url('/assets/images/destinations/australia.jpg');">
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

                    <a href="https://www.globalgroupofeducation.com/study-in-hungary" class="gge-dest-card-item" style="background-image: url('/assets/images/destinations/hungary.jpg');">
                        <div class="gge-dest-card-overlay"></div>
                        <span class="gge-dest-card-tag">Affordable Tuition</span>
                        <div class="gge-dest-card-bottom">
                            <div class="gge-dest-card-info">
                                <span class="gge-dest-card-flag">🇭🇺</span>
                                <strong class="gge-dest-card-name">Hungary</strong>
                            </div>
                            <span class="gge-dest-card-arrow"><i class="fa fa-arrow-right"></i></span>
                        </div>
                    </a>

                    <a href="https://www.globalgroupofeducation.com/study-in-uae" class="gge-dest-card-item" style="background-image: url('/assets/images/destinations/uae.jpg');">
                        <div class="gge-dest-card-overlay"></div>
                        <span class="gge-dest-card-tag">Global Hub</span>
                        <div class="gge-dest-card-bottom">
                            <div class="gge-dest-card-info">
                                <span class="gge-dest-card-flag">🇦🇪</span>
                                <strong class="gge-dest-card-name">UAE (Dubai)</strong>
                            </div>
                            <span class="gge-dest-card-arrow"><i class="fa fa-arrow-right"></i></span>
                        </div>
                    </a>

                    <a href="https://www.globalgroupofeducation.com/study-in-europe" class="gge-dest-card-item" style="background-image: url('/assets/images/destinations/europe.jpg');">
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

                    <a href="https://www.globalgroupofeducation.com/study-in-new-zealand" class="gge-dest-card-item" style="background-image: url('/assets/images/destinations/newzealand.jpg');">
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
                </div>

                <!-- SET 2 -->
                <div class="gge-dest-track-set" aria-hidden="true">
                    <a href="https://www.globalgroupofeducation.com/study-in-uk" class="gge-dest-card-item" style="background-image: url('/assets/images/destinations/uk.jpg');">
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

                    <a href="https://www.globalgroupofeducation.com/study-in-usa" class="gge-dest-card-item" style="background-image: url('/assets/images/destinations/usa.jpg');">
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

                    <a href="https://www.globalgroupofeducation.com/study-in-canada" class="gge-dest-card-item" style="background-image: url('/assets/images/destinations/canada.jpg');">
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

                    <a href="https://www.globalgroupofeducation.com/study-in-australia" class="gge-dest-card-item" style="background-image: url('/assets/images/destinations/australia.jpg');">
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

                    <a href="https://www.globalgroupofeducation.com/study-in-hungary" class="gge-dest-card-item" style="background-image: url('/assets/images/destinations/hungary.jpg');">
                        <div class="gge-dest-card-overlay"></div>
                        <span class="gge-dest-card-tag">Affordable Tuition</span>
                        <div class="gge-dest-card-bottom">
                            <div class="gge-dest-card-info">
                                <span class="gge-dest-card-flag">🇭🇺</span>
                                <strong class="gge-dest-card-name">Hungary</strong>
                            </div>
                            <span class="gge-dest-card-arrow"><i class="fa fa-arrow-right"></i></span>
                        </div>
                    </a>

                    <a href="https://www.globalgroupofeducation.com/study-in-uae" class="gge-dest-card-item" style="background-image: url('/assets/images/destinations/uae.jpg');">
                        <div class="gge-dest-card-overlay"></div>
                        <span class="gge-dest-card-tag">Global Hub</span>
                        <div class="gge-dest-card-bottom">
                            <div class="gge-dest-card-info">
                                <span class="gge-dest-card-flag">🇦🇪</span>
                                <strong class="gge-dest-card-name">UAE (Dubai)</strong>
                            </div>
                            <span class="gge-dest-card-arrow"><i class="fa fa-arrow-right"></i></span>
                        </div>
                    </a>

                    <a href="https://www.globalgroupofeducation.com/study-in-europe" class="gge-dest-card-item" style="background-image: url('/assets/images/destinations/europe.jpg');">
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

                    <a href="https://www.globalgroupofeducation.com/study-in-new-zealand" class="gge-dest-card-item" style="background-image: url('/assets/images/destinations/newzealand.jpg');">
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
                </div>
            </div>
        </div>
    </section>'''

# Updated Navbar Dropdown for Study Destinations
navbar_dest_html = '''                    <li class="gge-mk-nav-item gge-has-dropdown">
                        <a href="javascript:void(0)" class="gge-mk-nav-link gge-nav-dropdown-toggle" role="button" aria-haspopup="true" aria-expanded="false"><i class="fa fa-globe"></i> Study Destinations <i class="fa fa-angle-down"></i></a>
                        <ul class="gge-mk-nav-dropdown">
                            <li><a href="https://www.globalgroupofeducation.com/study-in-uk"><i class="fa fa-flag"></i> Study in UK</a></li>
                            <li><a href="https://www.globalgroupofeducation.com/study-in-usa"><i class="fa fa-flag"></i> Study in USA</a></li>
                            <li><a href="https://www.globalgroupofeducation.com/study-in-canada"><i class="fa fa-flag"></i> Study in Canada</a></li>
                            <li><a href="https://www.globalgroupofeducation.com/study-in-australia"><i class="fa fa-flag"></i> Study in Australia</a></li>
                            <li><a href="https://www.globalgroupofeducation.com/study-in-hungary"><i class="fa fa-flag"></i> Study in Hungary</a></li>
                            <li><a href="https://www.globalgroupofeducation.com/study-in-uae"><i class="fa fa-flag"></i> Study in UAE</a></li>
                            <li><a href="https://www.globalgroupofeducation.com/study-in-europe"><i class="fa fa-flag"></i> Study in Europe</a></li>
                            <li><a href="https://www.globalgroupofeducation.com/study-in-new-zealand"><i class="fa fa-flag"></i> Study in New Zealand</a></li>
                        </ul>
                    </li>'''

# Updated Mobile Drawer for Study Destinations
drawer_dest_html = '''                <a href="javascript:void(0)" class="gge-drawer-sub-toggle"><i class="fa fa-globe"></i> Study Destinations <i class="fa fa-angle-down"></i></a>
                <ul class="gge-drawer-sub">
                    <li><a href="https://www.globalgroupofeducation.com/study-in-uk">&bull; Study in UK</a></li>
                    <li><a href="https://www.globalgroupofeducation.com/study-in-usa">&bull; Study in USA</a></li>
                    <li><a href="https://www.globalgroupofeducation.com/study-in-canada">&bull; Study in Canada</a></li>
                    <li><a href="https://www.globalgroupofeducation.com/study-in-australia">&bull; Study in Australia</a></li>
                    <li><a href="https://www.globalgroupofeducation.com/study-in-hungary">&bull; Study in Hungary</a></li>
                    <li><a href="https://www.globalgroupofeducation.com/study-in-uae">&bull; Study in UAE</a></li>
                    <li><a href="https://www.globalgroupofeducation.com/study-in-europe">&bull; Study in Europe</a></li>
                    <li><a href="https://www.globalgroupofeducation.com/study-in-new-zealand">&bull; Study in New Zealand</a></li>
                </ul>'''

# Updated click redirect JS
direct_redirect_js = '''
    // Direct redirect for all course cards, destination cards, and dropdown links
    var directActionLinks = document.querySelectorAll('.gge-mk-nav-dropdown a, .gge-course-card, .gge-line-view-all, .gge-dest-card-item, .gge-drawer-sub a');
    directActionLinks.forEach(function(el) {
        el.addEventListener('click', function(e) {
            var targetUrl = this.getAttribute('href');
            if (targetUrl && targetUrl !== '#' && !targetUrl.startsWith('javascript:')) {
                e.preventDefault();
                window.location.href = targetUrl;
            }
        });
    });
'''

for fpath in html_files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Replace Destinations Section
        content = re.sub(
            r'<!-- 5\. TOP STUDY DESTINATIONS.*?<section class="gge-dest-line-section".*?</section>',
            destinations_html,
            content,
            flags=re.DOTALL
        )

        # Replace Navbar Study Destinations
        content = re.sub(
            r'<li class="gge-mk-nav-item gge-has-dropdown">\s*<a href="javascript:void\(0\)" class="gge-mk-nav-link gge-nav-dropdown-toggle"[^>]*>.*?Study Destinations.*?</ul>\s*</li>',
            navbar_dest_html,
            content,
            flags=re.DOTALL
        )

        # Replace Drawer Study Destinations
        content = re.sub(
            r'<a href="#destinations" class="gge-drawer-sub-toggle">.*?Study Destinations.*?</ul>',
            drawer_dest_html,
            content,
            flags=re.DOTALL
        )
        content = re.sub(
            r'<a href="javascript:void\(0\)" class="gge-drawer-sub-toggle">.*?Study Destinations.*?</ul>',
            drawer_dest_html,
            content,
            flags=re.DOTALL
        )

        # Update redirect script
        content = re.sub(
            r'// Direct redirect for all course cards.*?window\.location\.href = targetUrl;\s*\}\s*\}\);\s*\}\);',
            direct_redirect_js.strip(),
            content,
            flags=re.DOTALL
        )

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated HTML in {fpath}")

# 2. Update CSS in assets/css/custom.css and public/assets/css/custom.css
css_files = [
    'assets/css/custom.css',
    'public/assets/css/custom.css'
]

spacing_and_direction_css = '''
/* ========================================================================== */
/* TOP STUDY DESTINATIONS ALTERNATIVE DIRECTION (LEFT TO RIGHT MARQUEE)       */
/* ========================================================================== */
.gge-dest-line-track {
    display: flex !important;
    gap: 20px !important;
    width: max-content !important;
    animation: ggeDestLineMarqueeAlt 40s linear infinite !important;
}

.gge-dest-line-track:hover {
    animation-play-state: paused !important;
}

@keyframes ggeDestLineMarqueeAlt {
    0% { transform: translateX(-50%); }
    100% { transform: translateX(0); }
}

/* ========================================================================== */
/* ACADEMIC COURSES CARDS / TABS SPACING FIX (GENEROUS PADDING & GAPS)        */
/* ========================================================================== */
.gge-courses-section {
    padding: 90px 0 100px 0 !important;
}
.gge-courses-grid {
    display: grid !important;
    grid-template-columns: repeat(3, 1fr) !important;
    gap: 36px 32px !important;
    margin-top: 35px !important;
}
.gge-course-card {
    background: #ffffff !important;
    border: 1.5px solid #e2e8f0 !important;
    border-radius: 20px !important;
    padding: 34px 30px !important;
    display: flex !important;
    flex-direction: column !important;
    justify-content: space-between !important;
    text-decoration: none !important;
    box-shadow: 0 8px 24px rgba(13, 37, 82, 0.06) !important;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    position: relative !important;
    min-height: 260px !important;
}
.gge-course-card:hover {
    transform: translateY(-6px) !important;
    border-color: #eca411 !important;
    box-shadow: 0 16px 36px rgba(16, 39, 113, 0.12) !important;
    text-decoration: none !important;
}
.gge-course-icon-wrap {
    width: 52px !important;
    height: 52px !important;
    border-radius: 12px !important;
    background: #0f245c !important;
    color: #eca411 !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    font-size: 22px !important;
    margin-bottom: 22px !important;
}
.gge-course-card-title {
    font-size: 20px !important;
    font-weight: 800 !important;
    color: #0c1226 !important;
    margin-bottom: 14px !important;
    text-transform: uppercase !important;
    letter-spacing: 0.3px !important;
    line-height: 1.3 !important;
}
.gge-course-card-desc {
    font-size: 14.5px !important;
    line-height: 24px !important;
    color: #64748b !important;
    margin-bottom: 22px !important;
    flex-grow: 1 !important;
}
.gge-course-card-link {
    font-size: 14.5px !important;
    font-weight: 700 !important;
    color: #0f245c !important;
    display: inline-flex !important;
    align-items: center !important;
    gap: 8px !important;
    transition: color 0.2s ease, transform 0.2s ease !important;
}
.gge-course-card:hover .gge-course-card-link {
    color: #eca411 !important;
    transform: translateX(4px) !important;
}

@media (max-width: 991px) {
    .gge-courses-grid {
        grid-template-columns: repeat(2, 1fr) !important;
        gap: 28px !important;
    }
}
@media (max-width: 600px) {
    .gge-courses-grid {
        grid-template-columns: 1fr !important;
        gap: 24px !important;
    }
    .gge-course-card {
        padding: 26px 22px !important;
    }
}
'''

for csspath in css_files:
    if os.path.exists(csspath):
        with open(csspath, 'r', encoding='utf-8') as f:
            css_content = f.read()
        css_content += spacing_and_direction_css
        with open(csspath, 'w', encoding='utf-8') as f:
            f.write(css_content)
        print(f"Appended spacing_and_direction_css to {csspath}")

print("All updates applied successfully.")
