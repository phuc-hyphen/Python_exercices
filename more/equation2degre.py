from math import sqrt
print("equation 2 degre : Ax² + Bx + c")
A = int(input("A : "))
B = int(input("\nB : "))
C = int(input("\nC : "))


delta = B*B - 4*A*C
if delta > 0:
    print("l'equation 2 solutions : \n")
    print("x1 = ", (-B - sqrt(delta)/(2*A)))
    print("x2 = ", (-B + sqrt(delta)/(2*A)))
if delta ==0:
    print("l'equation a 1 solution double : x = ",-B/(2*A))
if delta < 0:
    print("l'équation ne possède pas de solution réelle.")