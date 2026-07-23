import re

with open('src/admin/config.yml', 'r', encoding='utf-8') as f:
    content = f.read()

new_content = re.sub(r'file:\s*"([^"]+?)(?<!\.json)"', r'file: "\1.json"', content)

with open('src/admin/config.yml', 'w', encoding='utf-8') as f:
    f.write(new_content)
