import re
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()
content = content.replace('class="section" class="section pb-12 md:pb-24 pt-12"', 'class="section pb-12 md:pb-24 pt-12"')
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
