import os
import re

html_files = [
    'index.html',
    'public/index.html',
    'public/pages/home.html',
    'public/pages/index.html'
]

crm_about_html = '''    <!-- 3. ABOUT US SECTION (FROM CRM LOGIN PAGE - EXACT MATCH) -->
    <section class="about-section-ten" id="about">
        <div class="container-fluid">
            <div class="row align-items-center">
                <div class="content-column col-xl-6 col-lg-7 col-md-12 col-sm-12 order-lg-2">
                    <div class="inner-column">
                        <div class="sec-title">
                            <span class="sub-title">ABOUT US</span>
                            <h2><span>Global Group Of Education</span></h2>
                            <div class="text">In this era of educational competition, the Global Group of Education brings you the finest consultants to help you achieve your desired degree from one of the best institutes in the UK and the world top-ranked universities. Our consultants are co-operative and excel at their work.</div>
                            <div class="abt-txt">
                                <h6>OUR WELL-GROUNDED TEAM</h6>
                                <div class="text">We have trustworthy consultant's veterans who are highly qualified and are skilled at their work. Our expert team that will guide you according to your preference and potential, and will also provide you with impartial advice.</div>
                                <h6>WHY CHOOSE GLOBAL GROUP OF EDUCATION?</h6>
                                <div class="text">We have a mission of making international education accessible and providing students with opportunities that will lead them towards a successful career. We are reliable, co-operative and have a fantastic team working to make education even more convenient.</div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="image-column col-xl-6 col-lg-5 col-md-12 col-sm-12">
                    <div class="inner-column">
                        <figure class="image-1"><img src="/assets/images/about/abt-img1.png" alt="Global Education Consultant" /></figure>
                        <figure class="image-2"><img src="/assets/images/about/abt-img2.png" alt="University Graduate" /></figure>
                        <div class="experience">
                            <div class="inner">
                                <div class="text">
                                    <strong>10</strong> Years of <br />
                                    experience
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="content-bottom">
                <div class="call-info-box-outer">
                    <div class="call-info-box-text">We provide full guidance to our students globally <span>Request A Call</span></div>
                    <div class="call-info-box">
                        <a href="tel:+447586589659"><span class="icon fa fa-phone"></span> +44 7586589659</a>
                    </div>
                </div>
            </div>
        </div>
    </section>'''

# 1. Update HTML files
for fpath in html_files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content = re.sub(
            r'<!-- 3\. ABOUT US SECTION.*?<section class="about-section-ten".*?</section>',
            crm_about_html,
            content,
            flags=re.DOTALL
        )
        if new_content != content:
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated about section in {fpath}")
        else:
            print(f"Could not regex replace about section in {fpath}")

# 2. Append/Update CSS
css_files = [
    'assets/css/custom.css',
    'public/assets/css/custom.css'
]

