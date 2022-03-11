from tkinter import *

def hello():
    label=Label(fen,text="hello")
    label.grid(row=1,column=2)
def canvas():
    canvas=Canvas(fen,width=100,heigh=50)
    canvas.create_line(0,0,50,50)
    canvas.grid(row=2,column=2)
def entry():
    text=StringVar()
    entry=Entry(fen)
    entry.grid(row=3,column=3)



fen=Tk()
fen.title("pratique")

but=Button(fen,text="bouton",command=hello)
but.grid(row=1,column=1)
but_2=Button(fen,text="canvas",command=canvas)
but_2.grid(row=2,column=1)
but_3=Button(fen,text="entry",command=entry)
but_3.grid(row=3,column=1)


fen.mainloop()
