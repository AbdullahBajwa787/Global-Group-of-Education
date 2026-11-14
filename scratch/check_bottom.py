with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('<!-- Start Preloader -->')
print("Index of Start Preloader:", idx)
if idx != -1:
    print("Length from Start Preloader to end:", len(text) - idx)
    # Check if there are scripts at the end of the file
    script_idx = text.rfind('<script')
    print("Last script block starts at:", script_idx)
    print(text[script_idx:])
