"""
    Converting any number of any base to another base with a tkinter gui
    @author: Josue Rojas
    @since: 05/01/2020
"""

from math import log, ceil
import tkinter as tk

style = ["DEF","ABC", "789", "456", "123", "0RC"]

def initWindow():
    global style
    w = tk.Tk()
    w.title("Ventana")
    w.geometry('500x500')
    w.configure(background='black')

    #components
    for r in range(6):
        for c in range(3):
            b = tk.Button(w, text=style[r][c], bg='red', fg='yellow', font='arial')
            b.grid(row = r, column = c, pady=5, padx=5)
    return w

initWindow().mainloop()

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


