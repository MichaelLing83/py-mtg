'''
'''

if __name__ == '__main__':
    from tkinter import Tk
    from tkinter import Canvas
    from tkinter import mainloop
    
    master = Tk()
    canvas = Canvas(master, width=200, height=200)
    canvas.pack()
    r = canvas.create_rectangle(0, 0, 20, 20, fill="blue")
    
    def ppp():
        canvas.move(r, 5, 5)
        canvas.after(1000, ppp)
    canvas.after(1000, ppp)
    
    master.mainloop()