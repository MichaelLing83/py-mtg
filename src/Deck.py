import Constants
from typecheck import *
from MtgDataBase import MtgDataBase
from Utilities import MtgException
from Utilities import guarantee
from CardCondition import CardCondition

class Deck:
    '''
    Representing a MTG deck, with facilitating methods.
    '''
    
    @typecheck
    def __init__(self, deck_list_str: str="", file_name: str="") -> nothing:
        '''
        Initialize a Deck instance from given deck list text.
        
        @deck_list_str (str): in format of "MTGO/Apprentice" from TCGPlayer site, e.g.
            4 Arid Mesa
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
            1 Tectonic Edge
        
        @return (Deck): a Deck instance
        '''
        # check input is valid
        if deck_list_str and file_name:
            raise MtgException("Deck cannot be initialized from a deck_list_str and a file_name!")
        elif not (deck_list_str or file_name):
            raise MtgException("Deck cannot be initialized! A deck_list_str or a file_name must be given!")
        
        if deck_list_str:
            self.__deck_list_text = deck_list_str.splitlines()
        if file_name:
            deck_file = open(file_name, "r", encoding="utf8")
            self.__deck_list_text = list()
            for l in deck_file.readlines():
                if len(l) >0:
                    self.__deck_list_text.append(l)
        self.__main_deck_dict = dict()
        self.__side_board_dict = dict()
        
        # parse and initialize all cards in the deck
        is_main_deck = True
        for line in self.__deck_list_text:
            #print("line = %s" % line)
            line = line.strip()
            if line.upper() == u"SIDEBOARD":
                is_main_deck = False
            else:
                num_of_card = int(line[0])
                guarantee(num_of_card > 0 and num_of_card < 5)
                name_of_card = line[1:].strip()
                #print("line = %s" % line)
                #print("name_of_card = %s" % name_of_card)
                guarantee(MtgDataBase.get_card_by_name(name_of_card) != None,
                    "Card name couldn't be found: %s" % name_of_card)
                if is_main_deck:
                    # add to main deck
                    guarantee(name_of_card not in self.__main_deck_dict.keys(),
                        "Card '%s' is defined multiple times for main deck!" % name_of_card)
                    self.__main_deck_dict[name_of_card] = num_of_card
                else:
                    # add to side board
                    guarantee(name_of_card not in self.__side_board_dict.keys(),
                        "Card '%s' is defined multiple times for side board!" % name_of_card)
                    self.__side_board_dict[name_of_card] = num_of_card
        # check the deck meets basic requirements
        c = 0
        for card_number in self.__main_deck_dict.values():
            c += card_number
        guarantee(c >= Constants.MAIN_DECK_MIN_SIZE,
            "Main deck needs at least %d cards, but it has only %d." % (Constants.MAIN_DECK_MIN_SIZE, c))
        c = 0
        for card_number in self.__side_board_dict.values():
            c += card_number
        guarantee(c <= Constants.SIDE_BOARD_MAX_SIZE,
            "Side board can have at most %d cards, but it has %d." % (Constants.SIDE_BOARD_MAX_SIZE, c))
    
    @typecheck
    def count(self, condition: CardCondition) -> int:
        '''
        Count how many cards in main deck meet given condition.
        
        @condition (CardCondition): a condition object to use for matching
        
        @return (int): number of cards in main deck that meet given condition.
        '''
        c = 0
        for card_name in self.__main_deck_dict.keys():
            if condition.check_card(MtgDataBase.get_card_by_name(card_name)):
                c += self.__main_deck_dict[card_name]
        return c