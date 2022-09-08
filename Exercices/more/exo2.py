
try:
    var = int(input("saisir un variable"))
    if var > 0:
        print("it is positive")
    elif var < 0:
        print("it is negative")
    else:
        print("it's null")
except:
    print("it isn't an integer")


