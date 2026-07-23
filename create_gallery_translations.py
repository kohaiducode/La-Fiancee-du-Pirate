import os
import json

def init_gallery():
    gallery_dir = os.path.join("src", "translations", "gallery")
    os.makedirs(gallery_dir, exist_ok=True)
    
    # 7 Languages display titles
    titles_map = {
        "fr": "Français (FR)",
        "en": "English (EN)",
        "en-au": "English (AU)",
        "de": "Deutsch (DE)",
        "it": "Italiano (IT)",
        "es": "Español (ES)",
        "ru": "Русский (RU)"
    }
    
    # Translated Alt SEO texts for the 8 default images
    alt_texts = {
        "fr": [
            "Vue panoramique de l'hôtel La Fiancée du Pirate",
            "Piscine chauffée et bâtiment de l'hôtel",
            "Transats et parasols au bord de la piscine",
            "Espace détente jacuzzi et piscine avec vue mer",
            "Snacks et rafraîchissements servis au bord de la piscine",
            "Chambre confortable avec balcon et vue panoramique mer",
            "Salle de petit-déjeuner lumineuse avec terrasse extérieure",
            "Buffet petit-déjeuner copieux face à la mer"
        ],
        "en": [
            "Panoramic view of La Fiancée du Pirate hotel",
            "Heated pool and hotel building",
            "Sun loungers and umbrellas by the pool",
            "Relaxation area jacuzzi and pool with sea view",
            "Snacks and refreshments served by the pool",
            "Comfortable room with balcony and panoramic sea view",
            "Bright breakfast room with outdoor terrace",
            "Generous breakfast buffet facing the sea"
        ],
        "en-au": [
            "Panoramic view of La Fiancée du Pirate hotel",
            "Heated pool and hotel building",
            "Sun loungers and umbrellas by the pool",
            "Relaxation area jacuzzi and pool with sea view",
            "Snacks and refreshments served by the pool",
            "Comfortable room with balcony and panoramic sea view",
            "Bright breakfast room with outdoor terrace",
            "Generous breakfast buffet facing the sea"
        ],
        "de": [
            "Panoramablick auf das Hotel La Fiancée du Pirate",
            "Beheizter Pool und Hotelgebäude",
            "Sonnenliegen und Sonnenschirme am Pool",
            "Entspannungsbereich Jacuzzi und Pool mit Meerblick",
            "Snacks und Erfrischungen am Pool serviert",
            "Komfortables Zimmer mit Balkon und Panoramameerblick",
            "Heller Frühstücksraum mit Außenterrasse",
            "Reichhaltiges Frühstücksbuffet mit Blick auf das Meer"
        ],
        "it": [
            "Vista panoramica dell'hotel La Fiancée du Pirate",
            "Piscina riscaldata e edificio dell'hotel",
            "Lettini e ombrelloni a bordo piscina",
            "Area relax jacuzzi e piscina con vista mare",
            "Snack e rinfreschi serviti a bordo piscina",
            "Camera confortevole con balcone e vista panoramica sul mare",
            "Luminosa sala colazione con terrazza esterna",
            "Ricca colazione a buffet di fronte al mare"
        ],
        "es": [
            "Vista panorámica del hotel La Fiancée du Pirate",
            "Piscina climatizada y edificio del hotel" ,
            "Tumbonas y sombrillas junto a la piscina",
            "Zona de relajación jacuzzi y piscina con vistas al mar",
            "Snacks y refrescos servidos junto a la piscina",
            "Habitación confortable con balcón y vistas panorámicas al mar",
            "Luminoso salón de desayuno con terraza exterior",
            "Abundante desayuno buffet frente al mar"
        ],
        "ru": [
            "Панорамный вид на отель La Fiancée du Pirate",
            "Подогреваемый бассейн и здание отеля",
            "Шезлонги и зонтики у бассейна",
            "Зона отдыха с джакузи и бассейном с видом на море",
            "Закуски и прохладительные напитки у бассейна",
            "Комфортабельный номер с балконом и панорамным видом на море",
            "Светлый зал для завтраков с открытой террасой",
            "Обильный завтрак 'шведский стол' с видом на море"
        ]
    }
    
    # 8 Default images in Photos/Galerie/
    default_items = [
        {"image": "Photos/Galerie/hotel_view.jpg", "category": "view"},
        {"image": "Photos/Galerie/pool_and_hotel.jpg", "category": "pool"},
        {"image": "Photos/Galerie/by_the_pool.jpg", "category": "pool"},
        {"image": "Photos/Galerie/jacuzzi_and_pool.jpg", "category": "pool"},
        {"image": "Photos/Galerie/snacks_by_the_pool.jpg", "category": "pool"},
        {"image": "Photos/Galerie/room_with_view.jpg", "category": "rooms"},
        {"image": "Photos/Galerie/dinner_room.jpg", "category": "breakfast"},
        {"image": "Photos/Galerie/breakfast.jpg", "category": "breakfast"}
    ]
    
    for lang, title in titles_map.items():
        lang_items = []
        for idx, item in enumerate(default_items):
            lang_items.append({
                "image": item["image"],
                "category": item["category"],
                "alt": alt_texts[lang][idx]
            })
            
        data = {
            "title": title,
            "items": lang_items
        }
        
        filepath = os.path.join(gallery_dir, f"{lang}.json")
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Created gallery config for {lang}")

if __name__ == "__main__":
    init_gallery()
