try:
    var = int(input("choisir un nombre"))
    if var % 2 == 0:
        print("c'est pair")
    else:
        print("c'est impair")
except:
    print("c'est pas un nombre")
