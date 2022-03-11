#!/usr/bin/env python

#----------------------------------------------------------------------
# Sujet:     	Correction du TP tkinter Pendu
#
# Auteur:      	Frédéric Thiré
# Email:	   	Frederic.Thire@ac-versailles.fr
#
# Created:     	9/03/2021
# Copyright:   	GNU GPL
#----------------------------------------------------------------------


# ---------------------------------------------------------------------
#                  Import des librairies / modules
# ---------------------------------------------------------------------
import tkinter as tk
from tkinter import messagebox

import pendu as jeu


# ---------------------------------------------------------------------
#                  Les fonctions graphiques
# ---------------------------------------------------------------------

# ------------
# La fonction qui dessine le pendu en fonction du nombre d'erreurs
# Ici le niveau indique le nombre d'erreurs commises par le joueur
def DessinePendu(niveau):
	if niveau==1:
		Wsurface.create_line(75,280,225,280,width=2,fill=couleur)
	elif niveau==2:
		Wsurface.create_line(150,280,150,100,width=2,fill=couleur)
	elif niveau==3:
		Wsurface.create_line(150,100,250,100,width=2,fill=couleur)
		Wsurface.create_line(250,100,250,125,width=2,fill=couleur)
	elif niveau==4:
		Wsurface.create_oval(235,125,265,155,width=2,outline=couleur)
	elif niveau==5:
		Wsurface.create_line(250,155,250,200,width=2,fill=couleur)
	elif niveau==6:
		Wsurface.create_line(225,165,275,165,width=2,fill=couleur)
	elif niveau==7:
		Wsurface.create_line(250,200,240,225,width=2,fill=couleur)
		Wsurface.create_line(250,200,260,225,width=2,fill=couleur)


# ------------
# C'est la fonction principale qui gère le déroulement du jeu
# d'un point de vue graphique
def Analyse():
	
	lettredonnee=lettre.get()
	Wchoix.delete(0,tk.END)
	
	if not(jeu.TestDejaVu(lettredonnee)):
		if jeu.AnalyseReponse(lettredonnee):
			# On a trouvé une lettre du mot !
			Wmot.config(text=jeu.motcache)
			if jeu.TestFinJeu():
				messagebox.showinfo("Pendu", "Bravo, vous avez gagné !")
				fen1.quit()
		else:
			# Suite de la pendaison
			DessinePendu(jeu.DonneNbErreurs())
		
		if jeu.DonneNbErreurs() >= 7:
			messagebox.showinfo("Pendu", "Vous avez perdu !")
			fen1.quit()
	else:
		messagebox.showinfo("", "Lettre déjà donnée")



# ------------
# On récupère le fait d'utiliser la touche Entrée du clavier
def callback(event):
	print("Appui sur Entrée")
	Analyse()

# ---------------------------------------------------------------------
#                  Le main
# ---------------------------------------------------------------------

# Init tkinter
fen1 = tk.Tk()
fen1.title("Pendu")

# couleur du tracé du pendu
couleur="brown"

# Lancement du jeu coté logique
jeu.Init()
jeu.LanceJeu()


# Zone de dessin
Wsurface=tk.Canvas(fen1,height=300,width=300,bg="white")
Wsurface.grid(row=0,columnspan=2)


# Le mot a deviner
Wmot=tk.Label(fen1, text=jeu.motcache, fg="black",width=10, height=3)
Wmot.grid(row=1,columnspan=2)



# La question
Wtexte=tk.Label(fen1, text="Lettre ?", fg="black",width=10, height=3)
Wtexte.grid(row=2,column=0)

# La reponse
lettre=tk.StringVar() 
Wchoix=tk.Entry(textvariable=lettre, width=5)
Wchoix.grid(row=2,column=1)
Wchoix.bind("<Return>",callback)


# un bouton pour valider
Wvalide = tk.Button(fen1,text="Valider",fg="blue",command=Analyse)
Wvalide.grid(row=3,columnspan=2)

tk.Button(fen1,text="Quitter",command=fen1.quit).grid(row=4,columnspan=2)
fen1.mainloop()
