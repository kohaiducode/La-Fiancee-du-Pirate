import os
import json
import shutil
import re
import unicodedata

def load_json(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def render_template(template_str, variables):
    def replace_var(match):
        key = match.group(1).strip()
        parts = key.split('.')
        
        # Traverse dictionary
        val = variables
        for part in parts:
            if isinstance(val, dict) and part in val:
                val = val[part]
            else:
                return match.group(0)  # Keep placeholder if key not found
        
        return str(val)
        
    # Pattern to match {{key}} or {{category.key}}
    pattern = re.compile(r'\{\{([^}]+)\}\}')
    return pattern.sub(replace_var, template_str)

def sanitize_name(name):
    name = name.lower()
    name = name.replace(" & ", "_and_")
    name = name.replace("&", "_and_")
    name = name.replace(" ", "_")
    name = name.replace("-", "_")
    name = "".join(
        c for c in unicodedata.normalize('NFD', name)
        if unicodedata.category(c) != 'Mn'
    )
    return name

def get_optimized_image_path(raw_path):
    if not raw_path:
        return ""
    raw_path = raw_path.replace('\\', '/')
    raw_path = raw_path.lstrip('/')
    
    if raw_path.startswith('Photos/'):
        parts = raw_path.split('/')
        sanitized_parts = [sanitize_name(p) for p in parts[1:-1]]
        filename = parts[-1]
        name_no_ext, _ = os.path.splitext(filename)
        sanitized_filename = f"{sanitize_name(name_no_ext)}.webp"
        
        final_parts = ['assets', 'images'] + sanitized_parts + [sanitized_filename]
        return '/'.join(final_parts)
    return raw_path

def compile_site():
    print("Compiling La Fiancee du Pirate website...")
    
    # Paths
    src_dir = "src"
    dist_dir = "docs"
    templates_dir = os.path.join(src_dir, "templates")
    pages_dir = os.path.join(src_dir, "pages")
    translations_dir = os.path.join(src_dir, "translations")
    
    # 1. Clean and recreate dist directory
    if os.path.exists(dist_dir):
        # Keep optimized images in dist/assets/images if they exist to avoid re-optimization delays,
        # but clean the rest. Or simply copy src/assets/images since optimize_images.py wrote there!
        shutil.rmtree(dist_dir)
    os.makedirs(dist_dir, exist_ok=True)
    
    # 2. Copy assets (CSS, JS, optimized images)
    src_assets = os.path.join(src_dir, "assets")
    dist_assets = os.path.join(dist_dir, "assets")
    if os.path.exists(src_assets):
        shutil.copytree(src_assets, dist_assets)
        print("Assets copied successfully.")
    
    # 3. Load layout files
    layout_tpl = ""
    with open(os.path.join(templates_dir, "layout.html"), 'r', encoding='utf-8') as f:
        layout_tpl = f.read()
        
    head_tpl = ""
    with open(os.path.join(templates_dir, "head.html"), 'r', encoding='utf-8') as f:
        head_tpl = f.read()
        
    header_tpl = ""
    with open(os.path.join(templates_dir, "header.html"), 'r', encoding='utf-8') as f:
        header_tpl = f.read()
        
    footer_tpl = ""
    with open(os.path.join(templates_dir, "footer.html"), 'r', encoding='utf-8') as f:
        footer_tpl = f.read()
        
    booking_tpl = ""
    with open(os.path.join(templates_dir, "booking-bar.html"), 'r', encoding='utf-8') as f:
        booking_tpl = f.read()

    # Get all pages
    pages = [f for f in os.listdir(pages_dir) if f.endswith('.html')]
    
    # Get all translation files (read from seo/ subfolder)
    seo_dir = os.path.join(translations_dir, "seo")
    translation_files = [f for f in os.listdir(seo_dir) if f.endswith('.json')]
    languages = [os.path.splitext(f)[0] for f in translation_files]
    
    # Language code mapping for Amenitiz URLs
    amenitiz_lang_map = {
        "fr": "fr",
        "en": "en",
        "en-au": "en",
        "de": "de",
        "it": "it",
        "es": "es",
        "ru": "ru"
    }
    
    # 4. Process each language
    for lang in languages:
        # Load language translation files from subfolders and merge them
        lang_data = {}
        for folder in ["seo", "navigation", "pages", "reviews"]:
            folder_file = os.path.join(translations_dir, folder, f"{lang}.json")
            if os.path.exists(folder_file):
                lang_data.update(load_json(folder_file))
                
        lang_upper = lang.upper()
        
        # Create language folder
        lang_dist_dir = os.path.join(dist_dir, lang)
        os.makedirs(lang_dist_dir, exist_ok=True)
        
        # Determine booking URL
        amenitiz_code = amenitiz_lang_map.get(lang, "en")
        booking_url = f"https://la-fiancee-du-pirate.amenitiz.io/{amenitiz_code}/booking/room"
        
        print(f"Processing language: {lang} (Amenitiz code: {amenitiz_code})")
        
        # Build TripAdvisor reviews slider HTML for this language
        reviews_html = ""
        reviews_list = lang_data.get("reviews", {}).get("items", [])
        for i, rev in enumerate(reviews_list):
            active_class = " active" if i == 0 else ""
            rating_stars = ""
            for _ in range(rev.get("rating", 5)):
                rating_stars += '<span class="ta-circle filled"></span>'
            for _ in range(5 - rev.get("rating", 5)):
                rating_stars += '<span class="ta-circle"></span>'
                
            reviews_html += f"""
            <div class="review-slide{active_class}" data-index="{i}">
                <div class="review-card">
                    <div class="review-rating">
                        {rating_stars}
                    </div>
                    <h4 class="review-title">"{rev.get('title')}"</h4>
                    <p class="review-text">"{rev.get('text')}"</p>
                    <div class="review-author">
                        <strong>{rev.get('author')}</strong> &ndash; <span>{rev.get('date')}</span>
                    </div>
                </div>
            </div>
            """
        
        # Build Photo Gallery Grid HTML for this language
        gallery_html = ""
        gallery_data = load_json(os.path.join(translations_dir, "gallery", f"{lang}.json"))
        gallery_items = gallery_data.get("items", [])
        for item in gallery_items:
            img_path = get_optimized_image_path(item.get("image", ""))
            category = item.get("category", "")
            alt = item.get("alt", "")
            
            gallery_html += f"""
            <div class="gallery-item" data-category="{category}">
                <img src="{{{{path_prefix}}}}{img_path}" alt="{alt}" class="gallery-img" loading="lazy">
                <div class="gallery-overlay">
                    <i class="fa-solid fa-maximize"></i>
                </div>
            </div>"""
            
        # Compile each page template
        for page in pages:
            page_name_no_ext = os.path.splitext(page)[0]
            
            # Map page metadata
            meta_title = ""
            meta_desc = ""
            if page_name_no_ext == "index":
                meta_title = lang_data["seo"]["home_title"]
                meta_desc = lang_data["seo"]["home_desc"]
            elif page_name_no_ext == "chambres":
                meta_title = lang_data["seo"]["rooms_title"]
                meta_desc = lang_data["seo"]["rooms_desc"]
            elif page_name_no_ext == "services":
                meta_title = lang_data["seo"]["services_title"]
                meta_desc = lang_data["seo"]["services_desc"]
            elif page_name_no_ext == "galerie":
                meta_title = lang_data["seo"]["gallery_title"]
                meta_desc = lang_data["seo"]["gallery_desc"]
            elif page_name_no_ext == "contact":
                meta_title = lang_data["seo"]["contact_title"]
                meta_desc = lang_data["seo"]["contact_desc"]
                
            # Render layout parts with page details
            is_index = (page_name_no_ext == "index")
            path_prefix = "../" if is_index else "../../"
            page_path = "" if is_index else f"{page_name_no_ext}/"
            
            context = {
                "lang": lang,
                "lang_upper": lang_upper,
                "path_prefix": path_prefix,
                "page_path": page_path,
                "booking_url": booking_url,
                "page_filename": page,
                "meta_title": meta_title,
                "meta_desc": meta_desc,
                
                # Active links
                "active_home": "active" if page_name_no_ext == "index" else "",
                "active_rooms": "active" if page_name_no_ext == "chambres" else "",
                "active_services": "active" if page_name_no_ext == "services" else "",
                "active_gallery": "active" if page_name_no_ext == "galerie" else "",
                "active_contact": "active" if page_name_no_ext == "contact" else "",
                
                # Active lang dropdown highlight
                "active_lang_fr": "active" if lang == "fr" else "",
                "active_lang_en": "active" if lang == "en" else "",
                "active_lang_de": "active" if lang == "de" else "",
                "active_lang_it": "active" if lang == "it" else "",
                "active_lang_es": "active" if lang == "es" else "",
                "active_lang_ru": "active" if lang == "ru" else "",
                "active_lang_en_au": "active" if lang == "en-au" else ""
            }
            
            # Combine language translation dictionary
            full_vars = {**lang_data, **context}
            
            # Render template parts
            rendered_head = render_template(head_tpl, full_vars)
            rendered_header = render_template(header_tpl, full_vars)
            rendered_booking = render_template(booking_tpl, full_vars)
            rendered_footer = render_template(footer_tpl, full_vars)
            
            # Load page specific content body
            page_content = ""
            with open(os.path.join(pages_dir, page), 'r', encoding='utf-8') as f:
                page_content = f.read()
                
            # Inject testimonial slides if homepage
            if page_name_no_ext == "index":
                page_content = page_content.replace("{{reviews_slides_placeholder}}", reviews_html)
            elif page_name_no_ext == "galerie":
                page_content = page_content.replace("{{gallery_grid_html}}", gallery_html)
                
            rendered_page_content = render_template(page_content, full_vars)
            
            # Assemble everything in layout
            final_html = layout_tpl
            final_html = final_html.replace("{{head}}", rendered_head)
            final_html = final_html.replace("{{header}}", rendered_header)
            final_html = final_html.replace("{{content}}", rendered_page_content)
            final_html = final_html.replace("{{booking_bar}}", rendered_booking)
            final_html = final_html.replace("{{footer}}", rendered_footer)
            
            # Final variable clean up
            final_html = render_template(final_html, full_vars)
            
            # Save compiled file
            if is_index:
                dest_file_path = os.path.join(lang_dist_dir, "index.html")
            else:
                page_dir = os.path.join(lang_dist_dir, page_name_no_ext)
                os.makedirs(page_dir, exist_ok=True)
                dest_file_path = os.path.join(page_dir, "index.html")
                
            with open(dest_file_path, 'w', encoding='utf-8') as f:
                f.write(final_html)
                
    # 5. Create root redirection index.html
    root_index_content = """<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>La Fiancée du Pirate</title>
    <script>
        // Detection of user browser language
        var userLang = navigator.language || navigator.userLanguage;
        userLang = userLang.toLowerCase();
        
        var targetLang = 'fr'; // Default language
        
        if (userLang.startsWith('en-au')) {
            targetLang = 'en-au';
        } else if (userLang.startsWith('en')) {
            targetLang = 'en';
        } else if (userLang.startsWith('de')) {
            targetLang = 'de';
        } else if (userLang.startsWith('it')) {
            targetLang = 'it';
        } else if (userLang.startsWith('es')) {
            targetLang = 'es';
        } else if (userLang.startsWith('ru')) {
            targetLang = 'ru';
        } else if (userLang.startsWith('fr')) {
            targetLang = 'fr';
        }
        
        window.location.replace('./' + targetLang + '/');
    </script>
</head>
<body>
    <p>Redirecting to <a href="./fr/">La Fiancée du Pirate</a>...</p>
</body>
</html>
"""
    with open(os.path.join(dist_dir, "index.html"), 'w', encoding='utf-8') as f:
        f.write(root_index_content)
        
    print("Compilation completed successfully!")

if __name__ == "__main__":
    compile_site()
