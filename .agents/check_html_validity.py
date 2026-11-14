from bs4 import BeautifulSoup

with open(r'g:\dien lanh ha noi\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

soup = BeautifulSoup(content, 'html.parser')

hero_tags = soup.find('div', class_='hero-tags')
if hero_tags:
    print('Found .hero-tags with items:')
    for item in hero_tags.find_all('div', class_='hero-tag'):
        label = item.find('span', class_='hero-tag__label').get_text(strip=True)
        has_svg = item.find('svg') is not None
        print(f' - {label}: has_svg={has_svg}')
else:
    print('ERROR: .hero-tags not found!')
