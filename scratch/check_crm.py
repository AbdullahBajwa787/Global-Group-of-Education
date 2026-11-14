import urllib.request
import re

url = 'https://globalgroupofeducationportal.com/'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        final_url = resp.geturl()
        print('Final URL:', final_url)
        html = resp.read().decode('utf-8', errors='ignore')
        print('HTML length:', len(html))
        
        # Save html to scratch for examination
        with open('scratch/crm_page.html', 'w', encoding='utf-8') as f:
            f.write(html)
            
        videos = re.findall(r'<video[^>]*>.*?</video>', html, re.DOTALL | re.IGNORECASE)
        print('Videos count:', len(videos))
        for v in videos:
            print('VIDEO TAG:', v[:300])
            
        mp4s = re.findall(r'https?://[^\s"\'<>]+\.mp4[^\s"\'<>]*', html, re.IGNORECASE)
        print('Direct MP4 links:', set(mp4s))
        
        # Also find any background videos or video sources
        sources = re.findall(r'<source[^>]+>', html, re.IGNORECASE)
        print('Sources:', sources)
        
        # Also check stylesheets or assets
        scripts = re.findall(r'<script[^>]+src=["\']([^"\']+)["\']', html, re.IGNORECASE)
        print('Scripts:', scripts[:5])

except Exception as e:
    print('Error:', e)
