# LE huu Phuc - SIRO


import random
from tkinter import *


# générer un mot à partir de la liste
def gene(liste):
    id=random.randint(0,len(liste)-1)
    mot=liste[id]
    return mot
# comparer la lettre et celles du mot
def compar(lettre, mot,cache):
    global vie,point
    mal=False
    bon=False
    for i in range(len(mot)):
        if(lettre==mot[i]):
            pos=i
            cache=cache[:pos]+lettre+cache[pos+1:]
            point=point+1
            bon=True
        else:
            mal=True
    if(mal==True and bon==False):
        label= Label(fen, text='La lettre est incorrect ', font=("Time New Romain", 15))
        label.place(x=400, y=200)
        vie=vie-1
        label_vie.config(text=vie)
        label_vie.place(x=930, y=50)
    return cache

# afficher les boutons et des fonctions
def affichage_bouton():
    global boutons
    alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    table_bouton=Canvas(fen,width=360, height=240,bg='white')
    table_bouton.place(x=360,y=240)

    k=0
    for i in range(4):
        for j in range(7):
            if (k<26):
                bou = Button(table_bouton, text=alphabet[k],font=('Time New Roman',15),command=lambda k=k: open(k))
                bou.grid(row=i,column=j,padx=10,pady=10,sticky=W)
                boutons.append(bou)
            k=k+1

# les fonctions du boutons
def open(num):
    global lettre,mot,cache
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u","v", "w", "x", "y", "z"]
    lettre=alphabet[num]
    boutons[num].config(state = 'disabled')
    if (vie>0):
        cache=compar(lettre, mot, cache)
        label_mot.config(text=cache)
        label_mot.pack(pady=20)
        image(vie)

def youwin():
    win=Toplevel()
    win.title("Win")
    win.geometry("360x100")
    la_win=Label(win,text=" YOU WIN ",font=("Time New Roman",40),pady=10,padx=10)
    la_win.pack()

def youlose():
    lose=Toplevel()
    lose.title("Win")
    lose.geometry("360x100")
    la_lose=Label(lose,text=" YOU LOSE ",font=("Time New Roman",40),pady=10,padx=10)
    la_lose.pack()

# liste des images
def image(vie):
    # les coordonnées pour dessiner le pendu
    coord= [(0,0,0,0), # case vide
            (20, 20, 120, 20),
            (120, 20,120, 50),
            (100,50,150,100),# tete
            (125, 100, 125, 150),# corps
            (125, 150, 160, 190),# pied
            (125, 150, 90, 190),#pied
            (125, 100, 160, 140),#bras
            (125, 100, 90, 140),#bras
            (110, 60, 115, 75),
            (110, 75, 115, 60),
            (130, 60, 135, 75),
            (130, 75, 135, 60)]
    if(point==len(mot)):
        youwin()
    if(vie==0):
        pendu.create_line(coord[9], width=2, fill='black')
        pendu.create_line(coord[10], width=2, fill='black')
        pendu.create_line(coord[11], width=2, fill='black')
        pendu.create_line(coord[12], width=2, fill='black')
        youlose()
    if(vie==7):
        pendu.create_oval(coord[10-vie], width=2, fill='red')
    else:
        pendu.create_line(coord[10-vie], width=2, fill='black')


# la fenetre de choix du liste
def choix_list():
    global liste
    fen_liste=Tk()
    fen_liste.title("choix de niveau")
    fen_liste.geometry("280x180")
    fond=Canvas(fen_liste,width=280,height=180,bg='#85a4c9')
    fond.place(x=0,y=0)
    Label(fen_liste,text='Choisir votre niveau : ',font=('Time New Roman',15),bg='#85a4c9').pack()
    # en appuyant sur un choix du niveau, un liste vais être récupérer et la fênêtre sera fermée
    bouton_n1=Button(fen_liste,text="Facile",font=("Time New Roman", 10),command= lambda :[niveau_1(),fen_liste.destroy()])
    bouton_n1.pack(pady=10)
    bouton_n2=Button(fen_liste,text="Moyen",font=("Time New Roman", 10),command=lambda :[niveau_2(),fen_liste.destroy()])
    bouton_n2.pack(pady=10)
    bouton_n3=Button(fen_liste,text="Difficile",font=("Time New Roman", 10),command=lambda :[niveau_3(),fen_liste.destroy()])
    bouton_n3.pack(pady=10)

    fen_liste.mainloop()

def niveau_1():
    global liste
    liste = ["legume","viande","fruit","eau"]
def niveau_2():
    global liste
    liste = ["accommodant","informatique","technologie","transistor"]
def niveau_3():
    global liste
    liste = ["intergouvernementalisations","anticonstitutionnellement","contraventionnalisation","hyperpresidentialisation"]
#------------------------------------------------------------------------------------------------------------------------------
# les variables du jeu
vie=10
point=0
stockage=[]
boutons=[]
win=False
liste=[]
# choix du liste
choix_list()

fen=Tk()
fen.title("Pendu")
fen.geometry("1000x480")
Canvas(fen, width=1000, height=480, bg='#85a4c9').place(x=0, y=0)

# affichage du mot
label_lettre=Label(fen,text="\n La lettre à deviner :  ",font=(20),bg='#85a4c9')
label_lettre.pack(pady=20)

# choisir un mot à partir du liste
mot=gene(liste)
cache=len(mot)* "*"                 #cacher le mot
label_mot=Label(fen, text = cache,font=("Time New Romain",60),bg='#85a4c9')
label_mot.pack(pady=20)

#affichage la taille du mot
text='La largeur du mot : ' + str(len(mot)) + '   lettres'
Label(fen, text=text, font=('Time New Roman', 15), bg='#85a4c9').place(x=720,y=25)

# affichage le nombre de vie
Label(fen, text='Nombre de devinette : ', font=('Time New Roman', 15), bg='#85a4c9').place(x=720,y=50)
label_vie=Label(fen, text=vie, font=('Time New Roman', 15), bg='#85a4c9')
label_vie.place(x=930,y=50)


pendu = Canvas(fen, width=360, height=240, bg='white')
pendu.place(x=0, y=240)
pendu.create_line(20, 20, 20, 225, width=2, fill='black')


affichage_bouton()


fen.mainloop()


