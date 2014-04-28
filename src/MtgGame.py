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
        raise MtgException("Battlefield class should never be instantiated!")

class SpellAndAbilityStack:
    '''
    This class should never be instantiated, since this class object is used to hold all the data
    and status.
    '''

    def __init__(self, *p, **k):
        raise MtgException("Battlefield class should never be instantiated!")

class Judge:
    '''
    This class should never be instantiated, since this class object is used to hold all the data
    and status.
    '''

    def __init__(self, *p, **k):
        raise MtgException("Battlefield class should never be instantiated!")