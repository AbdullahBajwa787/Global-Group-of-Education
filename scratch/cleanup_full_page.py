scripts_block = """
<!-- Essential Scripts -->
<script src="/assets/js/jquery.min.js"></script>
<script src="/assets/assets/bootstrap/js/bootstrap.min.js"></script>
<script src="/assets/js/custom.js"></script>

<script>
// Mobile Drawer Navigation Toggle
document.addEventListener('DOMContentLoaded', function() {
    var toggleBtn = document.getElementById('ggeMobileMenuToggle');
    var drawer = document.getElementById('ggeMobileDrawer');
    var backdrop = document.getElementById('ggeDrawerBackdrop');
    var closeBtn = document.getElementById('ggeDrawerClose');
    
    function openDrawer() {
        if (drawer) drawer.classList.add('open');
        if (backdrop) backdrop.classList.add('open');
        document.body.style.overflow = 'hidden';
    }
    
    function closeDrawer() {
        if (drawer) drawer.classList.remove('open');
        if (backdrop) backdrop.classList.remove('open');
        document.body.style.overflow = '';
    }
    
    if (toggleBtn) toggleBtn.addEventListener('click', openDrawer);
    if (closeBtn) closeBtn.addEventListener('click', closeDrawer);
    if (backdrop) backdrop.addEventListener('click', closeDrawer);
    
    // Submenu toggles in mobile drawer
    var subToggles = document.querySelectorAll('.gge-drawer-sub-toggle');
    subToggles.forEach(function(btn) {
        btn.addEventListener('click', function(e) {
            e.preventDefault();
            var parent = this.parentElement;
            if (parent) parent.classList.toggle('open');
        });
    });
});
</script>

<!-- Floating WhatsApp Widget (Bottom-Right Item 13) -->
<a href="https://wa.me/447586589659?text=Hello%20Global%20Group%20of%20Education,%20I%20would%20like%20to%20get%20free%20admission%20guidance." target="_blank" rel="noopener" class="gge-floating-whatsapp" aria-label="Chat on WhatsApp">
    <i class="fa fa-whatsapp"></i>
</a>

</body>
</html>
"""

import re

files = ['index.html', 'public/index.html', 'public/pages/home.html', 'public/pages/index.html']

for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the end of ggeMockupHomepage
    # Inside ggeMockupHomepage, we have the bottom CTA and copyrgt-sctn
    # We want to remove everything from '<!-- Start Preloader -->' to '</html>'
    # and replace with the essential scripts + </body></html>
    idx_preloader = content.find('<!-- Start Preloader -->')
    if idx_preloader != -1:
        # Keep everything up to idx_preloader, but check if ggeMockupHomepage was properly closed
        head_part = content[:idx_preloader].rstrip()
        # Ensure ggeMockupHomepage is closed if it wasn't
        if '</div>\n<!-- ======================================================================= -->\n<!-- END GGE MODERN MOCKUP HOMEPAGE' not in head_part:
            if not head_part.endswith('</div>'):
                head_part += '\n</div>'
        
        new_content = head_part + '\n\n' + scripts_block.strip() + '\n'
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"[{fpath}] Cleaned up old classic content ({len(content) - len(new_content)} bytes removed)!")
    else:
        print(f"[{fpath}] '<!-- Start Preloader -->' not found!")

print("All files cleaned up!")
