from tkinter import *

fen=Tk()
fen.title("cible")
fen.geometry("300x300")

cible=Canvas(fen,width=300,height=300)
cible.pack()

for i in range(0,150,20):
    coord=i,i,300-i,300-i
    print(coord)
    cible.create_oval(coord, fill='WHITE')

cible.create_line(0,150,300,150,width=2,fill='BLUE')
cible.create_line(150,0,150,300,width=2,fill='BLUE')

fen.mainloop()