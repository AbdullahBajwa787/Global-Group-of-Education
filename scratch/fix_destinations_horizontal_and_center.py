import os
import re

html_files = [
    'index.html',
    'public/index.html',
    'public/pages/home.html',
    'public/pages/index.html'
]

# Clean Horizontal Destinations Section with direct cards, centered header
clean_destinations_section = '''    <!-- 5. TOP STUDY DESTINATIONS (FULL-WIDTH CONTINUOUS RUNNING LINE / MARQUEE - HORIZONTAL ALTERNATIVE DIRECTION) -->
    <section class="gge-dest-line-section" id="destinations">
        <div class="gge-line-header-container">
            <span class="gge-line-badge"><i class="fa fa-plane"></i> Global Gateways</span>
            <h2 class="gge-line-title">Top Study Destinations</h2>
            <p class="gge-line-subtitle">Explore world-leading study destinations with direct university pathways, scholarships, and post-study work rights.</p>
            <a href="https://www.globalgroupofeducation.com/study-in-uk" class="gge-line-view-all">View All Destinations &rarr;</a>
        </div>

        <div class="gge-dest-line-viewport">
            <div class="gge-dest-line-track">
                <!-- Set 1 (8 countries) -->
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

                <!-- Set 2 (Duplicate 8 countries for seamless infinite loop) -->
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
    </section>'''

# Centered Universities Header
universities_header = '''    <!-- 6. POPULAR UNIVERSITIES (WORLD-CLASS CONTINUOUS RUNNING LINE / MARQUEE) -->
    <section class="gge-uni-line-section" id="universities">
        <div class="gge-line-header-container">
            <span class="gge-line-badge"><i class="fa fa-university"></i> Global Institutions</span>
            <h2 class="gge-line-title">World-Class Universities</h2>
            <p class="gge-line-subtitle">Direct partnership access to accredited degree, master's &amp; pathway programs across the globe.</p>
            <a href="https://www.globalgroupofeducation.com/all-universities" target="_blank" class="gge-line-view-all">View All Universities &rarr;</a>
        </div>'''

# Centered Courses Header
courses_header = '''    <!-- 8. EXPLORE ACADEMIC COURSES SECTION -->
    <section class="gge-courses-section" id="courses">
        <div class="container-fluid" style="max-width: 1320px; margin: 0 auto; padding: 0 20px;">
            <div class="gge-line-header-container">
                <span class="gge-line-badge"><i class="fa fa-book"></i> Academic Programs</span>
                <h2 class="gge-line-title">Explore Academic Courses</h2>
                <p class="gge-line-subtitle">Find accredited undergraduate, postgraduate, doctorate &amp; language programs at leading global universities.</p>
                <a href="https://www.globalgroupofeducation.com/undergraduate-courses" class="gge-line-view-all">View All Courses &rarr;</a>
            </div>'''

for fpath in html_files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        # 1. Replace Destinations section
        content = re.sub(
            r'<!-- 5\. TOP STUDY DESTINATIONS.*?<section class="gge-dest-line-section".*?</section>',
            clean_destinations_section,
            content,
            flags=re.DOTALL
        )

        # 2. Replace Universities header
        content = re.sub(
            r'<!-- 6\. POPULAR UNIVERSITIES.*?<section class="gge-uni-line-section".*?<div class="gge-line-header-container">.*?</div>\s*</div>',
            universities_header,
            content,
            flags=re.DOTALL
        )
        content = re.sub(
            r'<!-- 6\. POPULAR UNIVERSITIES.*?<section class="gge-uni-line-section".*?<div class="gge-line-header-container">.*?</div>',
            universities_header,
            content,
            flags=re.DOTALL
        )

        # 3. Replace Courses header
        content = re.sub(
            r'<!-- 8\. EXPLORE ACADEMIC COURSES SECTION -->\s*<section class="gge-courses-section"[^>]*>.*?<div class="gge-line-header-container">.*?</div>',
            courses_header,
            content,
            flags=re.DOTALL
        )

        # 4. Anti-glitch scroll restoration script
        scroll_fix_code = '''
    // Anti-scroll-glitch on refresh
    if ('scrollRestoration' in history) {
        history.scrollRestoration = 'manual';
    }
'''
        if 'Anti-scroll-glitch' not in content:
            content = content.replace(
                'document.addEventListener(\'DOMContentLoaded\', function() {',
                scroll_fix_code + 'document.addEventListener(\'DOMContentLoaded\', function() {'
            )

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated HTML in {fpath}")

