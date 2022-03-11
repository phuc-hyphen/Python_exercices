from tkinter import *

def cercle():
    global inter
    efface()
    for i in range(0,241,120):  # couris de 0 à 240
        for j in range(120,361,120): # couris de 120 à 360
            x=i
            x1=i+120
            y=j
            y1=j-120
            inter.create_oval(y1+5, x+5, y-5, x1-5, fill='white', width=1)
    return

def croix():
    efface()
    for i in range(0,241,120):  # couris de 0 à 240
        for j in range(120,361,120): # couris de 120 à 360
            x=i
            x1=i+120
            y=j
            y1=j-120
            inter.create_line(y1+5, x+5, y-5, x1-5, width=2)
            inter.create_line(y1+5 , x1-5 , y-5 , x+5 , width=2)


def efface():

    inter.delete("all") # clear all
    inter.create_line(0, 120, 360, 120, width=2, fill='red')
    inter.create_line(0, 240, 360, 240, width=2, fill='red')
    inter.create_line(120, 0, 120, 360, width=2, fill='red')
    inter.create_line(240, 0, 240, 360, width=2, fill='red')
    inter.place(x=0,y=0)

#-------------------------------------------------------------------------------------


fen=Tk()
fen.title("Croix and Cercle")
fen.geometry("360x450")

inter = Canvas(fen, width=360, height=360, bg='white')
efface()
inter.pack()

b_croix=Button(fen,text='Croix',font=('Time New Roman',10),command=croix)
b_croix.place(x=30,y=370)
b_cercle=Button(fen,text='Cercle',command=cercle)
b_cercle.place(x=170,y=370)
b_efface=Button(fen,text='Effacer',command=efface)
b_efface.place(x=300,y=370)
b_quitte=Button(fen,text='Quitter',command=fen.destroy)
b_quitte.place(x=170,y=400)



fen.mainloop()