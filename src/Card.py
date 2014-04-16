import Constants

class Card:
    '''
    Representing one MTG card. This class should be used as the only card interface, and it should
    be used to abstract any interface about a card from MtgDataBase. So all methods of MtgDataBase
    that return a card instance or a list of card instances, this class should be used to represent
    a card.
    '''
    def __init__(self, raw_card):
        '''
        Initializer.
        
        @raw_card (dict): A dict object from MtgDataBase representing a card.
        '''
        self.__card = raw_card
    
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
    
    def to_str(self):
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
    
    def is_legal_in(self, format):
        '''
        Return whether this card is legal in given format. Note that if a card is not legal,
        it can be "Banned" or "Restricted".
        
        @format (str): Must be one of Constans.ALL_FORMATS
        
        @return (list): list of dict objects, each of which represents a card.
        '''
        if format not in Constants.ALL_FORMATS:
            raise ValueError("Given format '%s' is not valid! It has to be one of following:\n%s" % (format, MtgDataBase.ALL_FORMATS))
        legalities = self.__card.get("legalities")
        if type(legalities) is dict and legalities.get(format) == "Legal":
            return True
        return False
    
    def check_condition(self, card_condition):
        '''
        Check this card against given condition.
        
        @card_condition (CardCondition): a condition to check against.
        
        @return (bool): True or False
        '''
        for value_type, op, value_list in card_condition.get_conditions():
            if op == "in":
                if not self.__card.get(value_type) in value_list:
                    return False
        return True