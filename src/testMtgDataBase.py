import unittest
from MtgDataBase import MtgDataBase

class TestMtgDataBase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\nStart testing %s" % __name__)
    
    @classmethod
    def tearDownClass(cls):
        print("\nFinish testing %s" % __name__)
    
    def setUp(self):
        self.mtgDb = MtgDataBase("../data/AllSets-x.json")
    
    def tearDown(self):
        pass
    
    def test_get_all_card_names(self):
        '''
        Verify that MtgDataBase can give a list of all card names.
        '''
        self.assertEqual(type(self.mtgDb.get_all_card_names()), list)
        self.assertEqual(len(self.mtgDb.get_all_card_names()), 14096)
    
    def test_get_card_by_name(self):
        '''
        Verify that MtgDataBase can give us a card by its exact English name.
        '''
        card = self.mtgDb.get_card_by_name("Acidic Slime")
        self.assertEqual(card.get("cmc"), 5)
    
    def test_get_card_with_similar_name(self):
        '''
        Verify that MtgDataBase can give us a list of cards by a partial name, case insensitive.
        '''
        cards = self.mtgDb.get_card_by_similar_name("honor")
        card = self.mtgDb.get_card_by_name("Honor of the Pure")
        self.assertIn(card, cards)
    
    def test_print_card(self):
        '''
        Verify that MtgDataBase can give us a string representing a given card.
        '''
        card = self.mtgDb.get_card_by_name("Acidic Slime")
        self.assertGreater(len(self.mtgDb.print_card(card)), 50)
    
    def test_get_cards_by_format(self):
        '''
        Verify that MtgDataBase can give us a list of cards based on given format.
        '''
        cards = self.mtgDb.get_cards_by_format("Standard")
        self.assertGreater(len(cards), 100)
        self.assertIn(self.mtgDb.get_card_by_name("Swamp"), cards)
        self.assertIn(self.mtgDb.get_card_by_name("Doom Blade"), cards)
    
    

if __name__ == '__main__':
    unittest.main()