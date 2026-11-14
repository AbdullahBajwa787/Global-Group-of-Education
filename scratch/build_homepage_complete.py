import re

HTML_STRUCTURE = """
<!-- ======================================================================= -->
<!-- GGE MODERN MOCKUP HOMEPAGE (ACTIVE DEFAULT VIEW)                        -->
<!-- ======================================================================= -->
<div id="ggeMockupHomepage" class="gge-homepage-view" style="display: block;">

    <!-- TOP HEADER BAR (CRM STYLE: CONTACT & SOCIAL, NO ANNOUNCEMENT BORDER) -->
    <div class="gge-crm-top-hdr">
        <div class="gge-crm-top-container">
            <ul class="gge-crm-info-list">
                <li><a href="tel:+447586589659"><i class="fa fa-phone"></i> +44 7586589659</a></li>
                <li><a href="mailto:london@globalgroupofeducation.com"><i class="fa fa-envelope-o"></i> london@globalgroupofeducation.com</a></li>
                <li><a href="#"><i class="fa fa-map-marker"></i> 126 East Ferry Road, Canary Wharf, London, UK, E14 9FP</a></li>
            </ul>
            <div class="gge-crm-social-box">
                <ul>
                    <li><a href="https://www.linkedin.com/company/global-group-of-education/" target="_blank" rel="noopener" aria-label="LinkedIn"><i class="fa fa-linkedin"></i></a></li>
                    <li><a href="https://www.instagram.com/gge.pakistan/" target="_blank" rel="noopener" aria-label="Instagram"><i class="fa fa-instagram"></i></a></li>
                    <li><a href="http://www.youtube.com/@globalgroupofeducation" target="_blank" rel="noopener" aria-label="YouTube"><i class="fa fa-youtube-play"></i></a></li>
                    <li><a href="https://www.facebook.com/globalgroupofeducationUKofficial/" target="_blank" rel="noopener" aria-label="Facebook"><i class="fa fa-facebook"></i></a></li>
                    <li><a href="https://x.com/globalgroupedu" target="_blank" rel="noopener" aria-label="Twitter"><i class="fa fa-twitter"></i></a></li>
                </ul>
            </div>
        </div>
    </div>

    <!-- 1. CURVED WHITE HEADER -->
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
                    <li class="gge-mk-nav-item">
                        <a href="#destinations" class="gge-mk-nav-link"><i class="fa fa-globe"></i> Study Destinations <i class="fa fa-angle-down"></i></a>
                        <ul class="gge-mk-nav-dropdown">
                            <li><a href="/study-in-uk"><i class="fa fa-flag"></i> Study in UK</a></li>
                            <li><a href="/study-in-usa"><i class="fa fa-flag"></i> Study in USA</a></li>
                            <li><a href="/study-in-canada"><i class="fa fa-flag"></i> Study in Canada</a></li>
                            <li><a href="/study-in-australia"><i class="fa fa-flag"></i> Study in Australia</a></li>
                            <li><a href="/study-in-europe"><i class="fa fa-flag"></i> Study in Europe</a></li>
                            <li><a href="/study-in-new-zealand"><i class="fa fa-flag"></i> Study in New Zealand</a></li>
                        </ul>
                    </li>
                    <li class="gge-mk-nav-item">
                        <a href="#courses" class="gge-mk-nav-link"><i class="fa fa-graduation-cap"></i> Courses <i class="fa fa-angle-down"></i></a>
                        <ul class="gge-mk-nav-dropdown">
                            <li><a href="https://www.globalgroupofeducation.com/doctorate-courses" target="_blank"><i class="fa fa-certificate"></i> Doctorate Courses</a></li>
                            <li><a href="https://www.globalgroupofeducation.com/postgraduate-courses" target="_blank"><i class="fa fa-graduation-cap"></i> Postgraduate Courses</a></li>
                            <li><a href="https://www.globalgroupofeducation.com/undergraduate-courses" target="_blank"><i class="fa fa-book"></i> Undergraduate Courses</a></li>
                            <li><a href="https://www.globalgroupofeducation.com/pre-master-courses" target="_blank"><i class="fa fa-university"></i> Pre-Master Courses</a></li>
                            <li><a href="https://www.globalgroupofeducation.com/foundation-courses" target="_blank"><i class="fa fa-cubes"></i> Foundation Courses</a></li>
                            <li><a href="https://www.globalgroupofeducation.com/english-language-courses" target="_blank"><i class="fa fa-language"></i> English Language Courses</a></li>
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
                <!-- Item 12: Login button with user icon -->
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
            <li><a href="#destinations"><i class="fa fa-globe"></i> Study Destinations</a></li>
            <li class="gge-drawer-has-sub">
                <a href="#courses" class="gge-drawer-sub-toggle"><i class="fa fa-graduation-cap"></i> Courses <i class="fa fa-angle-down"></i></a>
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
    <div class="gge-drawer-backdrop" id="ggeDrawerBackdrop"></div>

    <!-- 2. HERO VIDEO BANNER (CRM LOGIN PAGE STYLE) -->
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
            <div class="gge-mk-hero-left">
                <span class="gge-mk-hero-tag">Welcome and <span class="gge-tag-gold">Join Us for Success</span></span>
                <h1 class="gge-mk-hero-title">Your Gateway to<br>Studying Abroad</h1>
                <p class="gge-mk-hero-desc">
                    We provide a complete admissions services for Australia, Canada, Europe, UK, USA and other countries.
                </p>
                
                <!-- Buttons matching Image 2 exactly (Item 1) -->
                <div class="bttn-bx gge-hero-btn-row">
                    <a href="https://globalgroupofeducationportal.com/partner-registration" class="innr-bnr-bttn colrd-bttn" target="_blank" rel="noopener">
                        <i class="fa fa-user"></i> Be a Partner
                    </a>
                    <a href="https://globalgroupofeducationportal.com/student-registration" class="innr-bnr-bttn trns-bttn" target="_blank" rel="noopener">
                        <i class="fa fa-graduation-cap"></i> Be a Student
                    </a>
                </div>
            </div>
        </div>
    </section>

    <!-- 3. ABOUT US SECTION (FROM CRM LOGIN PAGE) -->
    <section class="about-section-ten" id="about">
        <div class="about-container">
            <div class="about-grid">
                <div class="about-content-col">
                    <div class="sec-title">
                        <span class="sub-title">ABOUT US</span>
                        <h2>Global Group Of Education</h2>
                    </div>
                    <p class="about-lead-text">
                        In this era of educational competition, the Global Group of Education brings you the finest consultants to help you achieve your desired degree from one of the best institutes in the UK and the world top-ranked universities. Our consultants are co-operative and excel at their work.
                    </p>
                    <div class="abt-txt">
                        <h6>OUR WELL-GROUNDED TEAM</h6>
                        <p>We have trustworthy consultant's veterans who are highly qualified and are skilled at their work. Our expert team that will guide you according to your preference and potential, and will also provide you with impartial advice.</p>
                        <h6>WHY CHOOSE GLOBAL GROUP OF EDUCATION?</h6>
                        <p>We have a mission of making international education accessible and providing students with opportunities that will lead them towards a successful career. We are reliable, co-operative and have a fantastic team working to make education even more convenient.</p>
                    </div>
                </div>

                <div class="about-images-col">
                    <div class="about-img-wrap">
                        <img src="/assets/images/about/abt-img1.png" alt="Global Education Consultant" class="about-img-1">
                        <img src="/assets/images/about/abt-img2.png" alt="University Campus" class="about-img-2">
                        <div class="about-experience-badge">
                            <strong>10</strong>
                            <span>Years of Experience</span>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Contact Line Bar -->
            <div class="about-call-bar">
                <div class="about-call-text">
                    We provide full guidance to our students globally. <span>Request A Call</span>
                </div>
                <a href="tel:+447586589659" class="about-call-btn">
                    <i class="fa fa-phone"></i> +44 7586589659
                </a>
            </div>
        </div>
    </section>

    <!-- 4. SERVICES SECTION (FROM CRM LOGIN PAGE) -->
    <section class="service-sctn" id="services">
        <div class="service-container">
            <div class="service-header">
                <h2>Services</h2>
                <p>Global Group of education helps you get admission in your preferred university.</p>
            </div>
            <div class="service-grid">
                <!-- 1 -->
                <div class="service-block-item">
                    <div class="service-icon-box">
                        <i class="fa fa-university"></i>
                    </div>
                    <div class="service-content-box">
                        <h4 class="title">University Selection &amp; Guidance</h4>
                        <p class="text">We help you choose the right universities and handle accommodation, travel, and pre-departure preparations for a smooth transition.</p>
                    </div>
                </div>
                <!-- 2 -->
                <div class="service-block-item">
                    <div class="service-icon-box">
                        <i class="fa fa-list-alt"></i>
                    </div>
                    <div class="service-content-box">
                        <h4 class="title">Admissions &amp; Interview Preparation</h4>
                        <p class="text">Our consultants and admissions officers work together to create strong applications and provide top guidance for interview preparation, setting students up for success.</p>
                    </div>
                </div>
                <!-- 3 -->
                <div class="service-block-item">
                    <div class="service-icon-box">
                        <i class="fa fa-money"></i>
                    </div>
                    <div class="service-content-box">
                        <h4 class="title">Scholarships at Top Universities</h4>
                        <p class="text">We partner with top UK universities to secure scholarships for our students, easing the path to studying abroad.</p>
                    </div>
                </div>
                <!-- 4 -->
                <div class="service-block-item">
                    <div class="service-icon-box">
                        <i class="fa fa-plane"></i>
                    </div>
                    <div class="service-content-box">
                        <h4 class="title">Visa &amp; Immigration Support</h4>
                        <p class="text">Our dedicated team at headquarters will help you secure your study visa for your chosen field, ensuring a smooth application process.</p>
                    </div>
                </div>
                <!-- 5 -->
                <div class="service-block-item">
                    <div class="service-icon-box">
                        <i class="fa fa-users"></i>
                    </div>
                    <div class="service-content-box">
                        <h4 class="title">Test Preparation</h4>
                        <p class="text">With our comprehensive approach to test preparation, we help you achieve optimal scores on language proficiency tests such as IELTS, LanguageCert, PTE, and others.</p>
                    </div>
                </div>
                <!-- 6 -->
                <div class="service-block-item">
                    <div class="service-icon-box">
                        <i class="fa fa-briefcase"></i>
                    </div>
                    <div class="service-content-box">
                        <h4 class="title">Post-Study Work Opportunities</h4>
                        <p class="text">We provide expert guidance on post-study work opportunities through our global network, helping you maximize your career prospects after graduation.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 5. TOP STUDY DESTINATIONS (FULL-WIDTH CONTINUOUS RUNNING LINE / MARQUEE) -->
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
    </section>

    <!-- 6. POPULAR UNIVERSITIES (WORLD-CLASS CONTINUOUS RUNNING LINE / MARQUEE) -->
    <section class="gge-uni-line-section" id="universities">
        <div class="gge-line-container">
            <div class="gge-line-header">
                <div class="gge-line-header-left">
                    <span class="gge-line-eyebrow">PRESTIGIOUS INSTITUTIONS</span>
                    <h2 class="gge-line-title">Popular Universities</h2>
                    <p class="gge-line-subtitle">Direct fast-track admissions to accredited universities across the globe.</p>
                </div>
                <div class="gge-line-header-right">
                    <a href="https://www.globalgroupofeducation.com/all-universities" target="_blank" class="gge-line-view-all">View All Universities &rarr;</a>
                </div>
            </div>
        </div>

        <!-- Infinite Running Marquee Track -->
        <div class="gge-uni-marquee-viewport">
            <div class="gge-uni-marquee-track">
                <!-- Set 1 -->
                <a href="/universities/northwood-university" class="gge-uni-marquee-tile" title="Northwood University">
                    <img src="/assets/images/mockup/unis/northwood.png" alt="Northwood University">
                </a>
                <a href="/universities/the-university-of-winchester" class="gge-uni-marquee-tile" title="University of Winchester">
                    <img src="/assets/images/mockup/unis/winchester.png" alt="University of Winchester">
                </a>
                <a href="/universities/heriot-watt-university" class="gge-uni-marquee-tile" title="Heriot-Watt University">
                    <img src="/assets/images/mockup/unis/heriot_watt.png" alt="Heriot-Watt University">
                </a>
                <a href="/universities/st_-george-university" class="gge-uni-marquee-tile" title="St. George's University">
                    <img src="/assets/images/mockup/unis/st_georges.png" alt="St. George's University">
                </a>
                <a href="/universities/queens-university-belfast" class="gge-uni-marquee-tile" title="Queen's University Belfast">
                    <img src="/assets/images/mockup/unis/queens_belfast.png" alt="Queen's University Belfast">
                </a>
                <a href="/courses" class="gge-uni-marquee-tile" title="LanguageCert Official Partner">
                    <img src="/assets/images/mockup/unis/language_cert.png" alt="LanguageCert">
                </a>
                <a href="/universities/falmouth-university" class="gge-uni-marquee-tile" title="Falmouth University">
                    <img src="/assets/images/mockup/unis/falmouth.png" alt="Falmouth University">
                </a>
                <a href="/courses" class="gge-uni-marquee-tile" title="University of Strathclyde">
                    <img src="/assets/images/mockup/unis/strathclyde.png" alt="University of Strathclyde">
                </a>

                <!-- Set 2 (Duplicate for seamless infinite loop) -->
                <a href="/universities/northwood-university" class="gge-uni-marquee-tile" title="Northwood University">
                    <img src="/assets/images/mockup/unis/northwood.png" alt="Northwood University">
                </a>
                <a href="/universities/the-university-of-winchester" class="gge-uni-marquee-tile" title="University of Winchester">
                    <img src="/assets/images/mockup/unis/winchester.png" alt="University of Winchester">
                </a>
                <a href="/universities/heriot-watt-university" class="gge-uni-marquee-tile" title="Heriot-Watt University">
                    <img src="/assets/images/mockup/unis/heriot_watt.png" alt="Heriot-Watt University">
                </a>
                <a href="/universities/st_-george-university" class="gge-uni-marquee-tile" title="St. George's University">
                    <img src="/assets/images/mockup/unis/st_georges.png" alt="St. George's University">
                </a>
                <a href="/universities/queens-university-belfast" class="gge-uni-marquee-tile" title="Queen's University Belfast">
                    <img src="/assets/images/mockup/unis/queens_belfast.png" alt="Queen's University Belfast">
                </a>
                <a href="/courses" class="gge-uni-marquee-tile" title="LanguageCert Official Partner">
                    <img src="/assets/images/mockup/unis/language_cert.png" alt="LanguageCert">
                </a>
                <a href="/universities/falmouth-university" class="gge-uni-marquee-tile" title="Falmouth University">
                    <img src="/assets/images/mockup/unis/falmouth.png" alt="Falmouth University">
                </a>
                <a href="/courses" class="gge-uni-marquee-tile" title="University of Strathclyde">
                    <img src="/assets/images/mockup/unis/strathclyde.png" alt="University of Strathclyde">
                </a>
            </div>
        </div>
    </section>

    <!-- 7. 200+ GLOBAL PARTNERS IN CARDS SHAPE (ITEM 19) -->
    <section class="gge-stats-cards-section">
        <div class="gge-stats-container">
            <div class="gge-stats-grid">
                <div class="gge-stat-card">
                    <div class="gge-stat-card-icon"><i class="fa fa-graduation-cap"></i></div>
                    <div class="gge-stat-card-number">10,000+</div>
                    <div class="gge-stat-card-label">Successful Applications</div>
                </div>
                <div class="gge-stat-card">
                    <div class="gge-stat-card-icon"><i class="fa fa-university"></i></div>
                    <div class="gge-stat-card-number">200+</div>
                    <div class="gge-stat-card-label">Partner Universities</div>
                </div>
                <div class="gge-stat-card">
                    <div class="gge-stat-card-icon"><i class="fa fa-globe"></i></div>
                    <div class="gge-stat-card-number">10+</div>
                    <div class="gge-stat-card-label">Study Destinations</div>
                </div>
                <div class="gge-stat-card">
                    <div class="gge-stat-card-icon"><i class="fa fa-smile-o"></i></div>
                    <div class="gge-stat-card-number">95%</div>
                    <div class="gge-stat-card-label">Student Satisfaction</div>
                </div>
            </div>
        </div>
    </section>

    <!-- 8. EXPLORE ACADEMIC COURSES SECTION -->
    <section class="gge-courses-section" id="courses">
        <div class="gge-line-container">
            <div class="gge-line-header">
                <div class="gge-line-header-left">
                    <span class="gge-line-eyebrow">ACADEMIC PROGRAMS</span>
                    <h2 class="gge-line-title">Explore Academic Courses</h2>
                    <p class="gge-line-subtitle">Find accredited undergraduate, postgraduate, doctorate &amp; language programs at leading global universities.</p>
                </div>
                <div class="gge-line-header-right">
                    <a href="https://www.globalgroupofeducation.com/undergraduate-courses" target="_blank" class="gge-line-view-all">View All Courses &rarr;</a>
                </div>
            </div>

            <div class="gge-courses-grid">
                <a href="https://www.globalgroupofeducation.com/doctorate-courses" target="_blank" rel="noopener" class="gge-course-card">
                    <div class="gge-course-icon-wrap"><i class="fa fa-certificate"></i></div>
                    <h3 class="gge-course-card-title">Doctorate Courses</h3>
                    <p class="gge-course-card-desc">Advanced PhD, DBA and doctoral research programs with global academic recognition and funding opportunities.</p>
                    <span class="gge-course-card-link">Explore Doctorate &rarr;</span>
                </a>
                <a href="https://www.globalgroupofeducation.com/postgraduate-courses" target="_blank" rel="noopener" class="gge-course-card">
                    <div class="gge-course-icon-wrap"><i class="fa fa-graduation-cap"></i></div>
                    <h3 class="gge-course-card-title">Postgraduate Courses</h3>
                    <p class="gge-course-card-desc">Master's degrees, MSc, MA and MBA programs with post-study work visa eligibility in UK, Canada, Australia and USA.</p>
                    <span class="gge-course-card-link">Explore Postgraduate &rarr;</span>
                </a>
                <a href="https://www.globalgroupofeducation.com/undergraduate-courses" target="_blank" rel="noopener" class="gge-course-card">
                    <div class="gge-course-icon-wrap"><i class="fa fa-book"></i></div>
                    <h3 class="gge-course-card-title">Undergraduate Courses</h3>
                    <p class="gge-course-card-desc">Bachelor's degrees (BSc, BA, BEng) across STEM, Business, Healthcare and Arts with scholarship guidance.</p>
                    <span class="gge-course-card-link">Explore Undergraduate &rarr;</span>
                </a>
                <a href="https://www.globalgroupofeducation.com/pre-master-courses" target="_blank" rel="noopener" class="gge-course-card">
                    <div class="gge-course-icon-wrap"><i class="fa fa-university"></i></div>
                    <h3 class="gge-course-card-title">Pre-Master Courses</h3>
                    <p class="gge-course-card-desc">Bridge programs bridging academic and language prerequisites directly into top-ranked master's degrees.</p>
                    <span class="gge-course-card-link">Explore Pre-Master &rarr;</span>
                </a>
                <a href="https://www.globalgroupofeducation.com/foundation-courses" target="_blank" rel="noopener" class="gge-course-card">
                    <div class="gge-course-icon-wrap"><i class="fa fa-cubes"></i></div>
                    <h3 class="gge-course-card-title">Foundation Courses</h3>
                    <p class="gge-course-card-desc">Fast-track pathway programs preparing international students for direct university bachelor degree entry.</p>
                    <span class="gge-course-card-link">Explore Foundation &rarr;</span>
                </a>
                <a href="https://www.globalgroupofeducation.com/english-language-courses" target="_blank" rel="noopener" class="gge-course-card">
                    <div class="gge-course-icon-wrap"><i class="fa fa-language"></i></div>
                    <h3 class="gge-course-card-title">English Language Courses</h3>
                    <p class="gge-course-card-desc">IELTS, PTE and LanguageCert test preparation courses tailored for student visa language requirements.</p>
                    <span class="gge-course-card-link">Explore Language &rarr;</span>
                </a>
            </div>
        </div>
    </section>

    <!-- 9. BOTTOM CTA BANNER (YOUR GATEWAY TO STUDYING ABROAD - END OF PAGE) -->
    <section class="gge-bottom-cta-section">
        <div class="gge-bottom-cta-container">
            <h2 class="gge-bottom-cta-title">Your Gateway to Studying Abroad</h2>
            <p class="gge-bottom-cta-desc">
                We provide a complete admissions services for Australia, Canada, Europe, UK, USA and other countries.
            </p>
            <div class="bttn-bx" style="justify-content: center;">
                <a href="https://globalgroupofeducationportal.com/partner-registration" class="innr-bnr-bttn colrd-bttn" target="_blank" rel="noopener">
                    <i class="fa fa-user"></i> Be a Partner
                </a>
                <a href="https://globalgroupofeducationportal.com/student-registration" class="innr-bnr-bttn trns-bttn" target="_blank" rel="noopener">
                    <i class="fa fa-graduation-cap"></i> Be a Student
                </a>
            </div>
        </div>
    </section>

    <!-- 10. CLEAN OFFICIAL FOOTER (MATCHING media_1794644004430_01e7fe27.png) -->
    <footer class="copyrgt-sctn">
        <div class="container-fluid">
            <div class="row">
                <div class="col-lg-12">
                    <div class="foot-contct-dtl">
                        <ul>
                            <li><i class="fa fa-phone"></i> <a href="tel:+447586589659">+44 7586589659</a></li>
                            <li><i class="fa fa-envelope-o"></i> <a href="mailto:london@globalgroupofeducation.com">london@globalgroupofeducation.com</a></li>
                            <li><i class="fa fa-globe"></i> <a href="https://www.globalgroupofeducation.com/" target="_blank">Global Group of Education</a></li>
                        </ul>
                    </div>
                </div>

                <div class="col-lg-12">
                    <div class="foot-scl-icon social-box">
                        <ul>
                            <li class="linkedin"><a href="https://www.linkedin.com/company/global-group-of-education/" target="_blank" rel="noopener" aria-label="LinkedIn"><i class="fa fa-linkedin"></i></a></li>
                            <li class="instagram"><a href="https://www.instagram.com/gge.pakistan/" target="_blank" rel="noopener" aria-label="Instagram"><i class="fa fa-instagram"></i></a></li>
                            <li class="youtube"><a href="http://www.youtube.com/@globalgroupofeducation" target="_blank" rel="noopener" aria-label="YouTube"><i class="fa fa-youtube-play"></i></a></li>
                            <li class="facebook"><a href="https://www.facebook.com/globalgroupofeducationUKofficial/" target="_blank" rel="noopener" aria-label="Facebook"><i class="fa fa-facebook"></i></a></li>
                            <li class="twitter"><a href="https://x.com/globalgroupedu" target="_blank" rel="noopener" aria-label="Twitter"><i class="fa fa-twitter"></i></a></li>
                        </ul>
                    </div>
                </div>

                <hr>
                <div class="col-lg-12">
                    <div class="cpyrgt-txt">
                        <p>&copy; Copyright <a href="https://www.globalgroupofeducation.com/" target="_blank">Global Group of Education</a>.</p>
                        <a href="/terms-and-conditions" class="footer_links">Terms and Conditions</a> |
                        <a href="/privacy-policy" class="footer_links">Privacy Policy</a> |
                        <a href="/cookie-policy" class="footer_links">Cookie Policy</a>
                    </div>
                </div>
            </div>
        </div>
    </footer>

    <!-- 11. FLOATING WHATSAPP BUTTON (BOTTOM-RIGHT ITEM 13) -->
    <a href="https://wa.me/447586589659" target="_blank" rel="noopener" class="gge-floating-whatsapp" aria-label="Chat on WhatsApp">
        <i class="fa fa-whatsapp"></i>
    </a>

</div>
<!-- ======================================================================= -->
<!-- END GGE MODERN MOCKUP HOMEPAGE                                          -->
<!-- ======================================================================= -->
"""

files = ['index.html', 'public/index.html', 'public/pages/home.html', 'public/pages/index.html']

for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace the entire ggeMockupHomepage block
    pattern = re.compile(
        r'<div id="ggeMockupHomepage"[^>]*>.*?</div>\s*<!-- ======================================================================= -->\s*<!-- END GGE MODERN MOCKUP HOMEPAGE',
        re.DOTALL
    )
    if pattern.search(content):
        content = pattern.sub(HTML_STRUCTURE.strip(), content)
        print(f"[{fpath}] Replaced ggeMockupHomepage block successfully!")
    else:
        # Looser pattern
        pattern2 = re.compile(
            r'<div id="ggeMockupHomepage"[^>]*>.*?<!-- Start Preloader -->',
            re.DOTALL
        )
        if pattern2.search(content):
            content = pattern2.sub(HTML_STRUCTURE.strip() + '\n\n<!-- Start Preloader -->', content)
            print(f"[{fpath}] Replaced ggeMockupHomepage (looser) successfully!")
        else:
            print(f"[{fpath}] ERROR: Pattern could not find ggeMockupHomepage!")

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"[{fpath}] Saved.")

print("All HTML files processed!")
