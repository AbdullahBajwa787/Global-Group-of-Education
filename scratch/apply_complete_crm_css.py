import os

complete_crm_css = """
/* ========================================================================== */
/* COMPLETE CRM & OFFICIAL SITE STYLING (MATCHING EXACT USER REQUIREMENTS)   */
/* ========================================================================== */

/* Top Bar (CRM Style) */
.gge-crm-top-hdr {
    background: #071130 !important;
    padding: 8px 30px !important;
    border-bottom: 1px solid rgba(255, 255, 255, 0.08) !important;
    color: #ffffff !important;
    font-size: 13.5px !important;
}

.gge-crm-top-container {
    max-width: 1380px !important;
    margin: 0 auto !important;
    display: flex !important;
    align-items: center !important;
    justify-content: space-between !important;
    flex-wrap: wrap !important;
    gap: 12px !important;
}

.gge-crm-info-list {
    display: flex !important;
    align-items: center !important;
    gap: 24px !important;
    list-style: none !important;
    margin: 0 !important;
    padding: 0 !important;
    flex-wrap: wrap !important;
}

.gge-crm-info-list a {
    color: #e2e8f0 !important;
    text-decoration: none !important;
    display: inline-flex !important;
    align-items: center !important;
    gap: 7px !important;
    transition: color 0.2s ease !important;
}

.gge-crm-info-list a:hover {
    color: #fbb019 !important;
}

.gge-crm-social-box ul {
    display: flex !important;
    align-items: center !important;
    gap: 10px !important;
    list-style: none !important;
    margin: 0 !important;
    padding: 0 !important;
}

.gge-crm-social-box a {
    width: 30px !important;
    height: 30px !important;
    border-radius: 4px !important;
    background: rgba(255, 255, 255, 0.08) !important;
    color: #ffffff !important;
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    font-size: 13px !important;
    text-decoration: none !important;
    transition: all 0.25s ease !important;
}

.gge-crm-social-box a:hover {
    background: #eca411 !important;
    color: #ffffff !important;
    transform: translateY(-2px) !important;
}

/* Header Login Button */
.gge-mk-login-btn {
    background: #0d2552 !important;
    color: #ffffff !important;
    font-size: 14px !important;
    font-weight: 600 !important;
    border-radius: 5px !important;
    padding: 9px 20px !important;
    display: inline-flex !important;
    align-items: center !important;
    gap: 8px !important;
    text-decoration: none !important;
    transition: all 0.25s ease !important;
    border: 1px solid rgba(255, 255, 255, 0.15) !important;
}

.gge-mk-login-btn:hover {
    background: #eca411 !important;
    color: #ffffff !important;
    text-decoration: none !important;
    border-color: #fddf84 !important;
    box-shadow: 0 4px 14px rgba(236, 164, 17, 0.35) !important;
}

/* CRM About Us Section */
.about-section-ten {
    width: 100% !important;
    position: relative !important;
    padding: 85px 30px !important;
    background: #ffffff !important;
}

.about-container {
    max-width: 1320px !important;
    margin: 0 auto !important;
}

.about-grid {
    display: grid !important;
    grid-template-columns: 1fr 1fr !important;
    gap: 60px !important;
    align-items: center !important;
}

.about-content-col .sec-title {
    margin-bottom: 25px !important;
}

.about-content-col .sub-title {
    font-size: 14px !important;
    font-weight: 700 !important;
    color: #eca411 !important;
    text-transform: uppercase !important;
    letter-spacing: 1.5px !important;
    display: block !important;
    margin-bottom: 8px !important;
}

.about-content-col h2 {
    font-size: 38px !important;
    font-weight: 800 !important;
    color: #102771 !important;
    line-height: 1.25 !important;
    margin-bottom: 16px !important;
}

.about-content-col .about-lead-text {
    font-size: 16px !important;
    line-height: 1.75 !important;
    color: #4a5568 !important;
    margin-bottom: 24px !important;
}

.abt-txt h6 {
    color: #102771 !important;
    font-size: 17px !important;
    font-weight: 700 !important;
    padding-top: 14px !important;
    margin-bottom: 8px !important;
    border-bottom: 2px solid #eca411 !important;
    width: fit-content !important;
}

.abt-txt p {
    font-size: 15px !important;
    line-height: 1.7 !important;
    color: #4a5568 !important;
    margin-bottom: 16px !important;
}

.about-images-col {
    position: relative !important;
}

.about-img-wrap {
    position: relative !important;
    display: flex !important;
    justify-content: center !important;
}

.about-img-1 {
    width: 82% !important;
    border-radius: 12px !important;
    box-shadow: 0 15px 40px rgba(16, 39, 113, 0.12) !important;
    display: block !important;
}

.about-img-2 {
    position: absolute !important;
    right: 0 !important;
    top: 15% !important;
    width: 48% !important;
    border-radius: 10px !important;
    border: 6px solid #ffffff !important;
    box-shadow: 0 12px 35px rgba(0, 0, 0, 0.18) !important;
}

.about-experience-badge {
    position: absolute !important;
    bottom: -15px !important;
    left: 20px !important;
    background: #102771 !important;
    color: #ffffff !important;
    padding: 18px 28px !important;
    border-radius: 10px !important;
    text-align: center !important;
    box-shadow: 0 10px 30px rgba(16, 39, 113, 0.25) !important;
    border-left: 5px solid #eca411 !important;
}

.about-experience-badge strong {
    display: block !important;
    font-size: 40px !important;
    font-weight: 800 !important;
    line-height: 1 !important;
    color: #eca411 !important;
}

.about-experience-badge span {
    font-size: 13px !important;
    font-weight: 600 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.5px !important;
}

/* Call Info Contact Line */
.about-call-bar {
    margin-top: 55px !important;
    background: #f8fafc !important;
    border: 1.5px solid #102771 !important;
    border-radius: 8px !important;
    padding: 16px 28px !important;
    display: flex !important;
    align-items: center !important;
    justify-content: space-between !important;
    flex-wrap: wrap !important;
    gap: 16px !important;
}

.about-call-text {
    font-size: 18px !important;
    color: #1e293b !important;
    font-weight: 500 !important;
}

.about-call-text span {
    color: #102771 !important;
    font-weight: 700 !important;
    margin-left: 10px !important;
}

.about-call-btn {
    background: #102771 !important;
    color: #ffffff !important;
    font-size: 18px !important;
    font-weight: 700 !important;
    padding: 10px 26px !important;
    border-radius: 6px !important;
    display: inline-flex !important;
    align-items: center !important;
    gap: 10px !important;
    text-decoration: none !important;
    transition: all 0.25s ease !important;
}

.about-call-btn:hover {
    background: #eca411 !important;
    color: #ffffff !important;
    text-decoration: none !important;
    transform: translateY(-2px) !important;
}

/* CRM Services Section */
.service-sctn {
    padding: 85px 30px 75px !important;
    background: #091529 url('/assets/images/service-bg.jpg') no-repeat center center / cover !important;
    position: relative !important;
}

.service-sctn::before {
    content: '' !important;
    position: absolute !important;
    top: 0 !important; left: 0 !important; right: 0 !important; bottom: 0 !important;
    background: rgba(9, 21, 41, 0.90) !important;
    z-index: 1 !important;
}

.service-container {
    position: relative !important;
    z-index: 2 !important;
    max-width: 1320px !important;
    margin: 0 auto !important;
}

.service-header {
    text-align: center !important;
    margin-bottom: 50px !important;
}

.service-header h2 {
    font-size: 38px !important;
    font-weight: 800 !important;
    color: #ffffff !important;
    margin-bottom: 12px !important;
}

.service-header p {
    font-size: 16.5px !important;
    color: rgba(255, 255, 255, 0.85) !important;
    max-width: 650px !important;
    margin: 0 auto !important;
}

.service-grid {
    display: grid !important;
    grid-template-columns: repeat(3, 1fr) !important;
    gap: 30px !important;
}

.service-block-item {
    background: #091529 !important;
    border: 1px solid #162a52 !important;
    border-radius: 8px !important;
    padding: 30px 24px 26px 24px !important;
    position: relative !important;
    overflow: hidden !important;
    transition: all 0.35s ease !important;
    display: flex !important;
    flex-direction: column !important;
}

.service-block-item::before {
    content: '' !important;
    position: absolute !important;
    left: 0 !important; bottom: 0 !important;
    width: 100% !important; height: 0 !important;
    background: #122972 !important;
    transition: all 0.35s ease !important;
    z-index: 0 !important;
}

.service-block-item:hover::before {
    height: 100% !important;
}

.service-block-item:hover {
    border-color: #eca411 !important;
    transform: translateY(-5px) !important;
    box-shadow: 0 15px 35px rgba(0, 0, 0, 0.3) !important;
}

.service-icon-box {
    position: relative !important;
    z-index: 2 !important;
    width: 65px !important;
    height: 60px !important;
    background: #102771 !important;
    border-radius: 6px !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    font-size: 26px !important;
    color: #eca411 !important;
    margin-bottom: 20px !important;
    box-shadow: 0 4px 12px rgba(0,0,0,0.2) !important;
}

.service-content-box {
    position: relative !important;
    z-index: 2 !important;
}

.service-content-box .title {
    font-size: 20px !important;
    font-weight: 700 !important;
    color: #ffffff !important;
    margin-bottom: 12px !important;
}

.service-content-box .text {
    font-size: 14.5px !important;
    line-height: 1.65 !important;
    color: rgba(255, 255, 255, 0.8) !important;
}

/* 200+ Global Partners Cards Section */
.gge-stats-cards-section {
    padding: 70px 30px !important;
    background: #f8fafc !important;
}

.gge-stats-container {
    max-width: 1320px !important;
    margin: 0 auto !important;
}

.gge-stats-grid {
    display: grid !important;
    grid-template-columns: repeat(4, 1fr) !important;
    gap: 24px !important;
}

.gge-stat-card {
    background: #ffffff !important;
    border: 1.5px solid #e2e8f0 !important;
    border-radius: 10px !important;
    padding: 32px 24px !important;
    text-align: center !important;
    box-shadow: 0 6px 20px rgba(13, 37, 82, 0.05) !important;
    transition: all 0.3s ease !important;
}

.gge-stat-card:hover {
    border-color: #eca411 !important;
    transform: translateY(-5px) !important;
    box-shadow: 0 14px 30px rgba(13, 37, 82, 0.12) !important;
}

.gge-stat-card-icon {
    font-size: 34px !important;
    color: #eca411 !important;
    margin-bottom: 14px !important;
}

.gge-stat-card-number {
    font-size: 36px !important;
    font-weight: 800 !important;
    color: #102771 !important;
    line-height: 1.1 !important;
    margin-bottom: 8px !important;
}

.gge-stat-card-label {
    font-size: 15px !important;
    font-weight: 600 !important;
    color: #475569 !important;
}

/* Bottom CTA Banner (End of Page) */
.gge-bottom-cta-section {
    background: #071130 !important;
    padding: 75px 30px !important;
    text-align: center !important;
    position: relative !important;
    border-top: 3px solid #eca411 !important;
}

.gge-bottom-cta-container {
    max-width: 800px !important;
    margin: 0 auto !important;
}

.gge-bottom-cta-title {
    font-size: 42px !important;
    font-weight: 800 !important;
    color: #ffffff !important;
    margin-bottom: 14px !important;
    letter-spacing: -0.5px !important;
}

.gge-bottom-cta-desc {
    font-size: 17px !important;
    color: rgba(255, 255, 255, 0.9) !important;
    line-height: 1.6 !important;
    margin-bottom: 30px !important;
}

/* Clean Official Footer (Matching media_1794644004430_01e7fe27.png) */
.copyrgt-sctn {
    background: #050d24 !important;
    padding: 40px 30px 30px 30px !important;
    color: #ffffff !important;
    text-align: center !important;
    border-top: 1px solid rgba(255, 255, 255, 0.08) !important;
}

.foot-contct-dtl ul {
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    gap: 32px !important;
    list-style: none !important;
    padding: 0 !important;
    margin: 0 0 24px 0 !important;
    flex-wrap: wrap !important;
}

.foot-contct-dtl li {
    font-size: 15px !important;
    color: #cbd5e1 !important;
}

.foot-contct-dtl li i {
    color: #eca411 !important;
    margin-right: 8px !important;
}

.foot-contct-dtl a {
    color: #ffffff !important;
    text-decoration: none !important;
    font-weight: 500 !important;
    transition: color 0.2s ease !important;
}

.foot-contct-dtl a:hover {
    color: #eca411 !important;
}

.foot-scl-icon ul {
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    gap: 12px !important;
    list-style: none !important;
    padding: 0 !important;
    margin: 0 0 28px 0 !important;
}

.foot-scl-icon a {
    width: 38px !important;
    height: 38px !important;
    background: #0f1c3f !important;
    color: #ffffff !important;
    border-radius: 4px !important;
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    font-size: 16px !important;
    text-decoration: none !important;
    border: 1px solid rgba(255, 255, 255, 0.08) !important;
    transition: all 0.25s ease !important;
}

.foot-scl-icon a:hover {
    background: #eca411 !important;
    border-color: #fddf84 !important;
    color: #ffffff !important;
    transform: translateY(-3px) !important;
}

.copyrgt-sctn hr {
    border: none !important;
    border-top: 1px solid rgba(255, 255, 255, 0.1) !important;
    max-width: 900px !important;
    margin: 20px auto !important;
}

.cpyrgt-txt {
    font-size: 14px !important;
    color: #94a3b8 !important;
    line-height: 1.8 !important;
}

.cpyrgt-txt p {
    margin-bottom: 6px !important;
    color: #94a3b8 !important;
}

.cpyrgt-txt a {
    color: #cbd5e1 !important;
    text-decoration: none !important;
    transition: color 0.2s ease !important;
}

.cpyrgt-txt a:hover {
    color: #eca411 !important;
}

.footer_links {
    margin: 0 8px !important;
}

/* Floating WhatsApp Widget (Bottom-Right) */
.gge-floating-whatsapp {
    position: fixed !important;
    bottom: 24px !important;
    right: 24px !important;
    width: 60px !important;
    height: 60px !important;
    background: #25d366 !important;
    color: #ffffff !important;
    border-radius: 50% !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    font-size: 32px !important;
    box-shadow: 0 6px 24px rgba(37, 211, 102, 0.45) !important;
    z-index: 99999 !important;
    text-decoration: none !important;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
}

.gge-floating-whatsapp:hover {
    transform: scale(1.1) !important;
    background: #20ba5a !important;
    color: #ffffff !important;
    box-shadow: 0 10px 30px rgba(37, 211, 102, 0.6) !important;
}

@media (max-width: 991px) {
    .about-grid { grid-template-columns: 1fr !important; gap: 40px !important; }
    .service-grid { grid-template-columns: repeat(2, 1fr) !important; }
    .gge-stats-grid { grid-template-columns: repeat(2, 1fr) !important; }
}

@media (max-width: 767px) {
    .service-grid { grid-template-columns: 1fr !important; }
    .gge-stats-grid { grid-template-columns: 1fr !important; }
    .about-call-bar { flex-direction: column !important; text-align: center !important; }
    .about-content-col h2 { font-size: 28px !important; }
    .service-header h2 { font-size: 28px !important; }
    .gge-bottom-cta-title { font-size: 28px !important; }
}
"""

for path in ['assets/css/custom.css', 'public/assets/css/custom.css']:
    with open(path, 'r', encoding='utf-8') as f:
        existing = f.read()
    with open(path, 'w', encoding='utf-8') as f:
        f.write(existing + "\n" + complete_crm_css)
    print(f"Updated {path}")

print("CSS appended successfully!")
