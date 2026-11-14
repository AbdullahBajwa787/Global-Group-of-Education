with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('END GGE MODERN MOCKUP HOMEPAGE')
if idx != -1:
    print("Found END GGE MODERN MOCKUP HOMEPAGE at index", idx)
    print("Following 1000 characters:")
    print(text[idx:idx+1000])
else:
    print("END GGE MODERN MOCKUP HOMEPAGE not found!")
