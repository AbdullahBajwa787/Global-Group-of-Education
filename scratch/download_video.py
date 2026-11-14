import urllib.request
import os

url = 'https://globalgroupofeducationportal.com/images/video.mp4'
dest = 'assets/videos/crm_video.mp4'
os.makedirs('assets/videos', exist_ok=True)
print('Downloading from', url)

opener = urllib.request.build_opener()
opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)')]
urllib.request.install_opener(opener)

try:
    urllib.request.urlretrieve(url, dest)
    print('SUCCESS! File saved to', dest, 'Size:', os.path.getsize(dest))
    # Also copy to public/assets/videos/
    os.makedirs('public/assets/videos', exist_ok=True)
    with open(dest, 'rb') as f_in, open('public/assets/videos/crm_video.mp4', 'wb') as f_out:
        f_out.write(f_in.read())
    print('Copied to public/assets/videos/crm_video.mp4')
except Exception as e:
    print('Error:', e)
