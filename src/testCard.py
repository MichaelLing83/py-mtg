import unittest
from MtgDataBase import MtgDataBase
from Card import Card

class TestCard(unittest.TestCase):

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
    
    def test_init(self):
        '''
        Verify that Card can be initialized.
        '''
        card = Card(self.mtgDb.get_card_by_name("Acidic Slime"))
    
    def test_name(self):
        '''
        Verify that Card give us the right name.
        '''
        card = Card(self.mtgDb.get_card_by_name("Acidic Slime"))
        self.assertEqual(card.name(), "Acidic Slime")
        self.assertEqual(card.name(language="Chinese Simplified"), "酸液黏菌")
    
    def test_check_type(self):
        '''
        Verify that Card can test its types.
        '''
        card = Card(self.mtgDb.get_card_by_name("Olivia Voldaren"))
        self.assertEqual(card.check_type("Vampire"), True)
        self.assertEqual(card.check_type("Legendary"), True)
        self.assertEqual(card.check_type("Zombie"), False)
        self.assertEqual(card.check_type("Creature"), True)
        self.assertEqual(card.check_type("Artifact"), False)
        self.assertEqual(card.check_type("Instant"), False)
    
    def test_cmc(self):
        '''
        Verify that Card can get its CMC.
        '''
        self.assertEqual(Card(self.mtgDb.get_card_by_name("Olivia Voldaren")).cmc(), 4)
    
    def test_check_color(self):
        '''
        Verify that Card can check if it has a given color.
        '''
        card = Card(self.mtgDb.get_card_by_name("Olivia Voldaren"))
        self.assertEqual(card.check_color("Black"), True)
        self.assertEqual(card.check_color("Red"), True)
        self.assertEqual(card.check_color("White"), False)
        self.assertEqual(card.check_color("Blue"), False)
        self.assertEqual(card.check_color("Green"), False)
        self.assertEqual(card.check_color("Colorless"), False)
        card = Card(self.mtgDb.get_card_by_name("Wooden Stake"))
        self.assertEqual(card.check_color("Black"), False)
        self.assertEqual(card.check_color("Red"), False)
        self.assertEqual(card.check_color("White"), False)
        self.assertEqual(card.check_color("Blue"), False)
        self.assertEqual(card.check_color("Green"), False)
        self.assertEqual(card.check_color("Colorless"), True)
        

if __name__ == '__main__':
    unittest.main()