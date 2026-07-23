import os
from PIL import Image

def optimize_images():
    src_photos_dir = "Photos"
    dest_images_dir = os.path.join("src", "assets", "images")
    
    print("Starting image optimization...")
    
    # Ensure destination directories exist
    os.makedirs(dest_images_dir, exist_ok=True)
    
    # Process Photos directory
    for root, dirs, files in os.walk(src_photos_dir):
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext in ['.jpg', '.jpeg', '.png', '.webp']:
                src_path = os.path.join(root, file)
                
                # Determine relative structure to preserve in assets
                rel_path = os.path.relpath(root, src_photos_dir)
                dest_sub_dir = os.path.join(dest_images_dir, rel_path.lower())
                os.makedirs(dest_sub_dir, exist_ok=True)
                
                filename_no_ext = os.path.splitext(file)[0].lower().replace(" ", "_")
                dest_path = os.path.join(dest_sub_dir, f"{filename_no_ext}.webp")
                
                try:
                    with Image.open(src_path) as img:
                        # Convert RGBA/P to RGB if converting to WebP (unless transparent, but webp supports transparency)
                        if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
                            # Keep transparent mode
                            pass
                        else:
                            img = img.convert('RGB')
                        
                        # Resize if width is larger than 1920px
                        max_width = 1920
                        if img.width > max_width:
                            ratio = max_width / float(img.width)
                            height = int(float(img.height) * float(ratio))
                            img = img.resize((max_width, height), Image.Resampling.LANCZOS)
                            print(f"Resized {file} to 1920x{height}")
                        
                        img.save(dest_path, "WEBP", quality=85)
                        print(f"Optimized and saved: {src_path} -> {dest_path}")
                except Exception as e:
                    print(f"Error optimizing {src_path}: {e}")

    # Copy root logo webp if it exists
    root_logo = "logo_pirate-1920w.webp"
    if os.path.exists(root_logo):
        logo_dest_dir = os.path.join(dest_images_dir, "logo")
        os.makedirs(logo_dest_dir, exist_ok=True)
        dest_logo_path = os.path.join(logo_dest_dir, "logo_pirate.webp")
        try:
            with Image.open(root_logo) as img:
                img.save(dest_logo_path, "WEBP", quality=90)
                print(f"Copied and saved logo to: {dest_logo_path}")
        except Exception as e:
            print(f"Error processing root logo: {e}")

if __name__ == "__main__":
    optimize_images()
