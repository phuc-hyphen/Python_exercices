print("3+4", 3 + 4)
print("3*4", 3 * 4)
print("3 puissance 4 = ", 3 ** 4)
print("14/3 = ", 14 / 3)
print("division entier 3//4", 3 // 4)
print("reste de la division 3%4 = ", 3 % 4)

a: int = 3
b = 4
print(" add 3 and 4 ", a + b)

str = "hello"
print(str + "world")
# print multi lines
print('''today the 17/01/22
i'm doing python 
it's boring''')

print("boring " * 3)

#print with in order
print("print", "with", "separator", sep='**')

#print without entering the line
print("print with new end of line", end='**')
print("%s %s %d" % ("valeur", "valeur2", 3))

import  time
# Ecrire sur la même ligne
for i in range (5):
    print ('\rTraitement en cours : ', i, end="")
    time.sleep(1)