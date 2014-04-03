
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
    
    def is_creature(self):
        '''
        Test if this is a creature.
        
        @return (bool): True or False
        '''
        return "Creature" in self.__card.get("type")