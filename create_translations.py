import os
import json

def create_translations():
    translations_dir = os.path.join("src", "translations")
    os.makedirs(translations_dir, exist_ok=True)
    
    # ------------------ FRENCH (fr) ------------------
    fr = {
        "nav": {
            "home": "Accueil",
            "rooms": "Chambres",
            "services": "Services & Activités",
            "gallery": "Galerie",
            "contact": "Contact",
            "book": "Réserver"
        },
        "hero": {
            "title": "Une parenthèse suspendue sur la Côte d'Azur",
            "subtitle": "Boutique-Hôtel de charme avec vue panoramique sur la rade de Villefranche-sur-Mer",
            "cta": "Réserver une chambre"
        },
        "booking_bar": {
            "check_in": "Arrivée",
            "check_out": "Départ",
            "guests": "Voyageurs",
            "search": "Disponibilité"
        },
        "accueil": {
            "intro_title": "Bienvenue à La Fiancée du Pirate",
            "intro_text": "Niché sur la moyenne corniche entre Nice et Monaco, notre boutique-hôtel intimiste et unique de 15 chambres vous offre un cadre exceptionnel et une vue panoramique imprenable sur la mer Méditerranée.",
            "intro_subtext": "Toute l'équipe se tient à votre entière disposition pour vous faire vivre un séjour inoubliable, comme à la maison, ou presque, mais à l'hôtel !",
            "card_view_title": "Vue Panoramique",
            "card_view_text": "Admirez la vue spectaculaire sur la rade de Villefranche et Saint-Jean-Cap-Ferrat depuis notre terrasse autour d'un verre.",
            "card_pool_title": "Piscine & Jardin",
            "card_pool_text": "Profitez de notre piscine calme et ensoleillée, détendez-vous dans notre jacuzzi ou dans les salons intimes de notre grand jardin.",
            "card_breakfast_title": "Petit-déjeuner Face Mer",
            "card_breakfast_text": "Un délicieux buffet servi tous les jours de 8h30 à 10h30 sur notre terrasse panoramique face à la mer.",
            "card_location_title": "Emplacement Idéal",
            "card_location_text": "Situé de manière privilégiée sur la moyenne corniche, avec accès direct par escalier à la vieille ville et aux plages.",
            "explore_rooms_title": "Nos Chambres & Pavillons",
            "explore_rooms_text": "Entièrement rénovées, climatisées et équipées de lits queen ou king-size pour un confort optimal.",
            "myblackcab_title": "Partenaire de transport personnalisé",
            "myblackcab_text": "Pour tous vos déplacements sur la Riviera, contactez directement notre partenaire Myblackcab pour un service de transport privé haut de gamme."
        },
        "rooms": {
            "title": "Nos Chambres & Pavillons",
            "subtitle": "Rénovés pour votre plus grand confort, offrant calme, intimité et élégance.",
            "cta": "Réserver cette chambre",
            "garden_title": "Chambre Côté Jardin",
            "garden_desc": "Ces chambres agréables vous permettent de profiter pleinement du jardin grâce à leur terrasse privative.",
            "garden_details": "Disponibles en version Double, Triple et Familiale, elles disposent d'une terrasse intime donnant sur notre écrin de verdure.",
            "mer_title": "Chambre Vue Mer",
            "mer_desc": "Spacieuses et accueillantes, ces chambres vous offrent une vue panoramique imprenable sur la baie de Villefranche-sur-Mer et le Cap Ferrat.",
            "mer_details": "Disponibles en version Double, Triple ou Quadruple. Réveillez-vous face au bleu de la Méditerranée.",
            "pavillons_title": "Nos Pavillons Privatifs",
            "pavillons_desc": "Séparés du bâtiment principal, nos deux pavillons privatifs offrent un espace unique de liberté et de bien-être.",
            "pavillons_details": "Le Pavillon de la Fiancée ravira les couples en quête de romantisme. Le Pavillon du Pirate séduira les familles par son emplacement privilégié.",
            "amenities_title": "Équipements inclus",
            "specs": {
                "size": "Superficie",
                "capacity": "Capacité",
                "bed": "Literie",
                "wifi": "Wifi Gratuit",
                "courtesy": "Plateau de courtoisie",
                "hairdryer": "Sèche-cheveux",
                "products": "Produits d'accueil"
            },
            "garden_specs": {
                "size": "16 à 25 m²",
                "capacity": "1 à 4 personnes",
                "bed": "Lit Queen Size ou lits jumeaux"
            },
            "mer_specs": {
                "size": "16 à 31 m²",
                "capacity": "1 à 4 personnes",
                "bed": "Lit King Size ou Queen Size"
            },
            "pavillons_specs": {
                "size": "20 ou 26 m²",
                "capacity": "2 ou 4 personnes",
                "bed": "Lit Queen Size ou King Size"
            },
            "footer_question": "Vous avez des questions sur nos équipements ?",
            "footer_cta": "Contactez-nous"
        },
        "services": {
            "title": "Services & Activités",
            "subtitle": "Tout ce dont vous avez besoin pour un séjour d'exception sur la Côte d'Azur.",
            "hotel_services_title": "Les Services de l'Hôtel",
            "hotel_services_desc": "Profitez de nos installations haut de gamme conçues pour votre détente et votre confort.",
            "service_pool_title": "Piscine & Jacuzzi",
            "service_pool_desc": "Une piscine extérieure chauffée selon la saison et un jacuzzi sur demande pour vos moments de bien-être.",
            "service_garden_title": "Jardin & Salons",
            "service_garden_desc": "Un grand jardin méditerranéen parsemé de petits salons intimes pour lire, se reposer ou boire un verre.",
            "service_breakfast_title": "Petit-déjeuner Buffet",
            "service_breakfast_desc": "Servi sur la terrasse face à la mer, composé de produits frais pour bien démarrer votre journée.",
            "service_cab_title": "Chauffeur Privé & Transferts",
            "service_cab_desc": "En partenariat avec Myblackcab, nous organisons vos transferts depuis/vers l'aéroport, la gare, ou vos excursions touristiques sur demande.",
            "activities_title": "Découvrir Villefranche-sur-Mer",
            "activities_desc": "Un village d'art et d'histoire au charme intemporel.",
            "citadelle_title": "La Citadelle Saint-Elme",
            "citadelle_desc": "Imposante forteresse du XVIe siècle construite pour protéger la rade. Elle abrite aujourd'hui la Mairie et 4 musées (dont le Musée Volti et le Musée Goetz-Boumeester). Entrée libre.",
            "chapelle_title": "La Chapelle Saint-Pierre",
            "chapelle_desc": "Entièrement restaurée et décorée en 1956 par le célèbre artiste Jean Cocteau, c'est un chef-d'œuvre incontournable dédié au patron des pêcheurs.",
            "rue_title": "La Rue Obscure",
            "rue_desc": "Une rue médiévale couverte de 130 mètres de long (XIVe s.) qui servait de chemin défensif, immortalisée par Cocteau sur ses toiles.",
            "port_title": "Le Port Royal de la Darse",
            "port_desc": "Bassin historique du XVIe siècle avec ses remparts, son phare historique, sa corderie et son port de plaisance actif.",
            "surroundings_title": "Aux alentours sur la Riviera",
            "surroundings_desc": "Notre hôtel est le point de départ idéal pour explorer la Côte d'Azur :",
            "surroundings_nice": "Nice (10 min) : le vieux Nice, le marché du cours Saleya, la Promenade des Anglais (accès rapide en bus).",
            "surroundings_monaco": "Monaco (20 min) : le Rocher, le Casino de Monte-Carlo, le Musée Océanographique.",
            "surroundings_villages": "Les villages perchés d'Eze et de Saint-Paul-de-Vence pour une escapade pittoresque.",
            "surroundings_italy": "L'Italie à seulement 7 stations de train (départs réguliers de la gare de Villefranche)."
        },
        "gallery": {
            "title": "Notre Galerie Photos",
            "subtitle": "Découvrez en images le cadre enchanteur de notre boutique-hôtel.",
            "filter_all": "Tout",
            "filter_view": "Hôtel & Vue",
            "filter_pool": "Piscine & Jardin",
            "filter_rooms": "Chambres",
            "filter_breakfast": "Petit-Déjeuner"
        },
        "contact": {
            "title": "Contactez-nous",
            "subtitle": "Une question ? Une demande de réservation spécifique ? Notre équipe est à votre écoute.",
            "info_title": "Coordonnées",
            "info_address": "8 Boulevard de La Corne d'Or\nMoyenne Corniche\n06230 Villefranche-sur-Mer, France",
            "info_phone": "+33 4 93 76 67 40 / +33 7 45 28 29 37",
            "info_email": "info@fianceedupirate.com",
            "form_title": "Envoyer un message",
            "form_name": "Nom complet",
            "form_email": "Adresse e-mail",
            "form_phone": "Téléphone",
            "form_message": "Message",
            "form_submit": "Envoyer le message",
            "form_success": "Merci ! Votre message a bien été envoyé. Nous vous répondrons dans les plus brefs délais.",
            "form_error": "Une erreur est survenue lors de l'envoi. Veuillez réessayer ou nous contacter par e-mail.",
            "map_title": "Nous localiser"
        },
        "reviews": {
            "title": "Ce que nos clients disent",
            "subtitle": "Découvrez les avis de nos voyageurs sur TripAdvisor",
            "read_more": "Lire tous les avis sur TripAdvisor",
            "items": [
                {
                    "author": "Sophie L.",
                    "date": "Juin 2026",
                    "rating": 5,
                    "title": "Vue époustouflante et accueil chaleureux",
                    "text": "Un séjour absolument magique ! La vue sur la rade de Villefranche est incroyable depuis la terrasse du petit-déjeuner. L'hôtel est calme, intime et l'équipe est aux petits soins. Nous reviendrons sans hésiter."
                },
                {
                    "author": "Thomas M.",
                    "date": "Mai 2026",
                    "rating": 5,
                    "title": "Un petit coin de paradis",
                    "text": "La piscine et le jacuzzi avec vue mer sont parfaits pour se détendre après une journée de visite. Les chambres sont modernes, bien équipées et très propres. Idéalement situé pour explorer la région."
                },
                {
                    "author": "Elena R.",
                    "date": "Avril 2026",
                    "rating": 5,
                    "title": "Le charme et le calme absolu",
                    "text": "Boutique-hôtel d'exception. Le petit-déjeuner buffet est copieux et de grande qualité, servi devant un paysage de carte postale. Le service de navette partenaire Myblackcab a été parfait."
                }
            ]
        },
        "footer": {
            "desc": "La Fiancée du Pirate, boutique-hôtel intimiste de 15 chambres niché sur les hauteurs de Villefranche-sur-Mer, entre Nice et Monaco.",
            "links_title": "Navigation",
            "contact_title": "Contact",
            "social_title": "Suivez-nous",
            "rights": "Tous droits réservés. Mentions Légales.",
            "tripadvisor_badge": "Classé Excellent sur TripAdvisor"
        },
        "seo": {
            "home_title": "La Fiancée du Pirate | Boutique-Hôtel de Charme Villefranche-sur-Mer",
            "home_desc": "Réservez votre séjour à La Fiancée du Pirate, boutique-hôtel de 15 chambres avec vue mer panoramique sur la baie de Villefranche-sur-Mer, piscine et jacuzzi.",
            "rooms_title": "Nos Chambres & Pavillons | La Fiancée du Pirate",
            "rooms_desc": "Découvrez nos chambres côté jardin avec terrasse privée, nos chambres vue mer panoramique et nos pavillons indépendants pour un séjour de luxe intimiste.",
            "services_title": "Services & Activités Côte d'Azur | La Fiancée du Pirate",
            "services_desc": "Découvrez les prestations de notre hôtel (piscine, jacuzzi, jardin) et les activités culturelles à Villefranche-sur-Mer (Citadelle, Chapelle Cocteau, etc.).",
            "gallery_title": "Galerie Photos | La Fiancée du Pirate",
            "gallery_desc": "Découvrez en images notre piscine avec vue sur mer, notre terrasse panoramique, nos chambres rénovées et notre cadre d'exception.",
            "contact_title": "Contact & Accès | La Fiancée du Pirate",
            "contact_desc": "Contactez l'hôtel La Fiancée du Pirate à Villefranche-sur-Mer. Formulaire de contact, adresse, téléphone, e-mail et plan d'accès."
        }
    }
    
    # ------------------ ENGLISH (en) ------------------
    en = {
        "nav": {
            "home": "Home",
            "rooms": "Rooms",
            "services": "Services & Activities",
            "gallery": "Gallery",
            "contact": "Contact",
            "book": "Book Now"
        },
        "hero": {
            "title": "A serene escape overlooking the French Riviera",
            "subtitle": "Charming boutique hotel with panoramic views of the bay of Villefranche-sur-Mer",
            "cta": "Book a room"
        },
        "booking_bar": {
            "check_in": "Arrival",
            "check_out": "Departure",
            "guests": "Guests",
            "search": "Check Availability"
        },
        "accueil": {
            "intro_title": "Welcome to La Fiancée du Pirate",
            "intro_text": "Nestled on the cliffside (moyenne corniche) between Nice and Monaco, our intimate and unique 15-room boutique hotel offers an exceptional setting and breath-taking panoramic views of the Mediterranean Sea.",
            "intro_subtext": "Our entire team is at your complete disposal to make your stay unforgettable. Feel at home, but with all the comforts of a hotel!",
            "card_view_title": "Panoramic Views",
            "card_view_text": "Admire the spectacular view of the bay of Villefranche and Saint-Jean-Cap-Ferrat from our terrace while enjoying a drink.",
            "card_pool_title": "Pool & Garden",
            "card_pool_text": "Enjoy our quiet, sunny swimming pool, relax in our jacuzzi, or unwind in the private lounge areas of our lush garden.",
            "card_breakfast_title": "Seafront Breakfast",
            "card_breakfast_text": "A delicious buffet served daily from 8:30 to 10:30 on our panoramic terrace overlooking the sea.",
            "card_location_title": "Ideal Location",
            "card_location_text": "Privileged location on the moyenne corniche, with direct staircase access to the historic old town and beaches.",
            "explore_rooms_title": "Our Rooms & Pavilions",
            "explore_rooms_text": "Fully renovated, air-conditioned, and equipped with queen or king-size beds for ultimate comfort.",
            "myblackcab_title": "Private Transport Partner",
            "myblackcab_text": "For all your travels along the Riviera, contact our partner Myblackcab directly for a premium private chauffeur service."
        },
        "rooms": {
            "title": "Our Rooms & Pavilions",
            "subtitle": "Renovated for your utmost comfort, combining tranquility, privacy, and elegance.",
            "cta": "Book this room",
            "garden_title": "Garden Side Room",
            "garden_desc": "These pleasant rooms allow you to fully enjoy the garden with their private terraces.",
            "garden_details": "Available in Double, Triple, and Family options, they feature a cozy private terrace opening onto our green sanctuary.",
            "mer_title": "Sea View Room",
            "mer_desc": "Spacious and welcoming, these rooms offer breathtaking panoramic views of the bay of Villefranche-sur-Mer and Cap Ferrat.",
            "mer_details": "Available in Double, Triple, or Quadruple configurations. Wake up facing the deep blue Mediterranean.",
            "pavillons_title": "Our Private Pavilions",
            "pavillons_desc": "Separated from the main building, our two private pavilions offer a unique space of freedom and well-being.",
            "pavillons_details": "The Pavillon de la Fiancée is perfect for couples seeking romance. The Pavillon du Pirate is ideal for families thanks to its prime location.",
            "amenities_title": "Included Amenities",
            "specs": {
                "size": "Surface Area",
                "capacity": "Capacity",
                "bed": "Bedding",
                "wifi": "Free Wi-Fi",
                "courtesy": "Courtesy Tray",
                "hairdryer": "Hairdryer",
                "products": "Complimentary Toiletries"
            },
            "garden_specs": {
                "size": "16 to 25 m²",
                "capacity": "1 to 4 guests",
                "bed": "Queen Size bed or twin beds"
            },
            "mer_specs": {
                "size": "16 to 31 m²",
                "capacity": "1 to 4 guests",
                "bed": "King Size or Queen Size bed"
            },
            "pavillons_specs": {
                "size": "20 or 26 m²",
                "capacity": "2 or 4 guests",
                "bed": "Queen Size or King Size bed"
            },
            "footer_question": "Any questions about our room amenities?",
            "footer_cta": "Contact us"
        },
        "services": {
            "title": "Services & Activities",
            "subtitle": "Everything you need for an exceptional stay on the French Riviera.",
            "hotel_services_title": "Hotel Services",
            "hotel_services_desc": "Enjoy our high-end amenities designed for your absolute relaxation.",
            "service_pool_title": "Pool & Jacuzzi",
            "service_pool_desc": "An outdoor swimming pool, heated according to the season, and a jacuzzi available upon request.",
            "service_garden_title": "Garden & Lounges",
            "service_garden_desc": "A large Mediterranean garden with cozy, intimate seating areas to read, rest, or enjoy a drink.",
            "service_breakfast_title": "Buffet Breakfast",
            "service_breakfast_desc": "Served on the sea-facing terrace, featuring fresh local products to start your day beautifully.",
            "service_cab_title": "Private Chauffeur & Transfers",
            "service_cab_desc": "In partnership with Myblackcab, we organize your transfers from/to the airport, train station, or sightseeing excursions upon request.",
            "activities_title": "Discover Villefranche-sur-Mer",
            "activities_desc": "A charming, timeless coastal town of art and history.",
            "citadelle_title": "Saint-Elme Citadel",
            "citadelle_desc": "An imposing 16th-century fortress built to protect the bay. Today it houses the City Hall and 4 museums (including the Volti Museum and Goetz-Boumeester Museum). Free entry.",
            "chapelle_title": "Saint-Pierre Chapel",
            "chapelle_desc": "Fully restored and decorated in 1956 by the famous artist Jean Cocteau, this is a must-see masterpiece dedicated to the patron saint of fishermen.",
            "rue_title": "The Obscure Street (Rue Obscure)",
            "rue_desc": "A 130-meter covered medieval street dating back to the 14th century, once used as a defensive pathway and painted by Jean Cocteau.",
            "port_title": "Royal Port of La Darse",
            "port_desc": "Historical 16th-century basin featuring ancient fortifications, a lighthouse, a traditional rope-walk, and an active yachting marina.",
            "surroundings_title": "Around the French Riviera",
            "surroundings_desc": "Our hotel is the ideal starting point to explore the Côte d'Azur:",
            "surroundings_nice": "Nice (10 min): Old Nice, the Cours Saleya flower market, and the Promenade des Anglais (easily accessible by bus).",
            "surroundings_monaco": "Monaco (20 min): The Palace, Monte-Carlo Casino, and the Oceanographic Museum.",
            "surroundings_villages": "The picturesque perched villages of Eze and Saint-Paul-de-Vence.",
            "surroundings_italy": "Italy is just 7 train stops away (regular departures from Villefranche station)."
        },
        "gallery": {
            "title": "Photo Gallery",
            "subtitle": "Discover the enchanting setting of our boutique hotel in pictures.",
            "filter_all": "All",
            "filter_view": "Hotel & Views",
            "filter_pool": "Pool & Garden",
            "filter_rooms": "Rooms",
            "filter_breakfast": "Breakfast"
        },
        "contact": {
            "title": "Contact Us",
            "subtitle": "Have a question? Special booking request? Our team is here to assist you.",
            "info_title": "Contact Details",
            "info_address": "8 Boulevard de La Corne d'Or\nMoyenne Corniche\n06230 Villefranche-sur-Mer, France",
            "info_phone": "+33 4 93 76 67 40 / +33 7 45 28 29 37",
            "info_email": "info@fianceedupirate.com",
            "form_title": "Send a Message",
            "form_name": "Full Name",
            "form_email": "Email Address",
            "form_phone": "Phone Number",
            "form_message": "Message",
            "form_submit": "Send Message",
            "form_success": "Thank you! Your message has been sent successfully. We will get back to you shortly.",
            "form_error": "An error occurred while sending. Please try again or contact us directly via email.",
            "map_title": "Our Location"
        },
        "reviews": {
            "title": "What Our Guests Say",
            "subtitle": "Check out our guest reviews on TripAdvisor",
            "read_more": "Read all reviews on TripAdvisor",
            "items": [
                {
                    "author": "Sophie L.",
                    "date": "June 2026",
                    "rating": 5,
                    "title": "Breathtaking views and warm hospitality",
                    "text": "An absolutely magical stay! The view over the bay of Villefranche is incredible from the breakfast terrace. The hotel is quiet, intimate, and the staff is wonderful. We will definitely return."
                },
                {
                    "author": "Thomas M.",
                    "date": "May 2026",
                    "rating": 5,
                    "title": "A small piece of paradise",
                    "text": "The pool and jacuzzi with sea view are perfect for relaxing after a day of sightseeing. Rooms are modern, well-equipped, and very clean. Perfectly situated to explore the region."
                },
                {
                    "author": "Elena R.",
                    "date": "April 2026",
                    "rating": 5,
                    "title": "Absolute charm and quietness",
                    "text": "Outstanding boutique hotel. The buffet breakfast is delicious and high quality, served in front of a picture-postcard view. The partner chauffeur service Myblackcab was perfect."
                }
            ]
        },
        "footer": {
            "desc": "La Fiancée du Pirate, an intimate 15-room boutique hotel nestled on the heights of Villefranche-sur-Mer, between Nice and Monaco.",
            "links_title": "Navigation",
            "contact_title": "Contact",
            "social_title": "Follow Us",
            "rights": "All rights reserved. Legal Notice.",
            "tripadvisor_badge": "Rated Excellent on TripAdvisor"
        },
        "seo": {
            "home_title": "La Fiancée du Pirate | Charming Boutique Hotel Villefranche-sur-Mer",
            "home_desc": "Book your stay at La Fiancée du Pirate, a 15-room boutique hotel with panoramic sea views of the Villefranche bay, swimming pool, and jacuzzi.",
            "rooms_title": "Our Rooms & Pavilions | La Fiancée du Pirate",
            "rooms_desc": "Explore our garden-side rooms with private terrace, panoramic sea-view rooms, and independent pavilions for an intimate luxury getaway.",
            "services_title": "Services & Activities French Riviera | La Fiancée du Pirate",
            "services_desc": "Discover our hotel amenities (pool, jacuzzi, garden) and cultural activities in Villefranche-sur-Mer (Citadel, Cocteau Chapel, etc.).",
            "gallery_title": "Photo Gallery | La Fiancée du Pirate",
            "gallery_desc": "View pictures of our sea-view pool, panoramic terrace, newly renovated rooms, and exceptional seaside setting.",
            "contact_title": "Contact & Access | La Fiancée du Pirate",
            "contact_desc": "Contact hotel La Fiancée du Pirate in Villefranche-sur-Mer. Message form, address, phone number, email, and location map."
        }
    }
    
    # ------------------ AUSTRALIAN ENGLISH (en-au) ------------------
    # Re-uses English with subtle Australian spelling/localizations
    en_au = json.loads(json.dumps(en))
    en_au["nav"]["book"] = "Book Now"
    en_au["hero"]["cta"] = "Book a room"
    en_au["seo"]["home_title"] = "La Fiancée du Pirate | Charming Boutique Hotel Villefranche-sur-Mer"
    
    # ------------------ GERMAN (de) ------------------
    de = {
        "nav": {
            "home": "Startseite",
            "rooms": "Zimmer",
            "services": "Service & Aktivitäten",
            "gallery": "Galerie",
            "contact": "Kontakt",
            "book": "Buchen"
        },
        "hero": {
            "title": "Eine Oase der Ruhe über der Côte d'Azur",
            "subtitle": "Charmantes Boutique-Hotel mit Panoramablick auf die Bucht von Villefranche-sur-Mer",
            "cta": "Zimmer buchen"
        },
        "booking_bar": {
            "check_in": "Anreise",
            "check_out": "Abreise",
            "guests": "Gäste",
            "search": "Verfügbarkeit prüfen"
        },
        "accueil": {
            "intro_title": "Willkommen im La Fiancée du Pirate",
            "intro_text": "An der Klippenstraße (Moyenne Corniche) zwischen Nizza und Monaco gelegen, bietet unser intimes und einzigartiges Boutique-Hotel mit 15 Zimmern eine außergewöhnliche Kulisse und einen atemberaubenden Panoramablick auf das Mittelmeer.",
            "intro_subtext": "Unser gesamtes Team steht Ihnen zur Verfügung, um Ihnen einen unvergesslichen Aufenthalt zu bereiten. Fühlen Sie sich wie zu Hause, aber mit dem Komfort eines Hotels!",
            "card_view_title": "Panoramablick",
            "card_view_text": "Genießen Sie bei einem Drink auf unserer Terrasse den spektakulären Blick auf die Bucht von Villefranche und Saint-Jean-Cap-Ferrat.",
            "card_pool_title": "Pool & Garten",
            "card_pool_text": "Nutzen Sie unseren ruhigen, sonnigen Pool, entspannen Sie im Whirlpool oder in den gemütlichen Lounges unseres großen Gartens.",
            "card_breakfast_title": "Frühstück mit Meerblick",
            "card_breakfast_text": "Ein köstliches Buffet, täglich von 8:30 bis 10:30 Uhr auf unserer Panoramaterrasse mit Meerblick serviert.",
            "card_location_title": "Ideale Lage",
            "card_location_text": "Privilegierte Lage an der Moyenne Corniche, mit direktem Treppenzugang zur historischen Altstadt und den Stränden.",
            "explore_rooms_title": "Zimmer & Pavillons",
            "explore_rooms_text": "Vollständig renoviert, klimatisiert und mit Queen- oder Kingsize-Betten für optimalen Komfort ausgestattet.",
            "myblackcab_title": "Partner für Privattransfers",
            "myblackcab_text": "Für alle Fahrten an der Riviera kontaktieren Sie direkt unseren Partner Myblackcab für einen erstklassigen Chauffeurservice."
        },
        "rooms": {
            "title": "Unsere Zimmer & Pavillons",
            "subtitle": "Renoviert für höchsten Komfort, Ruhe, Privatsphäre und Eleganz.",
            "cta": "Dieses Zimmer buchen",
            "garden_title": "Zimmer zur Gartenseite",
            "garden_desc": "Diese gemütlichen Zimmer verfügen über eine eigene Terrasse, auf der Sie den Garten in vollen Zügen genießen können.",
            "garden_details": "Verfügbar als Doppel-, Dreibett- und Familienzimmer, bieten sie eine private Terrasse mit Blick in die Natur.",
            "mer_title": "Zimmer mit Meerblick",
            "mer_desc": "Geräumig und einladend bieten diese Zimmer einen unvergesslichen Panoramablick auf die Bucht von Villefranche-sur-Mer und das Cap Ferrat.",
            "mer_details": "Verfügbar als Doppel-, Dreibett- oder Vierbettzimmer. Wachen Sie direkt vor dem blauen Mittelmeer auf.",
            "pavillons_title": "Unsere privaten Pavillons",
            "pavillons_desc": "Getrennt vom Hauptgebäude bieten unsere beiden privaten Pavillons einzigartigen Freiraum und Wohlbefinden.",
            "pavillons_details": "Der Pavillon de la Fiancée ist ideal für Paare, die Romantik suchen. Der Pavillon du Pirate ist dank seiner Lage ideal für Familien.",
            "amenities_title": "Inklusive Leistungen",
            "specs": {
                "size": "Größe",
                "capacity": "Kapazität",
                "bed": "Betten",
                "wifi": "Kostenloses WLAN",
                "courtesy": "Kaffee- und Teezubereiter",
                "hairdryer": "Haartrockner",
                "products": "Pflegeprodukte"
            },
            "garden_specs": {
                "size": "16 bis 25 m²",
                "capacity": "1 bis 4 Personen",
                "bed": "Queensize-Bett oder getrennte Betten"
            },
            "mer_specs": {
                "size": "16 bis 31 m²",
                "capacity": "1 to 4 Personen",
                "bed": "Kingsize- oder Queensize-Bett"
            },
            "pavillons_specs": {
                "size": "20 oder 26 m²",
                "capacity": "2 oder 4 Personen",
                "bed": "Queensize- oder Kingsize-Bett"
            },
            "footer_question": "Haben Sie Fragen zur Ausstattung unserer Zimmer?",
            "footer_cta": "Kontaktieren Sie uns"
        },
        "services": {
            "title": "Service & Aktivitäten",
            "subtitle": "Alles, was Sie für einen außergewöhnlichen Aufenthalt an der Côte d'Azur brauchen.",
            "hotel_services_title": "Hotelservices",
            "hotel_services_desc": "Nutzen Sie unsere erstklassigen Einrichtungen für Entspannung und Komfort.",
            "service_pool_title": "Pool & Whirlpool",
            "service_pool_desc": "Ein saisonal beheizter Außenpool und ein Whirlpool auf Anfrage für entspannende Momente.",
            "service_garden_title": "Garten & Lounges",
            "service_garden_desc": "Ein großer mediterraner Garten mit gemütlichen Sitzecken zum Lesen, Entspannen oder Genießen eines Getränks.",
            "service_breakfast_title": "Frühstücksbuffet",
            "service_breakfast_desc": "Auf der Terrasse mit Meerblick serviert, bestehend aus frischen Produkten für einen perfekten Start in den Tag.",
            "service_cab_title": "Transport & Ausflüge",
            "service_cab_desc": "Flughafentransfer in 20 Min., Buslinien nach Nizza und Monaco in der Nähe sowie unser privater Transferpartner Myblackcab.",
            "activities_title": "Villefranche-sur-Mer entdecken",
            "activities_desc": "Ein historisches Kunst- und Küstenstädtchen mit zeitlosem Charme.",
            "citadelle_title": "Die Zitadelle Saint-Elme",
            "citadelle_desc": "Imposante Festung aus dem 16. Jahrhundert, die zum Schutz der Bucht erbaut wurde. Heute beherbergt sie das Rathaus und 4 Museen (darunter das Volti-Museum und das Goetz-Boumeester-Museum). Freier Eintritt.",
            "chapelle_title": "Die Kapelle Saint-Pierre",
            "chapelle_desc": "Diese im Jahr 1956 vom berühmten Künstler Jean Cocteau vollständig restaurierte und dekorierte Kapelle ist ein Meisterwerk, das dem Schutzpatron der Fischer gewidmet ist.",
            "rue_title": "Die Rue Obscure (Dunkle Straße)",
            "rue_desc": "Eine 130 Meter lange, überdachte mittelalterliche Straße aus dem 14. Jahrhundert, die einst als Verteidigungsweg diente und von Cocteau gemalt wurde.",
            "port_title": "Der königliche Hafen von La Darse",
            "port_desc": "Historisches Hafenbecken aus dem 16. Jahrhundert mit alten Befestigungsanlagen, Leuchtturm, Seilerei und einem Yachthafen.",
            "surroundings_title": "Umgebung & Riviera",
            "surroundings_desc": "Unser Hotel ist der ideale Ausgangspunkt, um die Côte d'Azur zu erkunden:",
            "surroundings_nice": "Nizza (10 Min.): Die Altstadt, der Blumenmarkt Cours Saleya und die Promenade des Anglais (schnell mit dem Bus erreichbar).",
            "surroundings_monaco": "Monaco (20 Min.): Der Palast, das Casino Monte-Carlo und das Ozeanographische Museum.",
            "surroundings_villages": "Die malerischen Bergdörfer Eze und Saint-Paul-de-Vence.",
            "surroundings_italy": "Italien ist nur 7 Zugstationen entfernt (regelmäßige Abfahrten vom Bahnhof Villefranche)."
        },
        "gallery": {
            "title": "Fotogalerie",
            "subtitle": "Entdecken Sie die bezaubernde Kulisse unseres Hotels in Bildern.",
            "filter_all": "Alle",
            "filter_view": "Hotel & Ausblick",
            "filter_pool": "Pool & Garten",
            "filter_rooms": "Zimmer",
            "filter_breakfast": "Frühstück"
        },
        "contact": {
            "title": "Kontaktieren Sie uns",
            "subtitle": "Haben Sie Fragen oder spezielle Wünsche? Unser Team steht Ihnen gerne zur Verfügung.",
            "info_title": "Kontaktdaten",
            "info_address": "8 Boulevard de La Corne d'Or\nMoyenne Corniche\n06230 Villefranche-sur-Mer, Frankreich",
            "info_phone": "+33 4 93 76 67 40 / +33 7 45 28 29 37",
            "info_email": "info@fianceedupirate.com",
            "form_title": "Nachricht senden",
            "form_name": "Vollständiger Name",
            "form_email": "E-Mail-Adresse",
            "form_phone": "Telefonnummer",
            "form_message": "Nachricht",
            "form_submit": "Nachricht senden",
            "form_success": "Vielen Dank! Ihre Nachricht wurde erfolgreich gesendet. Wir werden uns in Kürze bei Ihnen melden.",
            "form_error": "Beim Senden ist ein Fehler aufgetreten. Bitte versuchen Sie es erneut oder kontaktieren Sie uns direkt per E-Mail.",
            "map_title": "Standort"
        },
        "reviews": {
            "title": "Was unsere Gäste sagen",
            "subtitle": "Erfahren Sie, was Reisende auf TripAdvisor über uns schreiben",
            "read_more": "Alle Bewertungen auf TripAdvisor lesen",
            "items": [
                {
                    "author": "Sophie L.",
                    "date": "Juni 2026",
                    "rating": 5,
                    "title": "Atemberaubende Aussicht und herzlicher Service",
                    "text": "Ein absolut zauberhafter Aufenthalt! Die Aussicht auf die Bucht von Villefranche von der Frühstücksterrasse ist unglaublich. Das Hotel ist ruhig, intim und das Personal sehr aufmerksam. Wir kommen wieder."
                },
                {
                    "author": "Thomas M.",
                    "date": "Mai 2026",
                    "rating": 5,
                    "title": "Ein kleines Stück Paradies",
                    "text": "Der Pool und Whirlpool mit Meerblick sind ideal zum Entspannen. Die Zimmer sind modern, gut ausgestattet und sehr sauber. Perfekte Lage, um die Region zu erkunden."
                },
                {
                    "author": "Elena R.",
                    "date": "April 2026",
                    "rating": 5,
                    "title": "Absoluter Charme und Ruhe",
                    "text": "Herausragendes Boutique-Hotel. Das Frühstücksbuffet ist köstlich und hochwertig, serviert vor einer Postkartenkulisse. Der Chauffeurservice von Partner Myblackcab war perfekt."
                }
            ]
        },
        "footer": {
            "desc": "La Fiancée du Pirate, ein gemütliches Boutique-Hotel mit 15 Zimmern auf den Höhen von Villefranche-sur-Mer, zwischen Nizza und Monaco.",
            "links_title": "Navigation",
            "contact_title": "Kontakt",
            "social_title": "Folgen Sie uns",
            "rights": "Alle Rechte vorbehalten. Impressum.",
            "tripadvisor_badge": "Auf TripAdvisor als Ausgezeichnet bewertet"
        },
        "seo": {
            "home_title": "La Fiancée du Pirate | Charmantes Boutique-Hotel Villefranche-sur-Mer",
            "home_desc": "Buchen Sie Ihren Aufenthalt im La Fiancée du Pirate, einem Boutique-Hotel mit 15 Zimmern, Panoramablick auf das Meer, Pool und Whirlpool.",
            "rooms_title": "Unsere Zimmer & Pavillons | La Fiancée du Pirate",
            "rooms_desc": "Entdecken Sie unsere Zimmer zur Gartenseite mit Terrasse, die Meerblickzimmer und unsere freistehenden Pavillons für einen luxuriösen Urlaub.",
            "services_title": "Service & Aktivitäten Côte d'Azur | La Fiancée du Pirate",
            "services_desc": "Erfahren Sie mehr über unseren Service (Pool, Garten, Whirlpool) und kulturelle Highlights in Villefranche-sur-Mer (Zitadelle, Kapelle Cocteau).",
            "gallery_title": "Fotogalerie | La Fiancée du Pirate",
            "gallery_desc": "Sehen Sie Bilder von unserem Pool mit Meerblick, der Panoramaterrasse und den komfortablen, renovierten Zimmern.",
            "contact_title": "Kontakt & Anfahrt | La Fiancée du Pirate",
            "contact_desc": "Kontaktieren Sie das Hotel La Fiancée du Pirate. Kontaktformular, Adresse, Telefonnummer, E-Mail-Adresse und Anfahrtskarte."
        }
    }
    
    # ------------------ ITALIAN (it) ------------------
    it = {
        "nav": {
            "home": "Home",
            "rooms": "Camere",
            "services": "Servizi & Attività",
            "gallery": "Galleria",
            "contact": "Contatti",
            "book": "Prenota"
        },
        "hero": {
            "title": "Un'oasi di pace sospesa sulla Costa Azzurra",
            "subtitle": "Incantevole boutique hotel con vista panoramica sulla baia di Villefranche-sur-Mer",
            "cta": "Prenota una camera"
        },
        "booking_bar": {
            "check_in": "Arrivo",
            "check_out": "Partenza",
            "guests": "Ospiti",
            "search": "Verifica disponibilità"
        },
        "accueil": {
            "intro_title": "Benvenuti a La Fiancée du Pirate",
            "intro_text": "Immerso sulla moyenne corniche tra Nizza e Monaco, il nostro boutique hotel intimo e unico di 15 camere vi offre una cornice eccezionale e una vista panoramica spettacolare sul Mar Mediterraneo.",
            "intro_subtext": "Tutto il nostro staff è a vostra disposizione per farvi vivere un soggiorno indimenticabile. Vi sentirete a casa, ma con tutti i comfort di un hotel!",
            "card_view_title": "Vista Panoramica",
            "card_view_text": "Ammirate la vista spettacolare sulla baia di Villefranche e Saint-Jean-Cap-Ferrat dalla nostra terrazza sorseggiando un drink.",
            "card_pool_title": "Piscina & Giardino",
            "card_pool_text": "Godetevi la nostra piscina tranquilla e soleggiata, rilassatevi nella vasca idromassaggio o nelle aree relax del nostro ampio giardino.",
            "card_breakfast_title": "Colazione Vista Mare",
            "card_breakfast_text": "Una deliziosa colazione a buffet servita tutti i giorni dalle 8:30 alle 10:30 sulla nostra terrazza panoramica di fronte al mare.",
            "card_location_title": "Posizione Ideale",
            "card_location_text": "Posizione privilegiata sulla moyenne corniche, con accesso diretto tramite scale al centro storico e alle spiagge.",
            "explore_rooms_title": "Camere & Padiglioni",
            "explore_rooms_text": "Interamente rinnovate, climatizzate e dotate di letti queen o king-size per il massimo comfort.",
            "myblackcab_title": "Partner di Trasporto Privato",
            "myblackcab_text": "Per tutti i vostri spostamenti sulla Riviera, contattate direttamente il nostro partner Myblackcab per un servizio di autista privato di lusso."
        },
        "rooms": {
            "title": "Le Nostre Camere & Padiglioni",
            "subtitle": "Rinnovate per il vostro massimo comfort, all'insegna di tranquillità, privacy ed eleganza.",
            "cta": "Prenota questa camera",
            "garden_title": "Camera Lato Giardino",
            "garden_desc": "Queste piacevoli camere vi consentono di godere appieno del giardino grazie alle loro terrazze private.",
            "garden_details": "Disponibili in versione Doppia, Tripla e Familiare, dispongono di una terrazza privata che si affaccia sulla nostra oasi di verde.",
            "mer_title": "Camera Vista Mare",
            "mer_desc": "Spaziose e accoglienti, queste camere offrono una vista panoramica spettacolare sulla baia di Villefranche-sur-Mer e su Cap Ferrat.",
            "mer_details": "Disponibili in versione Doppia, Tripla o Quadrupla. Svegliatevi di fronte all'azzurro del Mediterraneo.",
            "pavillons_title": "I Nostri Padiglioni Privati",
            "pavillons_desc": "Separati dal corpo principale, i nostri due padiglioni privati offrono uno spazio unico di libertà e benessere.",
            "pavillons_details": "Il Pavillon de la Fiancée incanterà le coppie in cerca di romanticismo. Il Pavillon du Pirate conquisterà le famiglie grazie alla sua posizione ideale.",
            "amenities_title": "Servizi inclusi",
            "specs": {
                "size": "Superficie",
                "capacity": "Capacità",
                "bed": "Letti",
                "wifi": "Wi-Fi Gratuito",
                "courtesy": "Set di cortesia (tè/caffè)",
                "hairdryer": "Asciugacapelli",
                "products": "Prodotti da bagno omaggio"
            },
            "garden_specs": {
                "size": "Da 16 a 25 m²",
                "capacity": "Da 1 a 4 persone",
                "bed": "Letto Queen Size o letti singoli"
            },
            "mer_specs": {
                "size": "Da 16 a 31 m²",
                "capacity": "Da 1 a 4 persone",
                "bed": "Letto King Size o Queen Size"
            },
            "pavillons_specs": {
                "size": "20 o 26 m²",
                "capacity": "2 o 4 persone",
                "bed": "Letto Queen Size o King Size"
            },
            "footer_question": "Avete domande sui servizi delle nostre camere?",
            "footer_cta": "Contattateci"
        },
        "services": {
            "title": "Servizi & Attività",
            "subtitle": "Tutto il necessario per un soggiorno eccezionale in Costa Azzurra.",
            "hotel_services_title": "Servizi dell'Hotel",
            "hotel_services_desc": "Approfittate delle nostre strutture di alta qualità pensate per il vostro relax.",
            "service_pool_title": "Piscine & Idromassaggio",
            "service_pool_desc": "Una piscina all'aperto riscaldata a seconda della stagione e una vasca idromassaggio su richiesta per i vostri momenti di benessere.",
            "service_garden_title": "Giardino & Salottini",
            "service_garden_desc": "Un grande giardino mediterraneo con salottini intimi per leggere, riposare o sorseggiare un drink.",
            "service_breakfast_title": "Colazione a Buffet",
            "service_breakfast_desc": "Servita sulla terrazza di fronte al mare, preparata con prodotti freschi locali per iniziare al meglio la giornata.",
            "service_cab_title": "Trasporti & Escursioni",
            "service_cab_desc": "Trasferimenti aeroportuali in 20 min., linee di autobus per Nizza e Monaco nelle vicinanze e il nostro partner di trasporto privato Myblackcab.",
            "activities_title": "Scoprire Villefranche-sur-Mer",
            "activities_desc": "Un affascinante borgo costiero d'arte e di storia dal fascino intramontabile.",
            "citadelle_title": "La Cittadella Saint-Elme",
            "citadelle_desc": "Imponente fortezza del XVI secolo costruita per proteggere la rada. Oggi ospita il Municipio e 4 musei (tra cui il Museo Volti e il Museo Goetz-Boumeester). Ingresso gratuito.",
            "chapelle_title": "La Cappella Saint-Pierre",
            "chapelle_desc": "Interamente restaurata e decorata nel 1956 dal celebre artista Jean Cocteau, è un capolavoro imperdibile dedicato al santo patrono dei pescatori.",
            "rue_title": "La Rue Obscure (Via Oscura)",
            "rue_desc": "Una via medievale coperta lunga 130 metri risalente al XIV secolo, che un tempo fungeva da passaggio difensivo ed è stata dipinta da Cocteau.",
            "port_title": "Porto Reale di La Darse",
            "port_desc": "Bacino storico del XVI secolo con antiche fortificazioni, faro storico, corderia e porto turistico attivo.",
            "surroundings_title": "Nei dintorni della Riviera",
            "surroundings_desc": "Il nostro hotel è il punto di partenza ideale per esplorare la Costa Azzurra:",
            "surroundings_nice": "Nizza (10 min): la vecchia Nizza, il mercato dei fiori di Cours Saleya e la Promenade des Anglais (facilmente raggiungibile in bus).",
            "surroundings_monaco": "Monaco (20 min): Il Palazzo dei Principi, il Casinò di Monte-Carlo e il Museo Oceanografico.",
            "surroundings_villages": "I pittoreschi villaggi medievali di Eze e Saint-Paul-de-Vence.",
            "surroundings_italy": "L'Italia è a sole 7 fermate di treno (partenze regolari dalla stazione di Villefranche)."
        },
        "gallery": {
            "title": "Galleria Fotografica",
            "subtitle": "Scoprite le immagini dell'incantevole cornice del nostro boutique hotel.",
            "filter_all": "Tutti",
            "filter_view": "Hotel & Vista",
            "filter_pool": "Piscina & Giardino",
            "filter_rooms": "Camere",
            "filter_breakfast": "Colazione"
        },
        "contact": {
            "title": "Contattaci",
            "subtitle": "Domande? Richieste speciali di prenotazione? Il nostro team è a tua disposizione.",
            "info_title": "Dettagli di Contatto",
            "info_address": "8 Boulevard de La Corne d'Or\nMoyenne Corniche\n06230 Villefranche-sur-Mer, Francia",
            "info_phone": "+33 4 93 76 67 40 / +33 7 45 28 29 37",
            "info_email": "info@fianceedupirate.com",
            "form_title": "Invia un messaggio",
            "form_name": "Nome completo",
            "form_email": "Indirizzo e-mail",
            "form_phone": "Numero di telefono",
            "form_message": "Messaggio",
            "form_submit": "Invia messaggio",
            "form_success": "Grazie! Il tuo messaggio è stato inviato con successo. Ti risponderemo al più presto.",
            "form_error": "Si è verificato un errore durante l'invio. Riprova o contattaci direttamente via e-mail.",
            "map_title": "La nostra posizione"
        },
        "reviews": {
            "title": "Cosa dicono i nostri ospiti",
            "subtitle": "Leggi le recensioni dei nostri viaggiatori su TripAdvisor",
            "read_more": "Leggi tutte le recensioni su TripAdvisor",
            "items": [
                {
                    "author": "Sophie L.",
                    "date": "Giugno 2026",
                    "rating": 5,
                    "title": "Vista spettacolare e accoglienza calorosa",
                    "text": "Un soggiorno assolutamente magico! La vista sulla baia di Villefranche dalla terrazza della colazione è incredibile. L'hotel è tranquillo, intimo e lo staff è fantastico. Ritorneremo sicuramente."
                },
                {
                    "author": "Thomas M.",
                    "date": "Maggio 2026",
                    "rating": 5,
                    "title": "Un piccolo angolo di paradiso",
                    "text": "La piscina e la vasca idromassaggio vista mare sono perfette per rilassarsi. Le camere sono moderne, ben attrezzate e molto pulite. Posizione strategica per esplorare la Riviera."
                },
                {
                    "author": "Elena R.",
                    "date": "Aprile 2026",
                    "rating": 5,
                    "title": "Fascino e tranquillità assoluta",
                    "text": "Boutique hotel eccezionale. La colazione a buffet è abbondante e di alta qualità, servita davanti a una vista da cartolina. Il servizio di autista partner Myblackcab è stato perfetto."
                }
            ]
        },
        "footer": {
            "desc": "La Fiancée du Pirate, boutique hotel intimo di 15 camere sulle alture di Villefranche-sur-Mer, tra Nizza e Monaco.",
            "links_title": "Navigazione",
            "contact_title": "Contatti",
            "social_title": "Seguici su",
            "rights": "Tutti i diritti riservati. Note Legali.",
            "tripadvisor_badge": "Valutato Eccellente su TripAdvisor"
        },
        "seo": {
            "home_title": "La Fiancée du Pirate | Incantevole Boutique Hotel Villefranche-sur-Mer",
            "home_desc": "Prenota il tuo soggiorno a La Fiancée du Pirate, boutique hotel di 15 camere con vista mare spettacolare sulla baia di Villefranche-sur-Mer, piscina e idromassaggio.",
            "rooms_title": "Camere & Padiglioni | La Fiancée du Pirate",
            "rooms_desc": "Scopri le nostre camere lato giardino con terrazza privata, camere vista mare panoramica e padiglioni indipendenti per vacanze esclusive in Costa Azzurra.",
            "services_title": "Servizi & Attività Costa Azzurra | La Fiancée du Pirate",
            "services_desc": "Scopri i servizi del nostro hotel (piscina, idromassaggio, giardino) e le attrazioni culturali a Villefranche-sur-Mer (Citadella, Cappella Cocteau).",
            "gallery_title": "Galleria Foto | La Fiancée du Pirate",
            "gallery_desc": "Guarda le foto della nostra piscina vista mare, della terrazza panoramica e delle nostre camere rinnovate ed eleganti.",
            "contact_title": "Contatti & Mappa | La Fiancée du Pirate",
            "contact_desc": "Contatta l'hotel La Fiancée du Pirate a Villefranche-sur-Mer. Modulo di contatto, indirizzo, telefono, e-mail e mappa stradale."
        }
    }
    
    # ------------------ SPANISH (es) ------------------
    es = {
        "nav": {
            "home": "Inicio",
            "rooms": "Habitaciones",
            "services": "Servicios & Actividades",
            "gallery": "Galería",
            "contact": "Contacto",
            "book": "Reservar"
        },
        "hero": {
            "title": "Un oasis de calma con vistas a la Costa Azul",
            "subtitle": "Encantador hotel boutique con vistas panorámicas a la bahía de Villefranche-sur-Mer",
            "cta": "Reservar una habitación"
        },
        "booking_bar": {
            "check_in": "Llegada",
            "check_out": "Salida",
            "guests": "Huéspedes",
            "search": "Comprobar disponibilidad"
        },
        "accueil": {
            "intro_title": "Bienvenidos a La Fiancée du Pirate",
            "intro_text": "Situado en la moyenne corniche entre Niza y Mónaco, nuestro hotel boutique íntimo y único de 15 habitaciones le ofrece un entorno excepcional y unas vistas panorámicas espectaculares del mar Mediterráneo.",
            "intro_subtext": "Todo nuestro equipo está a su disposición para que disfrute de una estancia inolvidable. ¡Siéntase como en casa, pero con los servicios de un hotel!",
            "card_view_title": "Vistas Panorámicas",
            "card_view_text": "Admire las vistas espectaculares de la bahía de Villefranche y Saint-Jean-Cap-Ferrat desde nuestra terraza mientras disfruta de una bebida.",
            "card_pool_title": "Piscina & Jardín",
            "card_pool_text": "Disfrute de nuestra piscina tranquila y soleada, relájese en el jacuzzi o en las acogedoras zonas de descanso de nuestro gran jardín.",
            "card_breakfast_title": "Desayuno Frente al Mar",
            "card_breakfast_text": "Un delicioso desayuno buffet servido todos los días de 8:30 a 10:30 en nuestra terraza panorámica con vistas al mar.",
            "card_location_title": "Ubicación Ideal",
            "card_location_text": "Ubicación privilegiada en la moyenne corniche, con acceso directo por escaleras al centro histórico y a las playas.",
            "explore_rooms_title": "Habitaciones & Pabellones",
            "explore_rooms_text": "Totalmente renovadas, climatizadas y equipadas con camas queen o king-size para su máximo confort.",
            "myblackcab_title": "Socio de Transporte Privado",
            "myblackcab_text": "Para todos sus traslados por la Riviera, contacte directamente con nuestro socio Myblackcab para un servicio de chófer privado premium."
        },
        "rooms": {
            "title": "Nuestras Habitaciones & Pabellones",
            "subtitle": "Renovadas para su mayor comodidad, combinando tranquilidad, privacidad y elegancia.",
            "cta": "Reservar esta habitación",
            "garden_title": "Habitación Lado Jardín",
            "garden_desc": "Estas agradables habitaciones le permiten disfrutar plenamente del jardín gracias a sus terrazas privadas.",
            "garden_details": "Disponibles en versiones Doble, Triple y Familiar, cuentan con una terraza privada que da a nuestro oasis verde.",
            "mer_title": "Habitación Vista al Mar",
            "mer_desc": "Espaciosas y acogedoras, estas habitaciones ofrecen unas vistas panorámicas espectaculares de la bahía de Villefranche-sur-Mer y Cap Ferrat.",
            "mer_details": "Disponibles en versiones Doble, Triple o Cuádruple. Despiértese frente al azul del Mediterráneo.",
            "pavillons_title": "Nuestros Pabellones Privados",
            "pavillons_desc": "Separados del edificio principal, nuestros dos pabellones privados ofrecen un espacio único de libertad y bienestar.",
            "pavillons_details": "El Pavillon de la Fiancée encantará a las parejas que buscan romance. El Pavillon du Pirate conquistará a las familias gracias a su ubicación privilegiada.",
            "amenities_title": "Servicios incluidos",
            "specs": {
                "size": "Superficie",
                "capacity": "Capacidad",
                "bed": "Camas",
                "wifi": "Wifi Gratis",
                "courtesy": "Bandeja de cortesía (café/té)",
                "hairdryer": "Secador de pelo",
                "products": "Productos de acogida gratis"
            },
            "garden_specs": {
                "size": "De 16 a 25 m²",
                "capacity": "De 1 a 4 personas",
                "bed": "Cama Queen Size o camas individuales"
            },
            "mer_specs": {
                "size": "De 16 a 31 m²",
                "capacity": "De 1 a 4 personas",
                "bed": "Cama King Size o Queen Size"
            },
            "pavillons_specs": {
                "size": "20 o 26 m²",
                "capacity": "2 o 4 personas",
                "bed": "Cama Queen Size o King Size"
            },
            "footer_question": "¿Tiene alguna pregunta sobre los servicios de nuestras habitaciones?",
            "footer_cta": "Contacte con nosotros"
        },
        "services": {
            "title": "Servicios & Actividades",
            "subtitle": "Todo lo que necesita para una estancia excepcional en la Costa Azul.",
            "hotel_services_title": "Servicios del Hotel",
            "hotel_services_desc": "Disfrute de nuestras instalaciones de primera calidad diseñadas para su relajación.",
            "service_pool_title": "Piscina & Jacuzzi",
            "service_pool_desc": "Una piscina al aire libre, climatizada según la temporada, y un jacuzzi disponible bajo petición para su bienestar.",
            "service_garden_title": "Jardín & Salones",
            "service_garden_desc": "Un gran jardín mediterráneo con íntimos salones al aire libre para leer, descansar o disfrutar de una bebida.",
            "service_breakfast_title": "Desayuno Buffet",
            "service_breakfast_desc": "Servido en la terraza frente al mar, elaborado con ingredientes locales frescos para empezar el día de la mejor manera.",
            "service_cab_title": "Transporte & Excursiones",
            "service_cab_desc": "Traslados al aeropuerto en 20 min., líneas de autobús a Niza y Mónaco cerca y nuestro socio de transporte privado Myblackcab.",
            "activities_title": "Descubrir Villefranche-sur-Mer",
            "activities_desc": "Un encantador pueblo pesquero de arte y de historia con un atractivo atemporal.",
            "citadelle_title": "La Ciudadela Saint-Elme",
            "citadelle_desc": "Imponente fortaleza del siglo XVI construida para proteger la bahía. Hoy alberga el Ayuntamiento y 4 museos (incluyendo el Museo Volti y el Museo Goetz-Boumeester). Entrada libre.",
            "chapelle_title": "La Capilla Saint-Pierre",
            "chapelle_desc": "Totalmente restaurada y decorada en 1956 por el famoso artista Jean Cocteau, es una obra maestra imprescindible dedicada al santo patrón de los pescadores.",
            "rue_title": "La Calle Oscura (Rue Obscure)",
            "rue_desc": "Una calle medieval cubierta de 130 metros de largo que data del siglo XIV, utilizada antiguamente como paso defensivo y pintada por Cocteau.",
            "port_title": "Puerto Real de La Darse",
            "port_desc": "Dársena histórica del siglo XVI con antiguas fortificaciones, faro, fábrica de cuerdas y un puerto deportivo activo.",
            "surroundings_title": "Alrededor de la Costa Azul",
            "surroundings_desc": "Nuestro hotel es el punto de partida ideal para explorar la Costa Azul:",
            "surroundings_nice": "Niza (10 min): el casco antiguo, el mercado de flores de Cours Saleya y el Paseo de los Ingleses (fácil acceso en autobús).",
            "surroundings_monaco": "Mónaco (20 min): El Palacio de los Príncipes, el Casino de Montecarlo y el Museo Oceanográfico.",
            "surroundings_villages": "Los pintorescos pueblos colgados de Eze y Saint-Paul-de-Vence.",
            "surroundings_italy": "Italia está a solo 7 paradas de tren (salidas regulares desde la estación de Villefranche)."
        },
        "gallery": {
            "title": "Galería de Fotos",
            "subtitle": "Descubra en imágenes el entorno encantador de nuestro hotel boutique.",
            "filter_all": "Todo",
            "filter_view": "Hotel & Vistas",
            "filter_pool": "Piscina & Jardín",
            "filter_rooms": "Habitaciones",
            "filter_breakfast": "Desayuno"
        },
        "contact": {
            "title": "Contacte con nosotros",
            "subtitle": "¿Tiene preguntas o alguna petición especial de reserva? Nuestro equipo está a su disposición.",
            "info_title": "Datos de Contacto",
            "info_address": "8 Boulevard de La Corne d'Or\nMoyenne Corniche\n06230 Villefranche-sur-Mer, Francia",
            "info_phone": "+33 4 93 76 67 40 / +33 7 45 28 29 37",
            "info_email": "info@fianceedupirate.com",
            "form_title": "Enviar un mensaje",
            "form_name": "Nombre completo",
            "form_email": "Correo electrónico",
            "form_phone": "Número de teléfono",
            "form_message": "Mensaje",
            "form_submit": "Enviar mensaje",
            "form_success": "¡Gracias! Su mensaje ha sido enviado con éxito. Le responderemos lo antes posible.",
            "form_error": "Ocurrió un error al enviar. Por favor, inténtelo de nuevo o contáctenos directamente por correo electrónico.",
            "map_title": "Ubicación"
        },
        "reviews": {
            "title": "Lo que dicen nuestros huéspedes",
            "subtitle": "Consulte los comentarios de nuestros huéspedes en TripAdvisor",
            "read_more": "Leer todas las opiniones en TripAdvisor",
            "items": [
                {
                    "author": "Sophie L.",
                    "date": "Junio 2026",
                    "rating": 5,
                    "title": "Vistas espectaculares y acogida cálida",
                    "text": "¡Una estancia absolutamente mágica! Las vistas de la bahía de Villefranche desde la terraza del desayuno son increíbles. El hotel es tranquilo, íntimo y el personal excelente. Volveremos sin dudarlo."
                },
                {
                    "author": "Thomas M.",
                    "date": "Mayo 2026",
                    "rating": 5,
                    "title": "Un pequeño trozo de paraíso",
                    "text": "La piscina y el jacuzzi con vistas al mar son ideales para relajarse. Las habitaciones son modernas, bien equipadas y muy limpias. Ubicación perfecta para explorar la zona."
                },
                {
                    "author": "Elena R.",
                    "date": "Abril 2026",
                    "rating": 5,
                    "title": "Encanto y tranquilidad absoluta",
                    "text": "Hotel boutique excepcional. El desayuno buffet es delicioso y de gran calidad, servido frente a una postal increíble. El servicio de chófer socio Myblackcab fue perfecto."
                }
            ]
        },
        "footer": {
            "desc": "La Fiancée du Pirate, hotel boutique íntimo de 15 habitaciones situado en las colinas de Villefranche-sur-Mer, entre Niza y Mónaco.",
            "links_title": "Navegación",
            "contact_title": "Contacto",
            "social_title": "Síganos",
            "rights": "Todos los derechos reservados. Aviso Legal.",
            "tripadvisor_badge": "Valorado como Excelente en TripAdvisor"
        },
        "seo": {
            "home_title": "La Fiancée du Pirate | Encantador Hotel Boutique Villefranche-sur-Mer",
            "home_desc": "Reserve su estancia en La Fiancée du Pirate, un hotel boutique de 15 habitaciones con vistas panorámicas al mar de la bahía de Villefranche, piscina y jacuzzi.",
            "rooms_title": "Nuestras Habitaciones & Pabellones | La Fiancée du Pirate",
            "rooms_desc": "Descubra nuestras habitaciones lado jardín con terraza privada, habitaciones con vistas al mar y pabellones independientes para una escapada íntima y exclusiva.",
            "services_title": "Servicios & Actividades Costa Azul | La Fiancée du Pirate",
            "services_desc": "Descubra los servicios de nuestro hotel (piscina, jacuzzi, jardín) y las actividades culturales en Villefranche-sur-Mer (Ciudadela, Capilla Cocteau).",
            "gallery_title": "Galería de Fotos | La Fiancée du Pirate",
            "gallery_desc": "Vea las fotos de nuestra piscina con vistas al mar, la terraza panorámica y nuestras habitaciones renovadas y confortables.",
            "contact_title": "Contacto & Mapa | La Fiancée du Pirate",
            "contact_desc": "Contacte con el hotel La Fiancée du Pirate. Formulario de contacto, dirección, teléfono, correo electrónico y mapa de ubicación."
        }
    }
    
    # ------------------ RUSSIAN (ru) ------------------
    ru = {
        "nav": {
            "home": "Главная",
            "rooms": "Номера",
            "services": "Услуги и развлечения",
            "gallery": "Галерея",
            "contact": "Контакты",
            "book": "Забронировать"
        },
        "hero": {
            "title": "Уютный отдых над Лазурным Берегом",
            "subtitle": "Очаровательный бутик-отель с панорамным видом на залив Вильфранш-сюр-Мер",
            "cta": "Забронировать номер"
        },
        "booking_bar": {
            "check_in": "Заезд",
            "check_out": "Выезд",
            "guests": "Гости",
            "search": "Проверить наличие"
        },
        "accueil": {
            "intro_title": "Добро пожаловать в La Fiancée du Pirate",
            "intro_text": "Расположенный на живописном склоне (Средний Корниш) между Ниццей и Монако, наш уютный и уникальный бутик-отель на 15 номеров предлагает исключительный сервис и захватывающий панорамный вид на Средиземное море.",
            "intro_subtext": "Вся наша команда в вашем полном распоряжении, чтобы сделать ваше пребывание незабываемым. Чувствуйте себя как дома, но со всеми удобствами отеля!",
            "card_view_title": "Панорамный вид",
            "card_view_text": "Любуйтесь великолепным видом на бухту Вильфранш и Кап-Ферра с нашей террасы за бокалом любимого напитка.",
            "card_pool_title": "Бассейн и сад",
            "card_pool_text": "Отдохните у нашего тихого солнечного бассейна, расслабьтесь в джакузи или в уединенных уголках нашего просторного сада.",
            "card_breakfast_title": "Завтрак с видом на море",
            "card_breakfast_text": "Вкусный завтрак «шведский стол» подается ежедневно с 8:30 до 10:30 на нашей панорамной террасе у моря.",
            "card_location_title": "Идеальное расположение",
            "card_location_text": "Удобное расположение на Среднем Корнише с прямым спуском по лестнице к историческому старому городу и пляжам.",
            "explore_rooms_title": "Наши номера и павильоны",
            "explore_rooms_text": "Полностью отремонтированные номера с кондиционером, оснащенные кроватями queen-size или king-size для вашего комфорта.",
            "myblackcab_title": "Партнер по трансферу Myblackcab",
            "myblackcab_text": "Для комфортных поездок по Ривьере свяжитесь напрямую с нашим партнером Myblackcab для заказа личного трансфера премиум-класса."
        },
        "rooms": {
            "title": "Наши номера и павильоны",
            "subtitle": "Отремонтированы для вашего максимального удобства, сочетая покой, уединение и элегантность.",
            "cta": "Забронировать этот номер",
            "garden_title": "Номер с выходом в сад",
            "garden_desc": "Эти приятные номера позволяют в полной мере насладиться садом благодаря собственной террасе.",
            "garden_details": "Доступны в двухместном, трехместном и семейном вариантах. К услугам гостей уютная терраса с видом на зеленый сад.",
            "mer_title": "Номер с видом на море",
            "mer_desc": "Просторные и гостеприимные номера с незабываемым панорамным видом на залив Вильфранш-сюр-Мер и Кап-Ферра.",
            "mer_details": "Доступны в двух-, трех- и четырехместной конфигурациях. Просыпайтесь под шум волн Средиземного моря.",
            "pavillons_title": "Наши отдельные павильоны",
            "pavillons_desc": "Расположенные отдельно от главного здания, наши два частных павильона дарят уникальное ощущение свободы и комфорта.",
            "pavillons_details": "Павильон «Fiancée» очарует влюбленные пары, а павильон «Pirate» идеально подойдет для семей благодаря отличному расположению.",
            "amenities_title": "Включенные удобства",
            "specs": {
                "size": "Площадь",
                "capacity": "Вместимость",
                "bed": "Кровати",
                "wifi": "Бесплатный Wi-Fi",
                "courtesy": "Чайный набор",
                "hairdryer": "Фен",
                "products": "Косметические средства"
            },
            "garden_specs": {
                "size": "От 16 до 25 м²",
                "capacity": "От 1 до 4 человек",
                "bed": "Кровать Queen Size или две односпальные кровати"
            },
            "mer_specs": {
                "size": "От 16 до 31 м²",
                "capacity": "От 1 до 4 человек",
                "bed": "Кровать King Size или Queen Size"
            },
            "pavillons_specs": {
                "size": "20 или 26 м²",
                "capacity": "2 или 4 человека",
                "bed": "Кровать Queen Size или King Size"
            },
            "footer_question": "У вас есть вопросы об оснащении номеров?",
            "footer_cta": "Свяжитесь с нами"
        },
        "services": {
            "title": "Услуги и развлечения",
            "subtitle": "Все необходимое для незабываемого отдыха на Лазурном Берегу.",
            "hotel_services_title": "Услуги отеля",
            "hotel_services_desc": "Воспользуйтесь нашими высококлассными удобствами для полного расслабления.",
            "service_pool_title": "Бассейн и джакузи",
            "service_pool_desc": "Открытый бассейн, подогреваемый по сезону, и джакузи по запросу для приятного отдыха.",
            "service_garden_title": "Сад и террасы",
            "service_garden_desc": "Просторный средиземноморский сад с уютными уголками для чтения, отдыха или бокала вина.",
            "service_breakfast_title": "Завтрак «шведский стол»",
            "service_breakfast_desc": "Сервируется на террасе у моря. Свежие фермерские продукты для отличного начала вашего дня.",
            "service_cab_title": "Транспорт и экскурсии",
            "service_cab_desc": "Трансфер в аэропорт за 20 мин., автобусы в Ниццу и Монако рядом, а также наш партнер по частным перевозкам Myblackcab.",
            "activities_title": "Откройте для себя Вильфранш-сюр-Мер",
            "activities_desc": "Очаровательный приморский городок искусств и истории.",
            "citadelle_title": "Цитадель Сен-Эльм",
            "citadelle_desc": "Внушительная крепость XVI века, построенная для защиты залива. Сегодня здесь находятся мэрия и 4 музея (включая музей Вольти и музей Гетца-Буместера). Вход бесплатный.",
            "chapelle_title": "Часовня Сен-Пьер",
            "chapelle_desc": "Полностью отреставрированная и расписанная Жаном Кокто в 1956 году, эта часовня — шедевр искусства, посвященный покровителю рыбаков.",
            "rue_title": "Темная улица (Rue Obscure)",
            "rue_desc": "Крытая средневековая улица XIV века длиной 130 метров, когда-то служившая оборонительным проходом и запечатленная Кокто на картинах.",
            "port_title": "Королевский порт Ля-Дарс",
            "port_desc": "Историческая гавань XVI века со старинными укреплениями, маяком, канатной мастерской и действующей яхтенной пристанью.",
            "surroundings_title": "Что посмотреть вокруг",
            "surroundings_desc": "Наш отель — идеальная отправная точка для путешествий по Лазурному Берегу:",
            "surroundings_nice": "Ницца (10 мин): Старый город, цветочный рынок Кур Салейя и Английская набережная (легко добраться на автобусе).",
            "surroundings_monaco": "Монако (20 мин): Княжеский дворец, казино Монте-Карло и Океанографический музей.",
            "surroundings_villages": "Живописные средневековые деревни Эз и Сен-Поль-де-Ванс.",
            "surroundings_italy": "Италия всего в 7 остановках на поезде (регулярное расписание от вокзала Вильфранш)."
        },
        "gallery": {
            "title": "Фотогалерея",
            "subtitle": "Посмотрите на очаровательную территорию нашего бутик-отеля на фотографиях.",
            "filter_all": "Все",
            "filter_view": "Отель и виды",
            "filter_pool": "Бассейн и сад",
            "filter_rooms": "Номера",
            "filter_breakfast": "Завтрак"
        },
        "contact": {
            "title": "Связаться с нами",
            "subtitle": "Остались вопросы или есть особые пожелания? Наша команда всегда рада помочь.",
            "info_title": "Контактная информация",
            "info_address": "8 Boulevard de La Corne d'Or\nMoyenne Corniche\n06230 Villefranche-sur-Mer, Франция",
            "info_phone": "+33 4 93 76 67 40 / +33 7 45 28 29 37",
            "info_email": "info@fianceedupirate.com",
            "form_title": "Отправить сообщение",
            "form_name": "Полное имя",
            "form_email": "Электронная почта",
            "form_phone": "Номер телефона",
            "form_message": "Сообщение",
            "form_submit": "Отправить",
            "form_success": "Спасибо! Ваше сообщение успешно отправлено. Мы ответим вам в самое ближайшее время.",
            "form_error": "Произошла ошибка при отправке. Пожалуйста, попробуйте еще раз или напишите нам на почту.",
            "map_title": "Как нас найти"
        },
        "reviews": {
            "title": "Отзывы наших гостей",
            "subtitle": "Узнайте, что о нас пишут путешественники на TripAdvisor",
            "read_more": "Читать все отзывы на TripAdvisor",
            "items": [
                {
                    "author": "Софи Л.",
                    "date": "Июнь 2026",
                    "rating": 5,
                    "title": "Потрясающий вид и теплое гостеприимство",
                    "text": "Абсолютно волшебный отдых! Вид на залив Вильфранш с террасы во время завтрака просто невероятный. Отель тихий и уютный, персонал очень отзывчивый. Обязательно вернемся."
                },
                {
                    "author": "Томас М.",
                    "date": "Май 2026",
                    "rating": 5,
                    "title": "Маленький райский уголок",
                    "text": "Бассейн и джакузи с видом на море просто великолепны для расслабления после экскурсий. Номера современные, чистые и хорошо оборудованные. Идеальное расположение для путешествий."
                },
                {
                    "author": "Елена Р.",
                    "date": "Апрель 2026",
                    "rating": 5,
                    "title": "Абсолютное очарование и покой",
                    "text": "Отличный бутик-отель. Завтрак сытный и вкусный, на фоне открыточного пейзажа. Услуги трансфера от партнера Myblackcab были безупречны."
                }
            ]
        },
        "footer": {
            "desc": "La Fiancée du Pirate — уютный бутик-отель на 15 номеров, расположенный на холмах Вильфранш-сюр-Мер, между Ниццей и Монако.",
            "links_title": "Разделы",
            "contact_title": "Контакты",
            "social_title": "Мы в соцсетях",
            "rights": "Все права защищены. Правовая информация.",
            "tripadvisor_badge": "Оценка «Отлично» на TripAdvisor"
        },
        "seo": {
            "home_title": "La Fiancée du Pirate | Очаровательный бутик-отель Вильфранш-сюр-Мер",
            "home_desc": "Забронируйте отдых в La Fiancée du Pirate — бутик-отель на 15 номеров с панорамным видом на море, бассейном и джакузи в бухте Вильфранш.",
            "rooms_title": "Наши номера и павильоны | La Fiancée du Pirate",
            "rooms_desc": "Откройте для себя наши номера с садом и террасой, панорамные номера с видом на море и отдельные павильоны для уединенного отдыха.",
            "services_title": "Услуги и развлечения Лазурный Берег | La Fiancée du Pirate",
            "services_desc": "Ознакомьтесь с услугами нашего отеля (бассейн, джакузи, сад) и достопримечательностями в Вильфранш-сюр-Мер (цитадель, часовня Кокто).",
            "gallery_title": "Фотогалерея | La Fiancée du Pirate",
            "gallery_desc": "Посмотрите фотографии нашего отеля: бассейн с видом на море, панорамная терраса и комфортабельные отремонтированные номера.",
            "contact_title": "Контакты и схема проезда | La Fiancée du Pirate",
            "contact_desc": "Связаться с отелем La Fiancée du Pirate. Форма обратной связи, адрес, телефон, электронная почта и схема проезда."
        }
    }

    # Write files
    lang_data = {
        "fr": fr,
        "en": en,
        "de": de,
        "it": it,
        "es": es,
        "ru": ru,
        "en-au": en_au
    }
    
    for code, data in lang_data.items():
        filepath = os.path.join(translations_dir, f"{code}.json")
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Created translation file: {filepath}")

if __name__ == "__main__":
    create_translations()
