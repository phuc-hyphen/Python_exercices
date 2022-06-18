somme=0
for i in range(0, 20):
    print (i, ' ', end="")
    somme = somme + i
print ("\n", somme)
print ("\n", 19*20/2)

couleurs = ["bleu", "vert", "jaune", "blanc", "noir"]
for couleur in couleurs:
    print (couleur)

tableau = [[0,1,2], ["a","b","c"], ["A", "B", "C"]]
for i in range(0,3):
    for j in range(0,3):
        print (tableau[i][j])

# saisir votre age
age = input ("Taper votre age :")
# convertir en entier
age = int(age)
while (age<0):
    age = input("Taper votre age :")
    age = int(age)
    if (age<0):
        print ("Votre age ne peut pas être négatif")
        break  # continue
import time
i = 0
while (i<10):
    print("\rindex courant :", i, end="")
    i += 1 # i = i+1
    time.sleep(1)
