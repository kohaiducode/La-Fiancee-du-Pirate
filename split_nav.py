import json
import os

with open('src/translations/navigation/index.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

header_data = {}
footer_data = {}

for lang, content in data.items():
    header_data[lang] = {
        "title": content.get("title", ""),
        "nav": content.get("nav", {}),
        "hero": content.get("hero", {}),
        "booking_bar": content.get("booking_bar", {})
    }
    footer_data[lang] = {
        "title": content.get("title", ""),
        "footer": content.get("footer", {})
    }

with open('src/translations/navigation/header.json', 'w', encoding='utf-8') as f:
    json.dump(header_data, f, ensure_ascii=False, indent=2)

with open('src/translations/navigation/footer.json', 'w', encoding='utf-8') as f:
    json.dump(footer_data, f, ensure_ascii=False, indent=2)

# Remove the old file
os.remove('src/translations/navigation/index.json')
