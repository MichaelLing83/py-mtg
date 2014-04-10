import json

class MtgDataBase:
    '''
    An database containing all MTG cards.
    '''
    ALL_FORMATS = ("Classic", "Commander", "Extended", "Freeform", "Block", "Legacy", "Modern",
                    "Prismatic", "Singleton 100", "Tribal Wars Legacy", "Tribal Wars Standard",
                    "Vintage", "Standard")
    def __init__(self, json_file_name):
        '''
        '''
        dbFile = open(json_file_name, 'r', encoding="utf-8")
        self.__rawMtgDb = json.load(dbFile)
        dbFile.close()
        self.__mtgDb = dict()
        for set_name in self.__rawMtgDb.keys():
            for card in self.__rawMtgDb.get(set_name).get("cards"):
                if card.get("name") not in self.__mtgDb.keys():
                    self.__mtgDb[card.get("name")] = card
        self.__all_card_names = list(self.__mtgDb.keys())
        self.__all_card_names.sort()
    
    def get_all_card_names(self):
        '''
        Return a list of all card names.
        '''
        return self.__all_card_names
    
    def get_card_by_name(self, name):
        '''
        Get an card by it's precise name.
        '''
        return self.__mtgDb[name]
    
    def get_card_by_similar_name(self, partial_name):
        '''
        Get a list of cards with similar names.
        '''
        cards = list()
        for name in self.get_all_card_names():
            if partial_name.upper() in name.upper():
                cards.append(self.get_card_by_name(name))
        return cards
    
    def print_card(self, card):
        '''
        Return a string representation of a card (dict).
        '''
        s = ""
        for key in card.keys():
            if key != "foreignNames":
                s += "%s:\t%s\n" % (key, card.get(key))
            #else:
                #sys.displayhook(card.get(key))
        return s
    
    def get_cards_by_format(self, format):
        '''
        Return a list of all cards of given format.
        
        @format (str): Must be one of following
            Classic, Commander, Extended, Freeform, Block, Legacy, Modern, Prismatic, Singleton 100,
            Tribal Wars Legacy, Tribal Wars Standard, Vintage
        
        @return (list): list of dict objects, each of which represents a card.
        '''
        if format not in MtgDataBase.ALL_FORMATS:
            raise ValueError("Given format '%s' is not valid! It has to be one of following:\n%s" % (format, MtgDataBase.ALL_FORMATS))
        cards = list()
        for name in self.get_all_card_names():
            card = self.get_card_by_name(name)
            legalities = card.get("legalities")
            if type(legalities) is dict and legalities.get(format) == "Legal":
                cards.append(card)
        return cards
