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
        self.assertEqual(card_condition.check_card(card), True)
    
    def test_more_check(self):
        '''
        Verify all key and op combination works:
        ALL_KEYS = ("mana_cost",    # e.g. {2}{B}{R}, use this to match specific mana cost
            "cmc",  # converted mana cost
            "type", # e.g. Legendary Creature — Vampire
            "rulings",  # use this to match any rule on a card
            "colors",   # e.g. ['Black', 'Red']
            "name", # e.g. Olivia Voldaren
            "rarity",   # e.g. Mythic Rare
            "power",    # a number
            "toughness",    # a number
            "legalities",   # forms that this card is legal in
            "text", # printed text on this card
            )
        OPS = ("have", "not have",  # key op B => key field (not) have value B
            "in", "not in", # key op B => key field (not) in given set B
            "<", ">", "==", "<=", ">=", "!=",
            "match", "not match"    # key op B => key field (not) match given regRex
            )
        '''
        card_condition = CardCondition()
        card_condition.add("mana_cost", "have", "{B}{R}")
        card_condition.add("cmc", "in", (4,5,6))
        card_condition.add("cmc", "not in", (1,2,3))
        card_condition.add("cmc", "<", 10)
        card_condition.add("cmc", "<=", 10)
        card_condition.add("cmc", "==", 4)
        card_condition.add("cmc", ">", 2)
        card_condition.add("cmc", ">=", 1)
        card_condition.add("cmc", "!=", 5)
        card_condition.add("type", "have", "Creature")
        card_condition.add("type", "not have", "Enchantment")
        card_condition.add("type", "match", "Creature")
        card_condition.add("type", "not match", "Enchantment")
        card_condition.add("rulings", "have", "gain control")
        card_condition.add("rulings", "not have", "destroy")
        card_condition.add("rulings", "match", "gain control")
        card_condition.add("rulings", "not match", "destroy")
        card_condition.add("colors", "have", "Black")
        card_condition.add("colors", "not have", "Green")
        card_condition.add("name", "have", "Olivia")
        card_condition.add("name", "not have", "God")
        card_condition.add("rarity", "have", "Rare")
        card_condition.add("rarity", "not have", "Common")
        card_condition.add("power", ">", 2)
        card_condition.add("legalities", "have", "Modern")
        card_condition.add("text", "have", "+1")
        card = MtgDataBase.get_card_by_name("Olivia Voldaren")
        self.assertEqual(card_condition.check_card(card), True)
        self.assertEqual(card_condition.check_card(MtgDataBase.get_card_by_name("Baloth Woodcrasher")), False)

if __name__ == '__main__':
    unittest.main()