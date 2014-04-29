'''
Classes for a MTG game. If any class became too big, it should be split out to a seperate file.
'''

from typecheck import *
from Utilities import MtgException

class Battlefield:
    '''
    This class should never be instantiated, since this class object is used to hold all the data
    and status.
    '''

    def __init__(self, *p, **k):
        raise MtgException("%s class should never be instantiated!" % __class__)

class SpellAndAbilityStack:
    '''
    This class should never be instantiated, since this class object is used to hold all the data
    and status.
    '''

    def __init__(self, *p, **k):
        raise MtgException("%s class should never be instantiated!" % __class__)

class Judge:
    '''
    This class should never be instantiated, since this class object is used to hold all the data
    and status.
    
    Judge:
        knows all the rules;
        execute all instructions in the game (e.g. resolve a spell/ability, perform state-based
            actions, etc.)
        any action in the game should involve the Judge
    '''

    def __init__(self, *p, **k):
        raise MtgException("%s class should never be instantiated!" % __class__)

class Player:
    '''
    A MTG player.
    '''
    def __init__(self):
        pass

class Graveyard:
    '''
    A MTG graveyard.
    '''
    def __init__(self):
        pass

class Event:
    '''
    A MTG event that occurs in the game.
    '''
    def __init__(self):
        pass