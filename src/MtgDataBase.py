import json
import Constants
from Card import Card

class MtgDataBase:
    '''
    An database containing all MTG cards.
    '''
    def __init__(self, json_file_name):
        '''
        Initialize a MTG card database from one json file from http://mtgjson.com/
        Thanks so much to Robert (robert@cosmicrealms.com).
        
        @json_file_name (str): path to the json file.
        
        @return (MtgDataBase): an MtgDataBase instance, which contains a internal dict of
                                card_name (str) -> Card instance
                               pairs.
        '''
        dbFile = open(json_file_name, 'r', encoding="utf-8")
        self.__rawMtgDb = json.load(dbFile)
        dbFile.close()
        self.__mtgDb = dict()
        for set_name in self.__rawMtgDb.keys():
            for card in self.__rawMtgDb.get(set_name).get("cards"):
                if card.get("name") not in self.__mtgDb.keys():
                    self.__mtgDb[card.get("name")] = Card(card)
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
    
    def get_cards_by_format(self, format):
        '''
        Return a list of all cards of given format.
        
        @format (str): Must be one of Constants.ALL_FORMATS
        
        @return (list): list of dict objects, each of which represents a card.
        '''
        if format not in Constants.ALL_FORMATS:
            raise ValueError("Given format '%s' is not valid! It has to be one of following:\n%s" % (format, MtgDataBase.ALL_FORMATS))
        cards = list()
        for name in self.get_all_card_names():
            card = self.get_card_by_name(name)
            if card.is_legal_in(format):
                cards.append(card)
        return cards
