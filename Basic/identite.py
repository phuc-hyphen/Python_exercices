a = [1, 2, 3]
b = a


# print ("a : ", a)
# print ("b : " , b)
#
# print ("a == b : ", a==b)
# print ("a is b : ", a is b)

# créer un nouvel objet b qui contient le même tableau que a
# b = list(a)
# print ("b : " , b)
# print ("a == b : ", a==b)
# print ("a is b : ", a is b)

def pattern_matching(P):
    F = [None] * len(P)
    F[0] = 0
    i = 0
    j = 0
    while i < len(P):
        if P[i] == P[j]:
            F[i] = j + 1
            i += 1
            j += 1
        elif j > 0:
            j = F[j - 1]
        else:
            F[i] = 0
            i += 1
    print(F)


pattern_matching("ababc")
