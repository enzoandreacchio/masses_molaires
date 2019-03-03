from tkinter import *

a = -56

fen = Tk()
fen.title("Output du prgm : ")
can = Canvas(fen, width = 500, height = 500)
can.pack()
can.create_text(50, 50, text = a)
can.create_line(44,60,64,60, width = 2)
