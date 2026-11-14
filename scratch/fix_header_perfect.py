import os
import re

files = [
    'index.html',
    'public/index.html',
    'public/pages/home.html',
    'public/pages/index.html'
]

correct_header = '''    <!-- 1. CURVED WHITE HEADER -->
    <header class="gge-mk-header-wrap">
        <div class="gge-mk-header">
            <a href="/" class="gge-mk-logo-link">
                <img src="/assets/images/round-logo.png" alt="Global Group of Education" class="gge-mk-logo-img">
            </a>
            
            <nav>
                <ul class="gge-mk-nav">
                    <li class="gge-mk-nav-item">
                        <a href="/" class="gge-mk-nav-link active"><i class="fa fa-home"></i> Home</a>
                    </li>
                    <li class="gge-mk-nav-item gge-has-dropdown">
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
                    </li>
                    <li class="gge-mk-nav-item gge-has-dropdown">
                        <a href="javascript:void(0)" class="gge-mk-nav-link gge-nav-dropdown-toggle" role="button" aria-haspopup="true" aria-expanded="false"><i class="fa fa-graduation-cap"></i> Courses <i class="fa fa-angle-down"></i></a>
                        <ul class="gge-mk-nav-dropdown">
                            <li><a href="https://www.globalgroupofeducation.com/doctorate-courses"><i class="fa fa-certificate"></i> Doctorate Courses</a></li>
                            <li><a href="https://www.globalgroupofeducation.com/postgraduate-courses"><i class="fa fa-graduation-cap"></i> Postgraduate Courses</a></li>
                            <li><a href="https://www.globalgroupofeducation.com/undergraduate-courses"><i class="fa fa-book"></i> Undergraduate Courses</a></li>
                            <li><a href="https://www.globalgroupofeducation.com/pre-master-courses"><i class="fa fa-university"></i> Pre-Master Courses</a></li>
                            <li><a href="https://www.globalgroupofeducation.com/foundation-courses"><i class="fa fa-cubes"></i> Foundation Courses</a></li>
                            <li><a href="https://www.globalgroupofeducation.com/english-language-courses"><i class="fa fa-language"></i> English Language Courses</a></li>
                        </ul>
                    </li>
                    <li class="gge-mk-nav-item">
                        <a href="#services" class="gge-mk-nav-link"><i class="fa fa-briefcase"></i> Our Services</a>
                    </li>
                    <li class="gge-mk-nav-item">
                        <a href="#about" class="gge-mk-nav-link"><i class="fa fa-institution"></i> About Us</a>
                    </li>
                    <li class="gge-mk-nav-item">
                        <a href="/contact-us" class="gge-mk-nav-link"><i class="fa fa-phone"></i> Contact Us</a>
                    </li>
                </ul>
            </nav>

            <div class="gge-mk-header-actions">
                <a href="https://wa.me/447586589659" target="_blank" rel="noopener" class="gge-mk-whatsapp-btn">
                    <i class="fa fa-whatsapp"></i> +44 7586589659
                </a>
                <a href="https://globalgroupofeducationportal.com/" target="_blank" rel="noopener" class="gge-mk-login-btn">
                    <i class="fa fa-user"></i> Login
                </a>
                <button type="button" class="gge-mobile-menu-toggle" id="ggeMobileMenuToggle" aria-label="Toggle Navigation">
                    <i class="fa fa-bars"></i>
                </button>
            </div>
        </div>
    </header>

    <!-- Mobile Drawer Navigation -->
    <div class="gge-mobile-drawer" id="ggeMobileDrawer">
        <div class="gge-drawer-header">
            <img src="/assets/images/round-logo.png" alt="GGE Logo" style="height: 48px;">
            <button type="button" class="gge-drawer-close" id="ggeDrawerClose">&times;</button>
        </div>
        <ul class="gge-drawer-nav">
            <li><a href="/"><i class="fa fa-home"></i> Home</a></li>
            <li class="gge-drawer-has-sub">
                <a href="javascript:void(0)" class="gge-drawer-sub-toggle"><i class="fa fa-globe"></i> Study Destinations <i class="fa fa-angle-down"></i></a>
                <ul class="gge-drawer-sub">
                    <li><a href="https://www.globalgroupofeducation.com/study-in-uk">&bull; Study in UK</a></li>
                    <li><a href="https://www.globalgroupofeducation.com/study-in-usa">&bull; Study in USA</a></li>
                    <li><a href="https://www.globalgroupofeducation.com/study-in-canada">&bull; Study in Canada</a></li>
                    <li><a href="https://www.globalgroupofeducation.com/study-in-australia">&bull; Study in Australia</a></li>
                    <li><a href="https://www.globalgroupofeducation.com/study-in-hungary">&bull; Study in Hungary</a></li>
                    <li><a href="https://www.globalgroupofeducation.com/study-in-uae">&bull; Study in UAE</a></li>
                    <li><a href="https://www.globalgroupofeducation.com/study-in-europe">&bull; Study in Europe</a></li>
                    <li><a href="https://www.globalgroupofeducation.com/study-in-new-zealand">&bull; Study in New Zealand</a></li>
                </ul>
            </li>
            <li class="gge-drawer-has-sub">
                <a href="https://www.globalgroupofeducation.com/undergraduate-courses" class="gge-drawer-sub-toggle"><i class="fa fa-graduation-cap"></i> Courses <i class="fa fa-angle-down"></i></a>
                <ul class="gge-drawer-sub">
                    <li><a href="https://www.globalgroupofeducation.com/doctorate-courses">&bull; Doctorate Courses</a></li>
                    <li><a href="https://www.globalgroupofeducation.com/postgraduate-courses">&bull; Postgraduate Courses</a></li>
                    <li><a href="https://www.globalgroupofeducation.com/undergraduate-courses">&bull; Undergraduate Courses</a></li>
                    <li><a href="https://www.globalgroupofeducation.com/pre-master-courses">&bull; Pre-Master Courses</a></li>
                    <li><a href="https://www.globalgroupofeducation.com/foundation-courses">&bull; Foundation Courses</a></li>
                    <li><a href="https://www.globalgroupofeducation.com/english-language-courses">&bull; English Language Courses</a></li>
                </ul>
            </li>
            <li><a href="#services"><i class="fa fa-briefcase"></i> Our Services</a></li>
            <li><a href="#about"><i class="fa fa-institution"></i> About Us</a></li>
            <li><a href="/contact-us"><i class="fa fa-phone"></i> Contact Us</a></li>
        </ul>
        <div class="gge-drawer-cta">
            <a href="https://globalgroupofeducationportal.com/" target="_blank" class="gge-mk-login-btn" style="width: 100%; justify-content: center; margin-bottom: 10px;">
                <i class="fa fa-user"></i> Login
            </a>
            <a href="https://wa.me/447586589659" target="_blank" rel="noopener" class="gge-mk-whatsapp-btn" style="width: 100%; justify-content: center;">
                <i class="fa fa-whatsapp"></i> WhatsApp UK Counsellor
            </a>
        </div>
    </div>
    <div class="gge-drawer-backdrop" id="ggeDrawerBackdrop"></div>\n\n'''

for fpath in files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Replace from '<!-- 1. CURVED WHITE HEADER -->' to '<!-- 2. HERO VIDEO BANNER'
        new_content = re.sub(
            r'<!-- 1\. CURVED WHITE HEADER -->.*?<!-- 2\. HERO VIDEO BANNER',
            correct_header + '    <!-- 2. HERO VIDEO BANNER',
            content,
            flags=re.DOTALL
        )
        if new_content != content:
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Fixed header in {fpath}")
        else:
            print(f"Failed to match header in {fpath}")

print("Done.")
