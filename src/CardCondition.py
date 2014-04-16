
class CardCondition:
    '''
    A condition class, whose instance can be used to check against a card.
    '''
    
    def __init__(self):
        self.__condition_list = list()
    
    def add(self, value_type, op, value_list):
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
    
    def get_conditions(self):
        return self.__condition_list