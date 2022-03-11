from tkinter import *
import random

def cercle(k):# créer un X en endroit souhaitée
    list_coord_cercle = []

    for i in range(0, 241, 120):  # courir de 0 à 240
        for j in range(120, 361, 120):  # courir de 120 à 360
            # les coordonnées
            x = i
            x1 = i + 120
            y = j
            y1 = j - 120
            # récupérer des données
            coord = [y1 + 5, x + 5, y - 5, x1 - 5]
            # les stoker dans un liste
            list_coord_cercle.append(coord)
    # dessiner le O
    inter.create_oval(list_coord_cercle[k], width=2)

def croix(k): # créer un X en endroit souhaitée
    list_coord_croix_1 = []
    list_coord_croix_2 = []

    for i in range(0,241,120):  # courir de 0 à 240
        for j in range(120,361,120): # courir de 120 à 360
            # les coordonnées
            x=i
            x1=i+120
            y=j
            y1=j-120
            # récupérer des données
            coord_1=[y1+5, x+5, y-5, x1-5]
            coord_2 = [y1+5 , x1-5 , y-5 , x+5]
            # les stoker dans un liste
            list_coord_croix_1.append(coord_1)
            list_coord_croix_2.append(coord_2)
    # dessiner le X
    inter.create_line(list_coord_croix_1[k], width=2)
    inter.create_line(list_coord_croix_2[k],width=2)

def jeu():
    inter.delete("all") # clear all
    inter.create_line(0, 120, 360, 120, width=2, fill='red')
    inter.create_line(0, 240, 360, 240, width=2, fill='red')
    inter.create_line(120, 0, 120, 360, width=2, fill='red')
    inter.create_line(240, 0, 240, 360, width=2, fill='red')
    inter.place(x=0,y=0)

def detec_clique(event):
    global tour, liste_case,case_joueur
    k=0
    # les coordonnées d'un clique
    x=event.x
    y=event.y
    # détecter la position
    for i in range(0,241,120):
        for j  in range(0,241,120):
            if( x > j and x < j + 120 and y > i and y < i + 120 ):
                # récupérer la position
                position = k

                tour += 1

            k += 1
     # vérifier si le case a été coché ou pas
    if position in liste_case:
        print(" ce case a été coché")
    else:
        # dessiner un croix
        croix(position)
        case_joueur.append(position) # prendre la position utilisé par le joueur
        liste_case.append(position)  # prendre la position utilisé

        if (len(liste_case)<8):
            machine()
        check_joueur()      # check_joueur()

def machine():# la partie de la machine

    global case_machine,win_joueur
    pos_machine = random.randint(0, 8)
    win_machine=False
    # vérifier si le case a été coché ou pas
    while pos_machine in liste_case:
        pos_machine = random.randint(0, 8)

    liste_case.append(pos_machine)              # prendre la position utilisé par la machine
    case_machine.append(pos_machine)            # prendre la position utilisé

    for i  in range(8):
        point_machine=0
        for j in range(len(case_machine)):
            if case_machine[j] in win_liste[i]:
                point_machine+=1
        if (point_machine == 3 and win_joueur==False):
            lose()
            win_machine=True
    if (len(liste_case)==9 and win_machine==False): egal()

    cercle(pos_machine) # dessiner un cercle

def check_joueur(): # faire voir si le joueur ou la machine a gagné
    global win_liste,win_joueur

    for i  in range(8):
        point_joueur=0
        for j in range(len(case_joueur)):
            if case_joueur[j] in win_liste[i]:
                point_joueur+=1
        if (point_joueur == 3):
            win()
            win_joueur=True
    if (len(liste_case)==9 and win_joueur==False): egal()


def win():
    win=Toplevel()
    win.title("Win")
    win.geometry("360x100")
    la_win=Label(win,text=" YOU WIN ",font=("Time New Roman",40),pady=10,padx=10)
    la_win.pack()

def lose():
    lose=Toplevel()
    lose.title("Lose")
    lose.geometry("360x100")
    la_lose=Label(lose,text=" YOU LOSE ",font=("Time New Roman",40),pady=10,padx=10)
    la_lose.pack()

def egal():
    egale=Toplevel()
    egale.title("Win")
    egale.geometry("480x100")
    legale=Label(egale,text=" END IN A DRAW ",font=("Time New Roman",40),pady=10,padx=10)
    legale.pack()

#-----------------------------------------------------------------#

tour=0
win_liste = [[0,1,2],[0,3,6],[0,4,8],[1,4,7],[2,5,8],[3,4,5],[6,7,8],[2,4,6]] # la liste des cases gagnant
case_joueur=[]
case_machine=[]
liste_case=[]
win_joueur=False



fen=Tk()
fen.title("Tic_Toc_Toe")
fen.geometry("360x360")


inter = Canvas(fen, width=360, height=360, bg='white')  # créer les carrés
inter.bind("<Button-1>", detec_clique)  # fonction pour détecter un clique
inter.place(x=0, y=0)

jeu()

fen.mainloop()