crm_about_css = '''
/* ========================================================================== */
/* EXACT CRM ABOUT US SECTION (MATCHING REFERENCE SCREENSHOT)                */
/* ========================================================================== */
.about-section-ten {
    width: 100% !important;
    position: relative !important;
    padding: 75px 40px !important;
    background: #ffffff !important;
}
.about-section-ten .container-fluid {
    max-width: 1320px !important;
    margin: 0 auto !important;
    padding: 0 15px !important;
}
.about-section-ten .content-column {
    position: relative !important;
}
.about-section-ten .content-column .inner-column {
    position: relative !important;
    padding-left: 20px !important;
}
@media (max-width: 991px) {
    .about-section-ten .content-column .inner-column {
        padding-left: 0 !important;
        margin-top: 40px !important;
    }
}
.about-section-ten .sec-title .sub-title {
    display: inline-block !important;
    font-size: 14px !important;
    font-weight: 700 !important;
    color: #eca411 !important;
    text-transform: uppercase !important;
    letter-spacing: 1.5px !important;
    margin-bottom: 8px !important;
}
.about-section-ten .sec-title h2 {
    font-size: 34px !important;
    font-weight: 800 !important;
    color: #102771 !important;
    margin-bottom: 20px !important;
    line-height: 1.25 !important;
}
.about-section-ten .sec-title .text {
    font-size: 15px !important;
    line-height: 26px !important;
    color: #555555 !important;
    margin-bottom: 20px !important;
}
.about-section-ten .abt-txt h6 {
    font-size: 15px !important;
    font-weight: 700 !important;
    color: #102771 !important;
    margin-top: 18px !important;
    margin-bottom: 6px !important;
    text-transform: uppercase !important;
    letter-spacing: 0.5px !important;
}
.about-section-ten .image-column {
    position: relative !important;
    margin-bottom: 0 !important;
}
.about-section-ten .image-column .inner-column {
    position: relative !important;
    max-width: 570px !important;
    margin: 0 auto !important;
    display: block !important;
}
.about-section-ten .image-column .image-1 {
    position: relative !important;
    margin-bottom: 0 !important;
    display: inline-block !important;
    width: 52% !important;
    max-width: 299px !important;
    vertical-align: top !important;
}
.about-section-ten .image-column .image-1 img {
    width: 100% !important;
    height: auto !important;
    display: block !important;
}
.about-section-ten .image-column .image-2 {
    position: absolute !important;
    right: 0 !important;
    top: 0 !important;
    margin-bottom: 0 !important;
    width: 48% !important;
    max-width: 270px !important;
    border: none !important;
    box-shadow: none !important;
    display: block !important;
}
.about-section-ten .image-column .image-2 img {
    width: 100% !important;
    height: auto !important;
    display: block !important;
}
.about-section-ten .experience {
    position: absolute !important;
    right: 0 !important;
    bottom: 0 !important;
    width: 48% !important;
    max-width: 270px !important;
    height: 190px !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    text-align: center !important;
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    padding: 0 !important;
}
.about-section-ten .experience:before {
    position: absolute !important;
    right: 0 !important;
    top: 0 !important;
    width: 100% !important;
    height: 100% !important;
    background-image: url(/assets/images/map.png) !important;
    background-repeat: no-repeat !important;
    background-position: center !important;
    background-size: contain !important;
    content: "" !important;
    opacity: 0.9 !important;
}
.about-section-ten .experience .inner {
    position: relative !important;
    z-index: 2 !important;
}
.about-section-ten .experience .text {
    color: #484750 !important;
    font-size: 15px !important;
    line-height: 22px !important;
    font-weight: 600 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.5px !important;
}
.about-section-ten .experience strong {
    color: #102771 !important;
    display: block !important;
    font-size: 65px !important;
    line-height: 1 !important;
    margin-bottom: 4px !important;
    font-weight: 800 !important;
}
.about-section-ten .content-bottom {
    margin-top: 45px !important;
    width: 100% !important;
}
.about-section-ten .content-bottom .call-info-box-outer {
    background-color: #f7f7f7 !important;
    border: 1.5px solid #102771 !important;
    padding: 10px 14px 10px 28px !important;
    align-items: center !important;
    display: flex !important;
    justify-content: space-between !important;
    border-radius: 6px !important;
    flex-wrap: wrap !important;
    gap: 15px !important;
    max-width: 100% !important;
}
.about-section-ten .content-bottom .call-info-box-outer .call-info-box-text {
    font-size: 16px !important;
    color: #222222 !important;
    font-weight: 500 !important;
}
.about-section-ten .content-bottom .call-info-box-outer .call-info-box-text span {
    color: #102771 !important;
    font-weight: 700 !important;
    margin-left: 20px !important;
}
.about-section-ten .content-bottom .call-info-box {
    background-color: #102771 !important;
    position: relative !important;
    padding: 10px 24px !important;
    border-radius: 4px !important;
    transition: 0.3s ease !important;
}
.about-section-ten .content-bottom .call-info-box:hover {
    background-color: #eca411 !important;
}
.about-section-ten .content-bottom .call-info-box a {
    color: #ffffff !important;
    font-size: 16px !important;
    font-weight: 700 !important;
    text-decoration: none !important;
    display: inline-flex !important;
    align-items: center !important;
    gap: 10px !important;
}
'''

for csspath in css_files:
    if os.path.exists(csspath):
        with open(csspath, 'r', encoding='utf-8') as f:
            css_content = f.read()
        css_content += crm_about_css
        with open(csspath, 'w', encoding='utf-8') as f:
            f.write(css_content)
        print(f"Appended crm_about_css to {csspath}")

print("Done exact CRM about application.")
