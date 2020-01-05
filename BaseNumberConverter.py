"""
    Converting any number of any base to another base with a tkinter gui
    @author: Josue Rojas
    @since: 05/01/2020
"""

from math import log, ceil
import tkinter as tk

inputText = ""
style= [["D", "E", "F", "BIN"],
        ["A", "B", "C", "OCT"],
        ["7", "8", "9", "DEC"],
        ["4", "5", "6", "HEX"],
        ["1", "2", "3",  "X"],
        ["0", "R", "C",  "Y"]]

def initWindow():
    global style, inputText
    w = tk.Tk()
    w.title("BaseNumberConverter")
    w.geometry('580x500')
    w.configure(background='black')

    color_boton = 'black'
    cn = 'white'
    actb="LightCyan3"
    ancho_boton = 20
    alto_boton = 20

    def digit(d):
        pass
    def clear():
        pass
    def enter():
        print("enter")
    def convert():
        global inputText
        def detectMode(inputText):
            allowed = "0123456789ABCDEF"
            for k in inputText:
                if k not in allowed:
                    inputText = "ERROR"

    tk.Entry(w,font=('Arial',15,"bold"),width=48,textvariable=inputText, bd=20, insertwidth=4,bg="lavender",justify="right").grid(sticky='N')  
    for i in range(4):
        tk.Button(w,font=('Arial',15,"bold"),width=4,textvariable=inputText, text=style[i][3],bd=20,bg="lavender",justify="right").grid(sticky='E')
    tk.Button(w,font=('Arial',15,"bold"),width=4, height=2,textvariable=inputText, text="=",bd=20,bg="lavender",command=convert, justify="right").grid(sticky='E')
    
    return w


w = initWindow()
w.mainloop()

# bin, hex, oct for dec to any number
# dec to bin, hex and oct
# n = 10
# n = '0xf101'
# print(bin(n))
# print(hex(n))
# print(oct(n))
# print(int(bin(n), 2))
# print(int(hex(n), 16))
# print(int(oct(n), 8))
#hexToOct return oct(int(hex, 16))
#octToHex return hex(int(oct, 8))


