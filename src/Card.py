
class Card:
    '''
    Representing one MTG card.
    '''
    def __init__(self, mtgDb, name):
        '''
        Initializer.
        
        @mtgDb (MtgDataBase): the database containing all cards.
        @name (str): name of the card.
        '''
        self.__name = name
        self.__mtgDb = mtgDb
        self.__card = self.__mtgDb.get_card_by_name(self.__name)
    
    def name(self, language="English"):
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
    
    def check_type(self, target_type):
        '''
        Check if this card has given target_type.
        
        @target_type (str): type to check against, can be one of:
            Creature, Artifact, Enchantment, Sorcery, Instant
            Legendary
            Zombie, Vampire, Human, Ooze
        
        @return (bool): True or False
        '''
        return target_type in self.__card.get("type")
    
    def cmc(self):
        '''
        Get Converted Mana Cost for this card.
        
        @return (int): CMC of the card.
        '''
        return self.__card.get("cmc")
    
    def check_color(self, color):
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