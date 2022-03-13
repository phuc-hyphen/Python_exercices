try:
    for i in range(0, 6):
        for j in range(i):
            print("*", end='')
        print(end='\n')
    print(end='\n')
    for i in range(5,0,-1):
        for j in range(i):
            print("*", end='')
        print(end='\n')

except:
    print("il y a des erreurs")
