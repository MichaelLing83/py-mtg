import json
import encodings.utf_8
import sys

class MtgDataBase:
    '''
    An database containing all MTG cards.
    '''
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
    
    def get_all_card_names(self):
        '''
        Return a list of all card names.
        '''
        return self.__mtgDb.keys()
    
    def get_db(self):
        return self.__mtgDb
    
    def get_card_by_name(self, name):
        '''
        Get an card by it's precise name.
        '''
        return self.__mtgDb[name]
    
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

if __name__ == '__main__':
    mtgDb = MtgDataBase("../data/AllSets-x.json")
    card = mtgDb.get_card_by_name("Acidic Slime")
    print(mtgDb.print_card(card))