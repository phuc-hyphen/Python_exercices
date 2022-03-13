try:
    nb1 = int(input("choisir un nombre"))
    nb2 = int(input("choisir un nombre"))

    if nb1 % nb2 == 0:
        print(nb1,"est divisble de",nb2)
    else:
        print(nb1,"est pas divisble de",nb2)
except:
    print("il y a des erreurs")
