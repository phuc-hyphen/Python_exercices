print(""" jeu de Pierre-Papier-Ciseau
1 : Perre
2 : Ciseaux
3 : Papier
""")

pseudo1 = input("Nom du joueur 1 : ")
pseudo2 = input("Nom du joueur 2 : ")
play = 1
choix1 = 0
choix2 = 0
while play == 1:
    try:
        while 1 > choix1 or choix1 > 3:
            choix1 = int(input("choix du joueur 1 : "))
        while 1 > choix2 or choix2 > 3:
            choix2 = int(input("choix du joueur 2 :"))

        if (choix1 == 1 and choix2 == 2) or (choix1 == 2 and choix2 == 3) or (choix1 == 3 and choix2 == 1):
            print(pseudo1, "est le gagnant")
        elif choix1 == choix2:
            print("Pas de gagnant")
        else:
            print(pseudo1, "est le gagnant")

        play = int(input("continuez ? (0: non, 1: yes) "))
        choix1,choix2 = 0,0
        if play != 0 and play != 1:
            print("commande indéterminé !!, arreter le jeu !! ")

    except:
        print("il y a des erreurs")
