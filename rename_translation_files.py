import os
import shutil

def rename_files():
    trans_dir = os.path.join("src", "translations")
    folders = ["seo", "navigation", "pages", "reviews", "gallery"]
    langs = ["fr", "en", "en-au", "de", "it", "es", "ru"]
    
    for folder in folders:
        folder_path = os.path.join(trans_dir, folder)
        if not os.path.exists(folder_path):
            continue
            
        for lang in langs:
            old_file = os.path.join(folder_path, f"{lang}.json")
            new_file = os.path.join(folder_path, f"index.{lang}.json")
            
            if os.path.exists(old_file):
                # Rename the file
                shutil.move(old_file, new_file)
                print(f"Renamed: {old_file} -> {new_file}")
                
    print("Renaming translation files complete!")

if __name__ == "__main__":
    rename_files()
