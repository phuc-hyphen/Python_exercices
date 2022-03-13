a = [1, 2, 3]
b = a
print ("a : ", a)
print ("b : " , b)

print ("a == b : ", a==b)
print ("a is b : ", a is b)

# créer un nouvel objet b qui contient le même tableau que a
b = list(a)
print ("b : " , b)
print ("a == b : ", a==b)
print ("a is b : ", a is b)