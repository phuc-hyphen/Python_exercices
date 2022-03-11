import random


def gene():
    global liste_carte,symbol,chiffre
    for i  in range(len(symbol)):
        for j in range(len(chiffre)):
            carte=[symbol[i],chiffre[j]]
            liste_carte.append(carte)
    print(liste_carte)


def mix():
    for i in range(50):
        carte_1 = random.randint(0, 31)
        carte_2 = random.randint(0, 31)
        carte_temp=liste_carte[carte_1]
        liste_carte[carte_1]=liste_carte[carte_2]
        liste_carte[carte_2]=carte_temp

    print(liste_carte)

def pick():

    for i in range(5):
        print(liste_carte[i])
    for i in range(5):
        liste_carte.pop(i)
    print(liste_carte)

def gene_liste_nombre():
    global liste_nombre
    for i in range (50):
        nombre=random.randint(0,200)
        liste_nombre.append(nombre)
    print(liste_nombre)

def cherche_max():
    max=0
    position=0
    for i in range(50):
        if(liste_nombre[i]>max):
            max=liste_nombre[i]
            position=i
    print(max,position)




#---------------Exo - 1 ----------------------

symbol=['\u2660','\u2661','\u2662','\u2663']
chiffre=['As','7','8','9','10','Valet','Dame','Roi']
liste_carte=[]
#----------------EXO - 2 --------------------------

liste_nombre=[]
gene_liste_nombre()
cherche_max()