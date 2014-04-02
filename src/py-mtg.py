import json
import encodings.utf_8

class MtgDataBase:
    '''
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

if __name__ == '__main__':
    mtgDb = MtgDataBase("../data/AllSets-x.json")
    card = mtgDb.get_card_by_name("Acidic Slime")
    for key in card.keys():
        if key != "foreignNames":
            print("%s:\t%s" % (key, card.get(key)))