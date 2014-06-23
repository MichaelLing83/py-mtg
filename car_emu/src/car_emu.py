#!/usr/bin/env python3
'''
Main module for emulating car movement in a field.
'''

from Field import Field
from tkinter import Tk
from tkinter import Canvas
import os
from Constants import Direction

def move_car(direction, move):
    '''
    Calculate how the car should be moved on the field, based on its direction and
    move command.
    '''
    result = (direction, 0, 0) # stay stationary by default
    if direction == Direction.N:
        result = {
                    Direction.FORWARD: (direction, 0, -1),
                    Direction.RIGHT: (Direction.E, 0, 0),
                    Direction.REVERSE: (direction, 0, 1),
                    Direction.LEFT: (Direction.W, 0, 0)
                }[move]
    elif direction == Direction.E:
        result = {
                    Direction.FORWARD: (direction, 1, 0),
                    Direction.RIGHT: (Direction.S, 0, 0),
                    Direction.REVERSE: (direction, -1, 0),
                    Direction.LEFT: (Direction.N, 0, 0)
                }[move]
    elif direction == Direction.S:
        result = {
                    Direction.FORWARD: (direction, 0, 1),
                    Direction.RIGHT: (Direction.W, 0, 0),
                    Direction.REVERSE: (direction, 0, -1),
                    Direction.LEFT: (Direction.E, 0, 0)
                }[move]
    elif direction == Direction.W:
        result = {
                    Direction.FORWARD: (direction, -1, 0),
                    Direction.RIGHT: (Direction.N, 0, 0),
                    Direction.REVERSE: (direction, 1, 0),
                    Direction.LEFT: (Direction.S, 0, 0)
                }[move]
    return result

if __name__ == '__main__':

    print(os.getcwd())

    field = Field("./src/field_rectangle.txt") # pylint: disable=C0103

    master = Tk() # pylint: disable=C0103
    canvas = Canvas(master, width=field.width, height=field.height) # pylint: disable=C0103
    canvas.pack()
    for line in field.get_lines():
        canvas.create_line(*line)
    CAR_RECTANGLE = canvas.create_rectangle(1, 1, 21, 21, fill="blue")

    def tick():
        '''
        Called periodically to let car perform its movement.
        '''
        field.car_direction, __x__, __y__ = move_car(field.car_direction, field.car.move())
        field.car_pos_x += __x__
        field.car_pos_y += __y__
        canvas.move(CAR_RECTANGLE, __x__, __y__)
        canvas.after(100, tick)
    canvas.after(100, tick)

    master.mainloop()
