import json
import re
from html.parser import HTMLParser

with open('index.html', encoding='utf-8') as f:
    content = f.read()

parser = HTMLParser()
parser.feed(content)
print("HTML Parse: OK!")

match = re.search(r'<script type="application/ld\+json">(.*?)</script>', content, re.DOTALL)
if match:
    data = json.loads(match.group(1))
    print(f"Schema JSON-LD Parse: OK! -> Type: {data['@type']}, Name: {data['name']}")
else:
    print("No JSON-LD found!")
