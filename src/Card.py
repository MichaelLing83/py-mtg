import Constants
from typecheck import *

class Card:
    '''
    Representing one MTG card. This class should be used as the only card interface, and it should
    be used to abstract any interface about a card from MtgDataBase. So all methods of MtgDataBase
    that return a card instance or a list of card instances, this class should be used to represent
    a card.
    '''
    
    @typecheck
    def __init__(self, raw_card: dict) -> nothing:
        '''
        Initializer.
        
        @raw_card (dict): A dict object from MtgDataBase representing a card.
        '''
        self.__card = raw_card
    
    @typecheck
    def name(self, language: str ="English") -> str:
        '''
        Get name of this card.
        
        @language="English" (str): in which language to get name. Can be one of the following:
            'Chinese Simplified'
            'Chinese Traditional'
            'French'
            'German'
            'Italian'
            'Japanese'
            'Korean'
            'Portuguese (Brazil)'
            'Russian'
            'Spanish'
        
        @return (str): name of this card.
        '''
        if language == "English":
            return self.__card.get("name")
        else:
            for language_name in self.__card.get("foreignNames"):
                if language in language_name.get("language"):
                    return language_name.get("name")
        raise ValueError("%s name is not found for card %s" % (language, self.__card.get("name")))
    
    @typecheck
    def check_type(self, target_type: one_of(Constants.ALL_CARD_TYPES)) -> bool:
        '''
        Check if this card has given target_type.
        
        @target_type (str): type to check against, can be one of:
            Creature, Artifact, Enchantment, Sorcery, Instant
            Legendary
            Zombie, Vampire, Human, Ooze
        
        @return (bool): True or False
        '''
        return target_type in self.__card.get("type")
    
    @typecheck
    def cmc(self) -> int:
        '''
        Get Converted Mana Cost for this card.
        
        @return (int): CMC of the card.
        '''
        return self.__card.get("cmc")
    
    @typecheck
    def check_color(self, color: one_of(Constants.ALL_COLORS)) -> bool:
        '''
        Check if this card has given color.
        
        @color (str): color to check, has to be one of following
            Black, White, Red, Green, Blue, Colorless
        
        @return (bool): whether this card has given color.
        '''
        if color == "Colorless":
            return "colors" not in self.__card.keys()
        elif color in ("Black", "White", "Red", "Blue", "Green"):
            if "colors" not in self.__card.keys():
                return False
            else:
                return color in self.__card.get("colors")
        raise ValueError("%s is not a valid color!" % color)
    
    @typecheck
    def to_str(self) -> str:
        '''
        Return a string representation of this card.
        '''
        s = ""
        for key in self.__card.keys():
            if key != "foreignNames":
                s += "%s:\t%s\n" % (key, self.__card.get(key))
            #else:
                #sys.displayhook(card.get(key))
        return s
    
    @typecheck
    def is_legal_in(self, format: one_of(Constants.ALL_FORMATS)) -> bool:
        '''
        Return whether this card is legal in given format. Note that if a card is not legal,
        it can be "Banned" or "Restricted".
        
        @format (str): Must be one of Constants.ALL_FORMATS
        
        @return (list): list of dict objects, each of which represents a card.
        '''
        if format not in Constants.ALL_FORMATS:
            raise ValueError("Given format '%s' is not valid! It has to be one of following:\n%s" % (format, MtgDataBase.ALL_FORMATS))
        legalities = self.__card.get("legalities")
        if type(legalities) is dict and legalities.get(format) == "Legal":
            return True
        return False
    
    @typecheck
    def mana_cost(self) -> str:
        return self.__card.get("manaCost")
    
    @typecheck
    def type(self) -> str:
        return self.__card.get("type")
    
    @typecheck
    def rulings(self) -> str:
        result = list()
        for one_rule in self.__card.get("rulings"):
            result.append(one_rule['date'] + "\t" + one_rule['text'])
        return "\n".join(result)
    
    @typecheck
    def colors(self) -> str:
        return " ".join( self.__card.get("colors") )
    
    @typecheck
    def rarity(self) -> str:
        return self.__card.get("rarity")
    
    @typecheck
    def power(self) -> int:
        return int(self.__card.get("power"))
    
    @typecheck
    def toughness(self) -> int:
        return int(self.__card.get("toughness"))
    
    @typecheck
    def legalities(self) -> str:
        result = list()
        for form in self.__card.get("legalities").keys():
            if self.__card.get("legalities")[form] == "Legal":
                result.append(form)
        return " ".join(result)
    
    @typecheck
    def text(self) -> str:
        return self.__card.get("text")
    
    @typecheck
    def get(self, key: one_of(Constants.ALL_KEYS)) -> either(int, str):
        return {
            "mana_cost": lambda: self.mana_cost(),    # e.g. {2}{B}{R}, use this to match specific mana cost
            "cmc": lambda: self.cmc(),  # converted mana cost
            "type": lambda: self.type(), # e.g. Legendary Creature — Vampire
            "rulings": lambda: self.rulings(),  # use this to match any rule on a card
            "colors": lambda: self.colors(),   # e.g. ['Black', 'Red']
            "name": lambda: self.name(), # e.g. Olivia Voldaren
            "rarity": lambda: self.rarity(),   # e.g. Mythic Rare
            "power": lambda: self.power(),    # a number
            "toughness": lambda: self.toughness(),    # a number
            "legalities": lambda: self.legalities(),   # forms that this card is legal or illegal in
            "text": lambda: self.text(), # printed text on this card
            }[key]()