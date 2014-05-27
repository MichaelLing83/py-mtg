'''
'''

from Utilities import guarantee

class Field:
    '''
    Field class represents the field that a car is going to run in. It contains all the edges of the
    field, and also all obstacles on this field.
    '''
    
    def __init__(self, file_name):
        '''
        '''
        file = open(file_name, 'r', encoding="utf-8")
        guarantee(file.closed == False, "file %s is closed unexpectedly" % file_name)
        current_section = None
        self.width = 0
        self.height = 0
        self.lines = list()
        for line in file.readlines():
            line = line.strip()
            if len(line) == 0 or line[0] == '#':
                # this is a comment line, go to next line
                continue
            elif line[0] == '[':
                # this is section name
                current_section = line[1:-1]
                print(current_section)
                continue
            else:
                # this gives some values
                if current_section == "dimension":
                    line = line.split(',')
                    self.width = int(line[0])
                    self.height = int(line[1])
                elif current_section == "lines":
                    line = line.split(',')
                    self.lines.append( (int(line[0]), int(line[1]), int(line[2]), int(line[3])) )
        print(self.width)
        print(self.height)
        print(self.lines)
        
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