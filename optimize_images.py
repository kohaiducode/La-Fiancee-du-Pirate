import os
import unicodedata
from PIL import Image

def sanitize_name(name):
    name = name.lower()
    name = name.replace(" & ", "_and_")
    name = name.replace("&", "_and_")
    name = name.replace(" ", "_")
    name = name.replace("-", "_")
    # Normalize and remove accents (unicode Category 'Mn')
    name = "".join(
        c for c in unicodedata.normalize('NFD', name)
        if unicodedata.category(c) != 'Mn'
    )
    return name

def optimize_images():
    src_photos_dir = "Photos"
    dest_images_dir = os.path.join("src", "assets", "images")
    
    print("Starting image optimization with folder sanitization...")
    
    # Ensure destination directories exist
    os.makedirs(dest_images_dir, exist_ok=True)
    
    # Process Photos directory
    for root, dirs, files in os.walk(src_photos_dir):
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext in ['.jpg', '.jpeg', '.png', '.webp']:
                src_path = os.path.join(root, file)
                
                # Sanitize relative folder path
                rel_path = os.path.relpath(root, src_photos_dir)
                parts = rel_path.split(os.sep)
                sanitized_parts = [sanitize_name(p) for p in parts if p and p != '.']
                
                dest_sub_dir = os.path.join(dest_images_dir, *sanitized_parts)
                os.makedirs(dest_sub_dir, exist_ok=True)
                
                filename_no_ext = sanitize_name(os.path.splitext(file)[0])
                dest_path = os.path.join(dest_sub_dir, f"{filename_no_ext}.webp")
                
                try:
                    with Image.open(src_path) as img:
                        # Convert to RGB if necessary
                        if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
                            pass
                        else:
                            img = img.convert('RGB')
                        
                        # Resize if wider than 1920px
                        max_width = 1920
                        if img.width > max_width:
                            ratio = max_width / float(img.width)
                            height = int(float(img.height) * float(ratio))
                            img = img.resize((max_width, height), Image.Resampling.LANCZOS)
                            print(f"Resized image to 1920px width")
                        
                        img.save(dest_path, "WEBP", quality=85)
                        print(f"Optimized and saved: {dest_path}")
                except Exception as e:
                    print(f"Error optimizing a photo file.")

    # Process root logo
    root_logo = "logo_pirate-1920w.webp"
    if os.path.exists(root_logo):
        logo_dest_dir = os.path.join(dest_images_dir, "logo")
        os.makedirs(logo_dest_dir, exist_ok=True)
        dest_logo_path = os.path.join(logo_dest_dir, "logo_pirate.webp")
        try:
            with Image.open(root_logo) as img:
                img.save(dest_logo_path, "WEBP", quality=90)
                print(f"Saved root logo to: {dest_logo_path}")
        except Exception as e:
            print("Error processing root logo.")

if __name__ == "__main__":
    optimize_images()
