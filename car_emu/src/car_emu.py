'''
'''

from Field import Field
from Car import Car
from tkinter import Tk
from tkinter import Canvas
from tkinter import mainloop
import os
from Constants import Direction

car_pos = (0, 0)

def move_car(direction, move):
    result = (direction, 0, 0) # stay stationary by default
    if direction == Direction.N:
        result = {  Direction.FORWARD: (direction, 0, -1),
                    Direction.RIGHT: (Direction.E, 0, 0),
                    Direction.REVERSE: (direction, 0, 1),
                    Direction.LEFT: (Direction.W, 0, 0)
                }[move]
    elif direction == Direction.E:
        result = {  Direction.FORWARD: (direction, 1, 0),
                    Direction.RIGHT: (Direction.S, 0, 0),
                    Direction.REVERSE: (direction, -1, 0),
                    Direction.LEFT: (Direction.N, 0, 0)
                }[move]
    elif direction == Direction.S:
        result = {  Direction.FORWARD: (direction, 0, 1),
                    Direction.RIGHT: (Direction.W, 0, 0),
                    Direction.REVERSE: (direction, 0, -1),
                    Direction.LEFT: (Direction.E, 0, 0)
                }[move]
    elif direction == Direction.W:
        result = {  Direction.FORWARD: (direction, -1, 0),
                    Direction.RIGHT: (Direction.N, 0, 0),
                    Direction.REVERSE: (direction, 1, 0),
                    Direction.LEFT: (Direction.S, 0, 0)
                }[move]
    return result

if __name__ == '__main__':
    
    print(os.getcwd())
    field = Field("./src/field_rectangle.txt")
    Field.car = Car()
    Field.car_direction = Direction.S
    
    master = Tk()
    canvas = Canvas(master, width=field.width, height=field.height)
    canvas.pack()
    for line in field.get_lines():
        canvas.create_line(*line)
    r = canvas.create_rectangle(1, 1, 21, 21, fill="blue")
    
    def ppp():
        Field.car_direction, x, y = move_car(Field.car_direction, Field.car.move())
        canvas.move(r, x, y)
        canvas.after(100, ppp)
    canvas.after(100, ppp)
    
    master.mainloop()