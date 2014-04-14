﻿import unittest
from Deck import Deck

class TestDeck(unittest.TestCase):

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
        Initialize a deck from a deck list string.
        '''
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
        deck = Deck(bw_token_modern_deck_list)
        self.assertNotEqual(deck, None)

if __name__ == '__main__':
    unittest.main()