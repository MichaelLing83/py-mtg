import json
import Constants
from typecheck import *
from Card import Card

class MtgDataBase:
    '''
    An database containing all MTG cards. And this class should never be instantiated.
    
    This MTG card database is initialized from one json file from http://mtgjson.com/
    Thanks so much to Robert (robert@cosmicrealms.com).
    '''
    
    dbFile = open(Constants.MTG_JSON_FILE_PATH, 'r', encoding="utf-8")
    __rawMtgDb = json.load(dbFile)
    dbFile.close()
    __mtgDb = dict()
    for set_name in __rawMtgDb.keys():
        for card in __rawMtgDb.get(set_name).get("cards"):
            if card.get("name") not in __mtgDb.keys():
                __mtgDb[card.get("name")] = Card(card)
    __all_card_names = list(__mtgDb.keys())
    __all_card_names.sort()
    
    @typecheck
    def __init__(self) -> nothing:
        '''
        This class should never be instantiated.
        '''
        raise ValueError("MtgDataBase class should never be initialized!")
    
    @classmethod
    @typecheck
    def get_all_card_names(cls) -> list:
        '''
        Return a list of all card names.
        '''
        return MtgDataBase.__all_card_names
    
    @classmethod
    @typecheck
    def get_card_by_name(cls, name: str) -> Card:
        '''
        Get an card by it's precise name.
        '''
        return MtgDataBase.__mtgDb[name]
    
    @classmethod
    @typecheck
    def get_card_by_similar_name(cls, partial_name: str) -> list:
        '''
        Get a list of cards with similar names.
        '''
        cards = list()
        for name in MtgDataBase.get_all_card_names():
            if partial_name.upper() in name.upper():
                cards.append(MtgDataBase.get_card_by_name(name))
        return cards
    
    @classmethod
    @typecheck
    def get_cards_by_format(cls, format: one_of(Constants.ALL_FORMATS)) -> list:
        '''
        Return a list of all cards of given format.
        
        @format (str): Must be one of Constants.ALL_FORMATS
        
        @return (list): list of dict objects, each of which represents a card.
        '''
        if format not in Constants.ALL_FORMATS:
            raise ValueError("Given format '%s' is not valid! It has to be one of following:\n%s" % (format, MtgDataBase.ALL_FORMATS))
        cards = list()
        for name in MtgDataBase.get_all_card_names():
            card = MtgDataBase.get_card_by_name(name)
            if card.is_legal_in(format):
                cards.append(card)
        return cards
