import os
import re

# 1. Update CSS in assets/css/custom.css and public/assets/css/custom.css
crm_hero_css = """
/* ========================================================================== */
/* CRM-STYLE HERO VIDEO BANNER & NEW BUTTONS (MATCHING IMAGE 2 & CRM PORTAL)  */
/* ========================================================================== */
.gge-mk-hero-section {
    position: relative !important;
    min-height: 600px !important;
    display: flex !important;
    align-items: center !important;
    overflow: hidden !important;
    background: #071130 !important;
}

.gge-mk-video-wrapper {
    position: absolute !important;
    top: 0 !important; left: 0 !important; right: 0 !important; bottom: 0 !important;
    width: 100% !important;
    height: 100% !important;
    overflow: hidden !important;
    z-index: 1 !important;
}

.gge-mk-hero-video {
    width: 100% !important;
    height: 100% !important;
    object-fit: cover !important;
    object-position: center !important;
}

.gge-mk-video-overlay {
    position: absolute !important;
    top: 0 !important; left: 0 !important; right: 0 !important; bottom: 0 !important;
    background: linear-gradient(90deg, rgba(7, 17, 48, 0.92) 0%, rgba(11, 19, 46, 0.78) 52%, rgba(7, 17, 48, 0.35) 85%, rgba(0, 0, 0, 0.15) 100%) !important;
    z-index: 2 !important;
}

.gge-mk-hero-grid.gge-mk-hero-fullwidth {
    position: relative !important;
    z-index: 5 !important;
    max-width: 1320px !important;
    width: 100% !important;
    margin: 0 auto !important;
    padding: 85px 25px 95px 25px !important;
    display: flex !important;
    align-items: center !important;
}

.gge-mk-hero-left {
    max-width: 680px !important;
    width: 100% !important;
}

.gge-mk-hero-tag {
    display: inline-block !important;
    font-size: 18px !important;
    font-weight: 600 !important;
    color: #ffffff !important;
    margin-bottom: 14px !important;
    letter-spacing: 0.3px !important;
}

.gge-tag-gold {
    color: #eca411 !important;
    font-weight: 700 !important;
}

.gge-mk-hero-title {
    font-size: 52px !important;
    font-weight: 800 !important;
    color: #ffffff !important;
    line-height: 1.15 !important;
    margin-bottom: 18px !important;
    text-shadow: 0 3px 12px rgba(0, 0, 0, 0.4) !important;
    letter-spacing: -0.5px !important;
}

.gge-mk-hero-desc {
    font-size: 16.5px !important;
    line-height: 1.65 !important;
    color: rgba(255, 255, 255, 0.92) !important;
    margin-bottom: 28px !important;
    max-width: 580px !important;
    text-shadow: 0 1px 4px rgba(0, 0, 0, 0.3) !important;
}

/* New Buttons exactly matching Image 2 & CRM Portal */
.bttn-bx,
.gge-hero-btn-row {
    display: flex !important;
    align-items: center !important;
    gap: 16px !important;
    margin-top: 22px !important;
    margin-bottom: 30px !important;
    flex-wrap: wrap !important;
}

.innr-bnr-bttn {
    font-size: 16px !important;
    font-weight: 600 !important;
    border-radius: 5px !important;
    padding: 12px 24px !important;
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    gap: 10px !important;
    white-space: nowrap !important;
    text-decoration: none !important;
    transition: all 0.28s ease !important;
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.2) !important;
    letter-spacing: 0.2px !important;
}

.colrd-bttn {
    background-color: #eca411 !important;
    color: #ffffff !important;
    border: 1px solid #fddf84 !important;
}

.colrd-bttn:hover {
    background-color: #d68f0a !important;
    color: #ffffff !important;
    border-color: #ffe69c !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 24px rgba(236, 164, 17, 0.45) !important;
    text-decoration: none !important;
}

.trns-bttn {
    background-color: #f2f4fd !important;
    color: #0c1226 !important;
    border: 1px solid rgba(123, 134, 154, 0.32) !important;
}

.trns-bttn:hover {
    background-color: #ffffff !important;
    color: #063385 !important;
    border-color: #ffffff !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 24px rgba(12, 18, 38, 0.25) !important;
    text-decoration: none !important;
}

/* Hero Trust Badges */
.gge-mk-hero-trust {
    display: flex !important;
    align-items: center !important;
    gap: 26px !important;
    flex-wrap: wrap !important;
    padding-top: 14px !important;
    border-top: 1px solid rgba(255, 255, 255, 0.15) !important;
}

.gge-mk-trust-item {
    display: flex !important;
    align-items: center !important;
    gap: 9px !important;
    color: rgba(255, 255, 255, 0.95) !important;
    font-size: 13.5px !important;
    font-weight: 500 !important;
}

.gge-mk-trust-icon {
    font-size: 17px !important;
    color: #fbb019 !important;
}

/* ========================================================================== */
/* TOP STUDY DESTINATIONS CONTINUOUS LINE MARQUEE                              */
/* ========================================================================== */
.gge-dest-marquee-viewport {
    width: 100% !important;
    overflow: hidden !important;
    position: relative !important;
    padding: 12px 0 24px 0 !important;
    mask-image: linear-gradient(to right, transparent 0%, black 4%, black 96%, transparent 100%) !important;
    -webkit-mask-image: linear-gradient(to right, transparent 0%, black 4%, black 96%, transparent 100%) !important;
}

.gge-dest-line-track {
    display: flex !important;
    gap: 20px !important;
    width: max-content !important;
    animation: ggeDestLineMarquee 38s linear infinite !important;
}

.gge-dest-line-track:hover {
    animation-play-state: paused !important;
}

@keyframes ggeDestLineMarquee {
    0% { transform: translateX(0); }
    100% { transform: translateX(-50%); }
}

@media (max-width: 991px) {
    .gge-mk-hero-title { font-size: 40px !important; }
    .gge-mk-hero-section { min-height: 520px !important; }
    .gge-mk-video-overlay {
        background: linear-gradient(180deg, rgba(7, 17, 48, 0.88) 0%, rgba(11, 19, 46, 0.95) 100%) !important;
    }
}

@media (max-width: 767px) {
    .gge-mk-hero-title { font-size: 32px !important; }
    .gge-mk-hero-desc { font-size: 15px !important; }
    .bttn-bx, .gge-hero-btn-row { flex-direction: column !important; align-items: stretch !important; gap: 12px !important; }
    .innr-bnr-bttn { width: 100% !important; }
    .gge-mk-hero-trust { flex-direction: column !important; align-items: flex-start !important; gap: 12px !important; }
}
"""

for css_file in ['assets/css/custom.css', 'public/assets/css/custom.css']:
    with open(css_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Append the new css at the end
    content += "\n" + crm_hero_css
    with open(css_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated CSS in", css_file)

print("CSS updates completed successfully!")
