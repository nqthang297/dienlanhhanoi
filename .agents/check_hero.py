with open(r'g:\dien lanh ha noi\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('hero-section')
end = text.find('</section>', start)
print(text[start-20:end+12])
