try:
    year = int(input("choisir un an"))
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 100 == 0:
                print(year, "est bissextile")
            else:
                print(year, "est pas bissextile")
        else:
            print(year, "est bissextile")
    else:
        print(year, "est pas bissextile")
except:
    print("il y a des erreurs")
