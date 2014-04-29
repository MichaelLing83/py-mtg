import os

ALL_FORMATS = ("Classic", "Commander", "Extended", "Freeform", "Block", "Legacy", "Modern",
                "Prismatic", "Singleton 100", "Tribal Wars Legacy", "Tribal Wars Standard",
                "Vintage", "Standard")
ALL_CARD_TYPES = ("Creature", "Artifact", "Enchantment", "Sorcery", "Instant", "Legendary",
                    "Zombie", "Vampire", "Human", "Ooze", "Land")
ALL_KEYS = ("mana_cost",    # e.g. {2}{B}{R}, use this to match specific mana cost
            "cmc",  # converted mana cost
            "type", # e.g. Legendary Creature — Vampire
            "rulings",  # use this to match any rule on a card
            "colors",   # e.g. ['Black', 'Red']
            "name", # e.g. Olivia Voldaren
            "rarity",   # e.g. Mythic Rare
            "power",    # a number
            "toughness",    # a number
            "legalities",   # forms that this card is legal or illegal in
            "text", # printed text on this card
            )
ALL_COLORS = ("Black", "White", "Red", "Green", "Blue", "Colorless")
MAIN_DECK_MIN_SIZE = 60
SIDE_BOARD_MAX_SIZE = 15
MTG_JSON_FILE_PATH = "./data/AllSets-x.json"
PROJECT_ROOT = "py-mtg"