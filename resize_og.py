from PIL import Image
import os

img_path = r"c:\Users\81704\Desktop\Code\Sites\La-Fiancee-du-Pirate\src\assets\images\og\image_open_graph.webp"
if os.path.exists(img_path):
    with Image.open(img_path) as img:
        img_resized = img.resize((1200, 630), Image.Resampling.LANCZOS)
        img_resized.save(img_path, format="WEBP", quality=90)
        print("Image successfully resized to 1200x630.")
else:
    print("File not found.")