# 5. Overwrite/Append CSS for perfect centering and horizontal marquee
css_additions = '''
/* ========================================================================== */
/* CENTERED HEADERS FOR ALL SECTIONS (TOP DESTINATIONS, UNIS, COURSES, STATS) */
/* ========================================================================== */
.gge-line-header-container {
    text-align: center !important;
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    justify-content: center !important;
    max-width: 820px !important;
    margin: 0 auto 35px auto !important;
    padding: 0 20px !important;
    float: none !important;
}

.gge-line-badge {
    margin: 0 auto 12px auto !important;
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    gap: 8px !important;
}

.gge-line-title {
    text-align: center !important;
    font-size: 36px !important;
    font-weight: 800 !important;
    color: #0c1226 !important;
    margin: 0 auto 12px auto !important;
    width: 100% !important;
    letter-spacing: -0.5px !important;
}

.gge-line-subtitle {
    text-align: center !important;
    font-size: 16px !important;
    line-height: 26px !important;
    color: #64748b !important;
    margin: 0 auto 20px auto !important;
    max-width: 680px !important;
    width: 100% !important;
}

.gge-line-view-all {
    margin: 0 auto !important;
    display: inline-flex !important;
}

/* ========================================================================== */
/* STRICTLY HORIZONTAL TOP STUDY DESTINATIONS RUNNING LINE (ALTERNATIVE REVERSE) */
/* ========================================================================== */
.gge-dest-line-section {
    padding: 60px 0 !important;
    background: #ffffff !important;
    overflow: hidden !important;
    position: relative !important;
}

.gge-dest-line-viewport {
    width: 100% !important;
    overflow: hidden !important;
    position: relative !important;
    padding: 15px 0 !important;
    mask-image: linear-gradient(to right, transparent 0%, black 5%, black 95%, transparent 100%) !important;
    -webkit-mask-image: linear-gradient(to right, transparent 0%, black 5%, black 95%, transparent 100%) !important;
}

.gge-dest-line-track {
    display: flex !important;
    flex-direction: row !important;
    flex-wrap: nowrap !important;
    align-items: center !important;
    gap: 20px !important;
    width: max-content !important;
    animation: ggeDestMarqueeAlt 40s linear infinite !important;
    -webkit-backface-visibility: hidden !important;
    backface-visibility: hidden !important;
    transform: translate3d(0, 0, 0) !important;
    will-change: transform !important;
}

.gge-dest-line-track:hover {
    animation-play-state: paused !important;
}

@keyframes ggeDestMarqueeAlt {
    0% {
        transform: translate3d(-50%, 0, 0);
    }
    100% {
        transform: translate3d(0, 0, 0);
    }
}

.gge-dest-card-item {
    flex: 0 0 250px !important;
    width: 250px !important;
    height: 175px !important;
    border-radius: 18px !important;
    background-size: cover !important;
    background-position: center !important;
    position: relative !important;
    overflow: hidden !important;
    display: inline-flex !important;
    flex-direction: column !important;
    justify-content: space-between !important;
    padding: 16px !important;
    text-decoration: none !important;
    box-shadow: 0 6px 18px rgba(0, 0, 0, 0.15) !important;
    transition: transform 0.3s ease, box-shadow 0.3s ease !important;
    box-sizing: border-box !important;
    flex-shrink: 0 !important;
}

.gge-dest-card-item:hover {
    transform: translateY(-5px) !important;
    box-shadow: 0 14px 28px rgba(0, 0, 0, 0.25) !important;
    text-decoration: none !important;
}

/* UNIVERSITIES MARQUEE REINFORCEMENT (SMOOTH FORWARD DIRECTION) */
.gge-uni-line-section {
    padding: 60px 0 !important;
    background: linear-gradient(180deg, #f8fafc 0%, #ffffff 100%) !important;
    overflow: hidden !important;
}

.gge-uni-marquee-track {
    display: flex !important;
    flex-direction: row !important;
    flex-wrap: nowrap !important;
    gap: 20px !important;
    width: max-content !important;
    animation: ggeUniLineMarquee 34s linear infinite !important;
    -webkit-backface-visibility: hidden !important;
    backface-visibility: hidden !important;
    transform: translate3d(0, 0, 0) !important;
    will-change: transform !important;
}

.gge-uni-marquee-track:hover {
    animation-play-state: paused !important;
}

@keyframes ggeUniLineMarquee {
    0% {
        transform: translate3d(0, 0, 0);
    }
    100% {
        transform: translate3d(-50%, 0, 0);
    }
}

/* ========================================================================== */
/* SMOOTH GPU SCROLL & ANTI-GLITCH REFRESH                                    */
/* ========================================================================== */
html {
    scroll-behavior: smooth !important;
    overflow-x: hidden !important;
}
body {
    overflow-x: hidden !important;
    width: 100% !important;
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
        css_content += css_additions
        with open(csspath, 'w', encoding='utf-8') as f:
            f.write(css_content)
        print(f"Appended centering & horizontal CSS to {csspath}")

print("Done.")
