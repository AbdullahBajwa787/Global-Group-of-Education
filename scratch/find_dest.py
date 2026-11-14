with open('index.html', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f, 1):
        if 'Top Study Destinations' in line or 'study destinations' in line.lower() or 'gge-dest' in line.lower():
            print(f'{i}: {line.strip()[:100]}')
