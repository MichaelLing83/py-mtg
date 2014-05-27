'''
'''

from Field import Field

if __name__ == '__main__':
    from tkinter import Tk
    from tkinter import Canvas
    from tkinter import mainloop
    
    import os
    print(os.getcwd())
    field = Field("./src/field_rectangle.txt")
    
    master = Tk()
    canvas = Canvas(master, width=field.width, height=field.height)
    canvas.pack()
    for line in field.get_lines():
        canvas.create_line(*line)
    r = canvas.create_rectangle(1, 1, 21, 21, fill="blue")
    
    def ppp():
        canvas.move(r, 5, 5)
        canvas.after(1000, ppp)
    canvas.after(1000, ppp)
    
    master.mainloop()