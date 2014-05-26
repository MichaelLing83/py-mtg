import unittest
from MtgDataBase import MtgDataBase
from CardCondition import CardCondition

class TestMtgDataBase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\nStart testing %s" % __name__)
    
    @classmethod
    def tearDownClass(cls):
        print("\nFinish testing %s" % __name__)
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_get_all_card_names(self):
        '''
        Verify that MtgDataBase can give a list of all card names.
        '''
        self.assertEqual(type(MtgDataBase.get_all_card_names()), list)
        self.assertGreaterEqual(len(MtgDataBase.get_all_card_names()), 14096)
    
    def test_get_card_by_name(self):
        '''
        Verify that MtgDataBase can give us a card by its exact English name.
        '''
        card = MtgDataBase.get_card_by_name("Acidic Slime")
        self.assertEqual(card.cmc(), 5)
    
    def test_get_card_with_similar_name(self):
        '''
        Verify that MtgDataBase can give us a list of cards by a partial name, case insensitive.
        '''
        cards = MtgDataBase.get_card_by_similar_name("honor")
        card = MtgDataBase.get_card_by_name("Honor of the Pure")
        self.assertIn(card, cards)
    
    def test_print_card(self):
        '''
        Verify that MtgDataBase can give us a string representing a given card.
        '''
        card = MtgDataBase.get_card_by_name("Acidic Slime")
        self.assertGreater(len(card.to_str()), 50)
    
    def test_get_cards_by_format(self):
        '''
        Verify that MtgDataBase can give us a list of cards based on given format.
        '''
        cards = MtgDataBase.get_cards_by_format("Standard")
        self.assertGreater(len(cards), 100)
        self.assertIn(MtgDataBase.get_card_by_name("Swamp"), cards)
        self.assertIn(MtgDataBase.get_card_by_name("Doom Blade"), cards)
    
    def test_get_cards(self):
        '''
        Verify that MtgDataBase can give us a list of cards based on given condition.
        '''
        condition = CardCondition()
        condition.add("cmc", "==", 10)
        cards = MtgDataBase.get_cards(condition)
        self.assertGreater(len(cards), 0)
        condition = CardCondition()
        condition.add("colors", "have", "Red")
        cards = MtgDataBase.get_cards(condition)
        self.assertGreater(len(cards), 0)
    

if __name__ == '__main__':
    unittest.main()