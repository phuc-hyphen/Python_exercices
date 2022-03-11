#!/usr/bin/env python


#----------------------------------------------------------------------
# Sujet:     	module pour le jeu du pendu (Version 2)
#
# Auteur:      	Frédéric Thiré
# Email:	   	Frederic.Thire@ac-versailles.fr
#
# Created:     	13/02/2018
# Copyright:   	GNU GPL
#----------------------------------------------------------------------

#----------------------------------------------------------------------
#                           MODULES
#----------------------------------------------------------------------

import random
import os

# ---------------------------------------------------------------------
#			FONCTIONS
# ---------------------------------------------------------------------


# -------------------------------------------------------------------
# on intialise quelques variables qui sont servir dans le jeu
# -------------------------------------------------------------------
def Init():
	global ListeMots
	global score
	global lettres_proposes
	
	ListeMots=["truc","toto"]
	score=7
	lettres_proposes=[]



# -------------------------------------------------------------------
# Cette fonction permet de connaître le nombre d'erreurs
# commises par le joueur
# -------------------------------------------------------------------
def DonneNbErreurs():
	return 7-score



# -------------------------------------------------------------------
# fonction qui s'occupe de trouver un mot à faire deviner
# L'exemple simple ci-dessous consiste à choisir un mot au hasard
# dans une liste de mots prédéfinie.
# -------------------------------------------------------------------
def DonneMotaDeviner():
	return ListeMots[random.randint(0,len(ListeMots)-1)]



# -------------------------------------------------------------------
# fonction interne qui cache le mot a deviner
# -------------------------------------------------------------------
def CacheMot(mot):
	return "*"*len(mot)


# -------------------------------------------------------------------
# Cette fonction s'occupe de faire apparaître la lettre devinée dans
# le mot qui s'affiche avec des etoiles.
# -------------------------------------------------------------------
def RemplacerEtoile(mot,mot_cache,lettre):
	NouveaumotCache=""
	for i in range(len(mot_cache)):
		if mot[i]==lettre:
			NouveaumotCache=NouveaumotCache+lettre
		else:
			NouveaumotCache=NouveaumotCache+mot_cache[i]
	return NouveaumotCache



# -------------------------------------------------------------------
# Ici on analyse la réponse du joueur
# -------------------------------------------------------------------
def AnalyseReponse(lettre):
	global score
	global motcache
	global lettres_proposes
	
	lettres_proposes.append(lettre)
	trouve=lettre in motadeviner
	
	if trouve:
		#print("Bravo tu as trouvé une lettre")
		motcache=RemplacerEtoile(motadeviner,motcache,lettre)
		
	else:
		#print("Raté")
		score -=1
	return trouve



# -------------------------------------------------------------------
# la lettre donnée a-t-elle déjà été vu ?
# -------------------------------------------------------------------
def TestDejaVu(lettre):
	return lettre in lettres_proposes



# -------------------------------------------------------------------
# a-t-on découvert le mot mystère ?
# -------------------------------------------------------------------
def TestFinJeu():
	return motcache==motadeviner



# -------------------------------------------------------------------
# Début de la partie
# -------------------------------------------------------------------
def LanceJeu():
	global motcache
	global motadeviner
	
	lettres_proposes=[]
	motadeviner=DonneMotaDeviner()
	print("Le mot à deviner est ",motadeviner)
	motcache=CacheMot(motadeviner)
	#print(motcache)
Init()
LanceJeu()

