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
        __cmc = self.__card.get("cmc")
        if __cmc:
            return int(self.__card.get("cmc"))
        else:
            return 0
    
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
        result = list()
        keys = set(Constants.ALL_KEYS)
        keys.discard("legalities")
        keys.discard("flavor")
        keys.discard("rulings")
        keys = list(keys)
        keys.sort()
        for key in ('name', 'type', 'mana_cost', 'cmc', 'rarity'):
            result.append(key + ":\t" + str(self.get(key)))
        if "Creature" in self.get("type"):
            result.append("power/toughness:\t%d/%d" % (self.get("power"), self.get("toughness")))
        result.append("text:\t%s" % self.get("text"))
        return "\n".join(result)
        #for key in self.__card.keys():
            #if key != "foreignNames":
                #s += "%s:\t%s\n" % (key, self.__card.get(key))
            #else:
                #sys.displayhook(card.get(key))
        #return s
    
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
        __mana_cost = self.__card.get("manaCost")
        if __mana_cost:
            return __mana_cost
        else:
            return ""
    
    @typecheck
    def type(self) -> str:
        return self.__card.get("type")
    
    @typecheck
    def rulings(self) -> str:
        result = list()
        rulings = self.__card.get("rulings")
        if not rulings:
            return ""
        for one_rule in rulings:
            result.append(one_rule['date'] + "\t" + one_rule['text'])
        return "\n".join(result)
    
    @typecheck
    def colors(self) -> str:
        #print(" ".join( self.__card.get("colors") ))
        colors = self.__card.get("colors")
        if not colors:
            return ""
        else:
            return " ".join(colors)
    
    @typecheck
    def rarity(self) -> str:
        return self.__card.get("rarity")
    
    @typecheck
    def power(self) -> int:
        power = self.__card.get("power")
        if not power:
            return 0
        elif not power.isnumeric():
            return 0
        else:
            return int(power)
    
    @typecheck
    def toughness(self) -> int:
        toughness = self.__card.get("toughness")
        if not toughness:
            return 0
        elif not toughness.isnumeric():
            return 0
        else:
            return int(toughness)
    
    @typecheck
    def legalities(self) -> str:
        result = list()
        legalities = self.__card.get("legalities")
        # if there is no legalities information, just return an empty string
        if not legalities:
            return ""
        for form in legalities.keys():
            if self.__card.get("legalities")[form] == "Legal":
                result.append(form)
        return " ".join(result)
    
    @typecheck
    def text(self) -> str:
        text = self.__card.get("text")
        if not text:
            return ""
        else:
            return text
    
    @typecheck
    def flavor(self) -> str:
        flavor = self.__card.get("flavor")
        if not flavor:
            return ""
        else:
            return flavor
    
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
            "flavor": lambda: self.flavor(),    # flavor text
            }[key]()