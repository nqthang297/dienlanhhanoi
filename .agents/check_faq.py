import re
with open(r'g:\dien lanh ha noi\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.findall(r'<([^ >]+)[^>]*class="[^"]*faq-item__question[^"]*"', text)
print('Tags for faq-item__question:', m)
