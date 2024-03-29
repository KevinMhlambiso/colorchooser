from tkinter import *
from tkinter import colorchooser

def click():
    color = colorchooser.askcolor()
    print(color)
    colorHex = color[1]
    print(colorHex)
    windows.config(bg=colorHex)

windows = Tk()

windows.geometry("450x450")
button = Button(windows,command=click,text='click me')
button.pack()

windows.mainloop()