import os
import json
import shutil

def migrate():
    trans_dir = os.path.join("src", "translations", "gallery")
    data_dir = os.path.join("src", "data")
    os.makedirs(data_dir, exist_ok=True)
    
    langs = ["fr", "en", "en-au", "de", "it", "es", "ru"]
    
    # Load all languages JSONs
    data = {}
    for l in langs:
        path = os.path.join(trans_dir, f"{l}.json")
        with open(path, 'r', encoding='utf-8') as f:
            data[l] = json.load(f)
            
    # Combine lists
    items = []
    fr_items = data['fr']['items']
    for i in range(len(fr_items)):
        image = fr_items[i]['image']
        category = fr_items[i]['category']
        
        # Build multi-language alt object
        new_item = {
            "image": image,
            "category": category
        }
        for l in langs:
            # Map e.g. "en-au" to "alt_en_au"
            key = f"alt_{l.replace('-', '_')}"
            new_item[key] = data[l]['items'][i]['alt']
            
        items.append(new_item)
        
    # Write merged JSON
    dest_path = os.path.join(data_dir, "gallery.json")
    with open(dest_path, 'w', encoding='utf-8') as f:
        json.dump({"items": items}, f, ensure_ascii=False, indent=2)
        
    # Delete temporary trans/gallery dir
    if os.path.exists(trans_dir):
        shutil.rmtree(trans_dir)
        
    print("Gallery successfully migrated to src/data/gallery.json!")

if __name__ == "__main__":
    migrate()
