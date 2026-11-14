with open(r'g:\dien lanh ha noi\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
sections = re.findall(r'<section[^>]*id="([^"]*)"[^>]*>', text)
print('Sections:', sections)

# Search for điều hòa, tủ lạnh, bình nóng lạnh
for term in ['điều hòa', 'tủ lạnh', 'bình nóng lạnh']:
    idx = text.lower().find(term)
    if idx != -1:
        print(f'Term "{term}" found around: {text[max(0, idx-50):min(len(text), idx+100)].strip()}')
