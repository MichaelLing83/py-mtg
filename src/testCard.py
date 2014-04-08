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
        card = Card(self.mtgDb, "Acidic Slime")
    
    def test_name(self):
        '''
        Verify that Card give us the right name.
        '''
        card = Card(self.mtgDb, "Acidic Slime")
        self.assertEqual(card.name(), "Acidic Slime")
        self.assertEqual(card.name(language="Chinese Simplified"), "酸液黏菌")
    
    def test_check_type(self):
        '''
        Verify that Card can test its types.
        '''
        self.assertEqual(Card(self.mtgDb, "Olivia Voldaren").check_type("Vampire"), True)
        self.assertEqual(Card(self.mtgDb, "Olivia Voldaren").check_type("Legendary"), True)
        self.assertEqual(Card(self.mtgDb, "Olivia Voldaren").check_type("Zombie"), False)
        self.assertEqual(Card(self.mtgDb, "Olivia Voldaren").check_type("Creature"), True)
        self.assertEqual(Card(self.mtgDb, "Olivia Voldaren").check_type("Artifact"), False)
        self.assertEqual(Card(self.mtgDb, "Olivia Voldaren").check_type("Instant"), False)
        

if __name__ == '__main__':
    unittest.main()