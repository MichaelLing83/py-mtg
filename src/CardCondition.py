from typecheck import *

class CardCondition:
    '''
    A condition class, whose instance can be used to check against a card.
    '''
    
    @typecheck
    def __init__(self) -> nothing:
        self.__condition_list = list()
    
    @typecheck
    def add(self, value_type: one_of("cmc", "type", "color"),
            op: one_of("in"),
            value_list: tuple) -> nothing:
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
    def get_conditions(self) -> list:
        return self.__condition_list