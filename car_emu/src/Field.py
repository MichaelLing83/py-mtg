'''
'''

from Utilities import guarantee

class Field:
    '''
    Field class represents the field that a car is going to run in. It contains all the edges of the
    field, and also all obstacles on this field.
    '''
    
    def __init__(self, width, height):
        '''
        '''
        self.width = width
        self.height = height
        self.lines = list()
        
    def add_line(self, start_x, start_y, end_x, end_y):
        '''
        '''
        guarantee(start_x >= 0 and start_x <= self.width, "start_x=%d is out of range" % start_x)
        guarantee(start_y >= 0 and start_y <= self.height, "start_y=%d is out of range" % start_y)
        guarantee(end_x >= 0 and end_x <= self.width, "end_x=%d is out of range" % end_x)
        guarantee(end_y >= 0 and end_y <= self.height, "end_y=%d is out of range" % end_y)
        self.lines.append( (start_x, start_y, end_x, end_y) )
    
    def get_lines(self):
        '''
        '''
        return self.lines