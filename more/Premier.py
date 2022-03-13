def is_premier(num):
    counter = 0
    for i in range(1, num):
        if num % i == 0:
            counter += 1
    if counter > 2:
        print("c'est pas un nombre premier")
    else:
        print("c'est un nombre premier")


try:
    num = int(input("chosse a number"))
    is_premier(num)
except:
    print("Error")
