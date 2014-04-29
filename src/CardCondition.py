﻿from typecheck import *
import Constants
from Card import Card
from Utilities import MtgException

class CardCondition:
    '''
    A condition class, whose instance can be used to check against a card.
    '''
    OPS = ("have", "not have",  # key op B => key field (not) have value B
            "in", "not in", # key op B => key field (not) in given set B
            "<", ">", "==", "<=", ">=", "!=",
            "match", "not match"    # key op B => key field (not) match given regRex
            )
    
    @typecheck
    def __init__(self) -> nothing:
        self.__condition_list = list()
    
    @typecheck
    def add(self, value_type: one_of(Constants.ALL_KEYS),
            op: one_of(OPS),
            value_list: either(tuple, int, str)) -> nothing:
        '''
        Add a condition, e.g.:
            "cmc", "in", (4, 5)
            should give a condition that card's cmc is either 4 or 5.
        
        @value_type (str): type of value to check against, e.g.:
            cmc, type, color
        @op (str): condition operator, e.g.: in, not in
        @value_list (tuple): tuple of values.
        
        @return (bool): True or False
        '''
        self.__condition_list.append( (value_type, op, value_list) )
    
    @typecheck
    def check_card(self, card: Card) -> bool:
        result = True
        for key, op, value in self.__condition_list:
            try:    # check one condition
                result = result and {
                    'have': lambda key, value: value in card.get(key),
                    'not have': lambda key, value: value not in card.get(key),
                    'in': lambda key, value: card.get(key) in value,
                    'not in': lambda key, value: card.get(key) not in value,
                    '<': lambda key, value: card.get(key) < value,
                    '>': lambda key, value: card.get(key) > value,
                    '==': lambda key, value: card.get(key) == value,
                    '<=': lambda key, value: card.get(key) <= value,
                    '>=': lambda key, value: card.get(key) >= value,
                    '!=': lambda key, value: card.get(key) != value,
                    'match': lambda key, value: value in card.get(key),
                    'not match': lambda key, value: value not in card.get(key),
                }[op](key, value)
            except MtgException:
                raise MtgException("Condition \"%s %s %s\" is not legal!" % (key, op, value))
        return result
    
    @typecheck
    def get_conditions(self) -> list:
        return self.__condition_list