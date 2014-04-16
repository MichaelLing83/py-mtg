import unittest
from CardCondition import CardCondition
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
        pass
    
    def tearDown(self):
        pass
    
    def test_init(self):
        '''
        Verify that CardCondition can be initialized.
        '''
        card_condition = CardCondition()
    
    def test_add(self):
        '''
        Verify that we can add new condition.
        '''
        card_condition = CardCondition()
        card_condition.add("cmc", "in", (3,))
    
    def test_check(self):
        '''
        Verify that Card can be checked against a condition.
        '''
        card_condition = CardCondition()
        card_condition.add("cmc", "in", (4,))
        card = MtgDataBase.get_card_by_name("Olivia Voldaren")
        self.assertEqual(card.check_condition(card_condition), True)
        

if __name__ == '__main__':
    unittest.main()