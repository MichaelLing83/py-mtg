import json
import encodings.utf_8

class MtgDataBase:
    '''
    An database containing all MTG cards.
    '''
    def __init__(self, json_file_name):
        '''
        '''
        dbFile = open(json_file_name, 'r', encoding="utf-8")
        self.mtgDb = json.load(dbFile)
        dbFile.close()
    
    def get_card_by_name(self, name):
        '''
        Get an card by it's precise name.
        '''
        for set_name in self.mtgDb.keys():
            for card in self.mtgDb.get(set_name).get("cards"):
                if card.get("name") == name:
                    return card
        raise ValueError('Card name "%s" is not found!' % name)
    
    def print_card(self, card):
        '''
        Return a string representation of a card (dict).
        '''
        s = ""
        for key in card.keys():
            if key != "foreignNames":
                s += "%s:\t%s\n" % (key, card.get(key))
        return s

if __name__ == '__main__':
    mtgDb = MtgDataBase("../data/AllSets-x.json")
    card = mtgDb.get_card_by_name("Acidic Slime")
    print(mtgDb.print_card(card))