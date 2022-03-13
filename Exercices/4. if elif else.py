age=18
if (age<18):
    print("Vous êtes mineur")
elif (age>18):
    print ("Vous êtes majeur")
else:
    print ("Je ne sais pas répondre !")

prix = 10000
duree = 12

if (prix<15000) and (duree<15):
    print("taux =" , "2%")
elif (prix>=15000) or (duree>=15):
    print("taux =" , "4%")
