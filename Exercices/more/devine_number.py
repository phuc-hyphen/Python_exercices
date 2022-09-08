from random import randint


def play(number):
    tri = 0
    dev = int(input("devinez un nombre en tre 1 et 10 :"))

    while dev != number and tri < 3:
        print("Try n° :", tri + 1)
        if dev < number:
            print("trop bas")
        elif dev > number:
            print("trop haut")
        else:
            print("c'est gagnant , tout à fait juste")
        dev = int(input("devinez un nombre en tre 1 et 10 :"))

        tri += 1
    print("c'est perdu, 3 essaies dépassées !! ")


try:
    joue = True
    while joue:
        number = randint(1, 10)
        play(number)
        stop = input("continuez ? (Quitter pour quitter) ")
        if stop == "Quitter":
            joue = False

except:
    print("il y a des erreurs")
#
