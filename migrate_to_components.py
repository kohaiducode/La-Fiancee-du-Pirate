import os
import json
import shutil

def recurse_merge(path_objs):
    first_val = next(iter(path_objs.values()))
    
    if isinstance(first_val, dict):
        res = {}
        keys = set()
        for obj in path_objs.values():
            if isinstance(obj, dict):
                keys.update(obj.keys())
        for k in keys:
            sub_objs = {}
            for lang, obj in path_objs.items():
                if isinstance(obj, dict) and k in obj:
                    sub_objs[lang] = obj[k]
            res[k] = recurse_merge(sub_objs)
        return res
    elif isinstance(first_val, list):
        res_list = []
        min_len = min(len(obj) for obj in path_objs.values() if isinstance(obj, list))
        for idx in range(min_len):
            sub_objs = {}
            for lang, obj in path_objs.items():
                sub_objs[lang] = obj[idx]
            res_list.append(recurse_merge(sub_objs))
        return res_list
    else:
        # Leaf value: return a dictionary with language keys
        return path_objs

def migrate():
    trans_dir = os.path.join("src", "translations")
    data_dir = os.path.join("src", "data")
    os.makedirs(data_dir, exist_ok=True)
    
    langs = ["fr", "en", "en-au", "de", "it", "es", "ru"]
    folders = ["seo", "navigation", "pages", "reviews"]
    
    # 1. Load and merge all translations for each language
    merged_by_lang = {}
    for lang in langs:
        lang_data = {}
        for folder in folders:
            path = os.path.join(trans_dir, folder, f"{lang}.json")
            if os.path.exists(path):
                with open(path, 'r', encoding='utf-8') as f:
                    lang_data.update(json.load(f))
        merged_by_lang[lang] = lang_data
        
    # 2. Merge them into a single structure
    full_merged = recurse_merge(merged_by_lang)
    
    # 3. Create components
    
    # Global Component
    global_data = {
        "seo": full_merged.get("seo", {}),
        "nav": full_merged.get("nav", {}),
        "booking_bar": full_merged.get("booking_bar", {}),
        "reviews": full_merged.get("reviews", {}),
        "footer": full_merged.get("footer", {})
    }
    
    # Accueil Component
    accueil_data = {
        "hero": full_merged.get("hero", {}),
        "accueil": full_merged.get("accueil", {})
    }
    # Add card images
    accueil_data["accueil"]["card_view_image"] = "Photos/Accueil/Vue Panoramique/469280682_18093389905496419_2802448118524091836_n.jpg"
    accueil_data["accueil"]["card_pool_image"] = "Photos/Accueil/Piscine & Jardin/473058781_1208091584049818_5863954410700728121_n.jpg"
    accueil_data["accueil"]["card_breakfast_image"] = "Photos/Accueil/Petit-déjeuner Face Mer/94744280_2994539400612314_2403694604873367552_n.jpg"
    accueil_data["accueil"]["card_location_image"] = "Photos/Accueil/Emplacement Idéal/473557294_1209966607195649_1255708061335853651_n.jpg"
    
    # Chambres Component
    rooms_data = {
        "rooms": full_merged.get("rooms", {})
    }
    # Add room images
    rooms_data["rooms"]["garden_image"] = "Photos/Accueil/snacks_by_the_pool.jpg"
    rooms_data["rooms"]["mer_image"] = "Photos/Accueil/room_with_view.jpg"
    rooms_data["rooms"]["pavillons_image"] = "Photos/Accueil/jacuzzi_and_pool.jpg"
    
    # Services Component
    services_data = {
        "services": full_merged.get("services", {})
    }
    
    # 4. Save component JSON files
    with open(os.path.join(data_dir, "global.json"), 'w', encoding='utf-8') as f:
        json.dump(global_data, f, ensure_ascii=False, indent=2)
        
    with open(os.path.join(data_dir, "accueil.json"), 'w', encoding='utf-8') as f:
        json.dump(accueil_data, f, ensure_ascii=False, indent=2)
        
    with open(os.path.join(data_dir, "chambres.json"), 'w', encoding='utf-8') as f:
        json.dump(rooms_data, f, ensure_ascii=False, indent=2)
        
    with open(os.path.join(data_dir, "services.json"), 'w', encoding='utf-8') as f:
        json.dump(services_data, f, ensure_ascii=False, indent=2)
        
    # 5. Delete src/translations folder (leaving src/translations/gallery if it existed, but it is deleted)
    if os.path.exists(trans_dir):
        shutil.rmtree(trans_dir)
        
    print("Migration to component JSON files complete!")

if __name__ == "__main__":
    migrate()
