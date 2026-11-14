import urllib.request

urls = [
    'https://www.globalgroupofeducation.com/study-in-uk',
    'https://www.globalgroupofeducation.com/study-in-usa',
    'https://www.globalgroupofeducation.com/study-in-canada',
    'https://www.globalgroupofeducation.com/study-in-australia',
    'https://www.globalgroupofeducation.com/study-in-hungary',
    'https://www.globalgroupofeducation.com/study-in-uae',
    'https://www.globalgroupofeducation.com/study-in-europe',
    'https://www.globalgroupofeducation.com/study-in-new-zealand'
]
for u in urls:
    try:
        req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'})
        res = urllib.request.urlopen(req, timeout=5)
        print(res.getcode(), u)
    except Exception as e:
        print(e, u)
