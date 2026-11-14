from bs4 import BeautifulSoup

with open(r'g:\dien lanh ha noi\index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

for tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
    elems = soup.find_all(tag)
    print(f'{tag}: {len(elems)} elements')
    for el in elems[:10]:
        cls = el.get('class', [])
        txt = ' '.join(el.get_text().split())[:60]
        print(f'  <{tag} class="{" ".join(cls)}">: {txt}')
