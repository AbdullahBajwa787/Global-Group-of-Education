import urllib.request
import os

images = [
    ('https://globalgroupofeducationportal.com/images/abt-img1.png', 'assets/images/about/abt-img1.png'),
    ('https://globalgroupofeducationportal.com/images/abt-img2.png', 'assets/images/about/abt-img2.png'),
    ('https://globalgroupofeducationportal.com/images/service-bg.jpg', 'assets/images/service-bg.jpg')
]

os.makedirs('assets/images/about', exist_ok=True)
os.makedirs('public/assets/images/about', exist_ok=True)

opener = urllib.request.build_opener()
opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
urllib.request.install_opener(opener)

for url, local_path in images:
    try:
        print(f"Downloading {url} to {local_path}...")
        urllib.request.urlretrieve(url, local_path)
        # copy to public
        pub_path = 'public/' + local_path
        os.makedirs(os.path.dirname(pub_path), exist_ok=True)
        with open(local_path, 'rb') as f_in, open(pub_path, 'wb') as f_out:
            f_out.write(f_in.read())
        print(f"Saved {local_path} ({os.path.getsize(local_path)} bytes)")
    except Exception as e:
        print(f"Error downloading {url}: {e}")
