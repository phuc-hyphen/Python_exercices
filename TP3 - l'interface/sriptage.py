from tkinter import *
#++++++++++++++++++++++++++++++++++++++++++++++++++
def script(text,deca):
    list = []
    for i in range(len(text)):
        temps = ord(text[i])  # transform en chiffre ASCII
        temps = temps + deca  # ajouter un décalage
        lettre = chr(temps)  # transform en lettre
        list.append(lettre)  # récupérer dans un list

    mot_scrip = ''.join(list)  # regrouper en un mot
    return mot_scrip

def descript(text,deca):
    list = []
    for i in range(len(text)):
        temps = ord(text[i])  # transform en chiffre ASCII
        temps = temps - deca  # ajouter un décalage
        lettre = chr(temps)  # transform en lettre
        list.append(lettre)  # récupérer dans un list

    mot_descrip = ''.join(list)  # regrouper en un mot
    return mot_descrip
# -----------------------------------


text=input("saisir un mot : ")
deca=int(input("saisir un décalage (en chiffre) : "))
print(script(text,deca))
mot=script(text,deca)
print(descript(mot,deca))

