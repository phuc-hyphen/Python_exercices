#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Exercices sur les chaines de caractères (TP 2)
#
# Fait par              : Prof X
# Le                    : 25/02/2020
# Derniere modification : 


# ---------------------------------------------------------------------
#                              fonctions
# ---------------------------------------------------------------------

# ----
# Cette fonction indique si le mot donné contient le caractere 'e'
def TestContientE(mot,lettre='e'):
    trouve=False
    
    # On part du principe qu'il n'y a pas de 'e' !!!!
    # Ensuite, on parcours toute la chaine jusqu'à trouver un 'e'
    index=0
    while (not(trouve) and index <len(mot)):
        #print("Je regarde le caractere ",mot[index])
        if mot[index]==lettre:
            trouve=True
        index+=1
    
    return trouve


# ----
# Dexième version plus simple
def TestContientEv2(mot):
    return 'e' in mot


# ----
# Cette fonction compte combien il y a de 'b' dans la chaine donnée
def CombiendeB(mot):
    Nb=0
    for c in mot:
        if c=='b':
            Nb+=1
    return Nb


# ----
# On souhaite intercalé des étoiles
def Intercale_Etoiles(mot):
    mot_etoile=""
    
    for c in mot[:-1]:
        mot_etoile=mot_etoile+c+"*"
    
    mot_etoile=mot_etoile+mot[-1]
    
    return mot_etoile


# ----
# On souhaite retourner un mot ... l'ecrire à l'envers !!
def Inverse(mot):
    mot_retourner=""
    
    for index in range(len(mot)):
        mot_retourner=mot_retourner+mot[len(mot)-index-1]
    
    return mot_retourner
    

# ----
# Deuxième version ....
def Inversev2(mot):
    mot_retourner=""
    
    for c in mot:
        mot_retourner=c+mot_retourner
    
    return mot_retourner


# ----
# On souhaite une fonction qui indique si le mot donné en argument
# est un palindrome.
def Test_Palindrome(mot):
    return mot==Inversev2(mot)


# ----
def ex1():
    mot=input("Donnez moi un mot : ")
    if TestContientE(mot):
        print("Oui")
    else:
        print("Non")
    
    print("Il y a ",CombiendeB(mot)," b dans ",mot)

# ----
def ex2():
    mot=input("Donnez moi un mot : ")
    #mot="TAXER"

    print(Intercale_Etoiles(mot))


# ----
def ex3():
    mot=input("Donnez moi un mot : ")
    #mot="TAXER"

    print(Inversev(mot))
    print(Inversev2(mot))


# ----
def ex4():
    mot=input("Donnez moi un mot : ")
    if Test_Palindrome(mot):
        print(mot," est un palindrome")
    else:
        print(mot," n'est pas un palindrome")



# ----
def exercices():
    ex1()
    ex2()
    ex3()
    ex4()
# ---------------------------------------------------------------------
#                                main
# ---------------------------------------------------------------------


ex4()
