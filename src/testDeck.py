import unittest
from Deck import Deck
from CardCondition import CardCondition

class TestDeck(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\nStart testing %s" % __name__)
    
    @classmethod
    def tearDownClass(cls):
        print("\nFinish testing %s" % __name__)
    
    def setUp(self):
        bw_token_modern_deck_list = '''4 Arid Mesa
4 Doom Blade
2 Engineered Explosives
3 Fetid Heath
4 Godless Shrine
4 Honor of the Pure
2 Inquisition of Kozilek
3 Isolated Chapel
4 Lingering Souls
4 Marsh Flats
4 Path to Exile
2 Plains
4 Spectral Procession
4 Squadron Hawk
1 Swamp
3 Sword of War and Peace
3 Tectonic Edge
4 Thoughtseize
1 Vault of the Archangel
Sideboard
3 Disenchant
2 Grafdigger's Cage
3 Liliana of the Veil
3 Rest in Peace
3 Stony Silence
1 Tectonic Edge'''
        self.deck = Deck(deck_list_str=bw_token_modern_deck_list)
    
    def tearDown(self):
        pass
    
    def test_init_from_str(self):
        '''
        Initialize a deck from a deck list string.
        '''
        self.assertNotEqual(self.deck, None)
    
    def test_init_from_file(self):
        '''
        Initialize a deck from a deck list file.
        '''
        self.assertNotEqual(Deck(file_name="data/BW_Token_Modem.deck"), None)
    
    def test_count(self):
        '''
        Verify that Deck can count cards by type correctly.
        '''
        self.assertEqual(self.deck.count(CardCondition("type", "have", "Land")), 25)
        self.assertEqual(self.deck.count(CardCondition("type", "have", "Creature")), 4)
        self.assertEqual(self.deck.count(CardCondition("type", "have", "Instant")), 8)
        self.assertEqual(self.deck.count(CardCondition("type", "have", "Enchantment")), 4)
        self.assertEqual(self.deck.count(CardCondition("type", "have", "Artifact")), 5)
        self.assertEqual(self.deck.count(CardCondition("type", "have", "Sorcery")), 14)

if __name__ == '__main__':
    unittest.main()