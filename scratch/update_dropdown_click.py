import os

files = [
    'index.html',
    'public/index.html',
    'public/pages/home.html',
    'public/pages/index.html'
]

target_nav = '''                    <li class="gge-mk-nav-item">
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
                        <a href="https://www.globalgroupofeducation.com/undergraduate-courses" class="gge-mk-nav-link"><i class="fa fa-graduation-cap"></i> Courses <i class="fa fa-angle-down"></i></a>
                        <ul class="gge-mk-nav-dropdown">'''

replacement_nav = '''                    <li class="gge-mk-nav-item gge-has-dropdown">
                        <a href="javascript:void(0)" class="gge-mk-nav-link gge-nav-dropdown-toggle" role="button" aria-haspopup="true" aria-expanded="false"><i class="fa fa-globe"></i> Study Destinations <i class="fa fa-angle-down"></i></a>
                        <ul class="gge-mk-nav-dropdown">
                            <li><a href="/study-in-uk"><i class="fa fa-flag"></i> Study in UK</a></li>
                            <li><a href="/study-in-usa"><i class="fa fa-flag"></i> Study in USA</a></li>
                            <li><a href="/study-in-canada"><i class="fa fa-flag"></i> Study in Canada</a></li>
                            <li><a href="/study-in-australia"><i class="fa fa-flag"></i> Study in Australia</a></li>
                            <li><a href="/study-in-europe"><i class="fa fa-flag"></i> Study in Europe</a></li>
                            <li><a href="/study-in-new-zealand"><i class="fa fa-flag"></i> Study in New Zealand</a></li>
                        </ul>
                    </li>
                    <li class="gge-mk-nav-item gge-has-dropdown">
                        <a href="javascript:void(0)" class="gge-mk-nav-link gge-nav-dropdown-toggle" role="button" aria-haspopup="true" aria-expanded="false"><i class="fa fa-graduation-cap"></i> Courses <i class="fa fa-angle-down"></i></a>
                        <ul class="gge-mk-nav-dropdown">'''

target_script = '''    // Submenu toggles in mobile drawer
    var subToggles = document.querySelectorAll('.gge-drawer-sub-toggle');
    subToggles.forEach(function(btn) {
        btn.addEventListener('click', function(e) {
            e.preventDefault();
            var parent = this.parentElement;
            if (parent) parent.classList.toggle('open');
        });
    });
});'''

replacement_script = '''    // Submenu toggles in mobile drawer
    var subToggles = document.querySelectorAll('.gge-drawer-sub-toggle');
    subToggles.forEach(function(btn) {
        btn.addEventListener('click', function(e) {
            e.preventDefault();
            var parent = this.parentElement;
            if (parent) parent.classList.toggle('open');
        });
    });

    // Desktop Header Dropdowns: Study Destinations & Courses open ONLY on mouse click, NOT on hover
    var desktopDropdowns = document.querySelectorAll('.gge-mk-nav-item.gge-has-dropdown');
    desktopDropdowns.forEach(function(item) {
        var toggleLink = item.querySelector('.gge-nav-dropdown-toggle') || item.querySelector('.gge-mk-nav-link');
        if (!toggleLink) return;
        
        toggleLink.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();
            
            var wasOpen = item.classList.contains('open');
            
            // Close other dropdowns
            desktopDropdowns.forEach(function(other) {
                if (other !== item) {
                    other.classList.remove('open');
                    var otherLink = other.querySelector('.gge-nav-dropdown-toggle') || other.querySelector('.gge-mk-nav-link');
                    if (otherLink) otherLink.setAttribute('aria-expanded', 'false');
                }
            });
            
            if (wasOpen) {
                item.classList.remove('open');
                toggleLink.setAttribute('aria-expanded', 'false');
            } else {
                item.classList.add('open');
                toggleLink.setAttribute('aria-expanded', 'true');
            }
        });
    });
    
    // Close dropdowns on outside click
    document.addEventListener('click', function(e) {
        if (!e.target.closest('.gge-mk-nav-item.gge-has-dropdown')) {
            desktopDropdowns.forEach(function(item) {
                item.classList.remove('open');
                var toggleLink = item.querySelector('.gge-nav-dropdown-toggle') || item.querySelector('.gge-mk-nav-link');
                if (toggleLink) toggleLink.setAttribute('aria-expanded', 'false');
            });
        }
    });

    // Close on Escape key
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') {
            desktopDropdowns.forEach(function(item) {
                item.classList.remove('open');
                var toggleLink = item.querySelector('.gge-nav-dropdown-toggle') || item.querySelector('.gge-mk-nav-link');
                if (toggleLink) toggleLink.setAttribute('aria-expanded', 'false');
            });
        }
    });
});'''

for fpath in files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Normalize CRLF
        content_norm = content.replace('\r\n', '\n')
        target_nav_norm = target_nav.replace('\r\n', '\n')
        replacement_nav_norm = replacement_nav.replace('\r\n', '\n')
        target_script_norm = target_script.replace('\r\n', '\n')
        replacement_script_norm = replacement_script.replace('\r\n', '\n')
        
        if target_nav_norm in content_norm:
            content_norm = content_norm.replace(target_nav_norm, replacement_nav_norm)
            print(f"Replaced nav in {fpath}")
        else:
            print(f"Nav target NOT found in {fpath}")
            
        if target_script_norm in content_norm:
            content_norm = content_norm.replace(target_script_norm, replacement_script_norm)
            print(f"Replaced script in {fpath}")
        else:
            print(f"Script target NOT found in {fpath}")
            
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content_norm)

print("Done.")
