import os
import json

locales = ['fr', 'en', 'en-au', 'de', 'it', 'es', 'ru']
folders = ['seo', 'navigation', 'pages']
base_dir = 'src/translations'

for folder in folders:
    folder_path = os.path.join(base_dir, folder)
    if not os.path.exists(folder_path):
        continue
    
    # Find all base names (e.g., accueil)
    files = os.listdir(folder_path)
    base_names = set()
    for f in files:
        if f.endswith('.json') and not f.endswith('.json.fr.json'):
            parts = f.split('.')
            if len(parts) >= 3 and parts[-2] in locales:
                base_names.add(parts[0])
                
    for base in base_names:
        merged_data = {}
        for loc in locales:
            file_path = os.path.join(folder_path, f"{base}.{loc}.json")
            if os.path.exists(file_path):
                with open(file_path, 'r', encoding='utf-8') as f:
                    try:
                        merged_data[loc] = json.load(f)
                    except Exception as e:
                        print(f"Error loading {file_path}: {e}")
        
        # Save merged file
        out_path = os.path.join(folder_path, f"{base}.json")
        with open(out_path, 'w', encoding='utf-8') as f:
            json.dump(merged_data, f, ensure_ascii=False, indent=2)
        print(f"Merged {base} into {out_path}")
        
        # Delete old locale files
        for loc in locales:
            file_path = os.path.join(folder_path, f"{base}.{loc}.json")
            if os.path.exists(file_path):
                os.remove(file_path)
