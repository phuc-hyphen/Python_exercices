# a = 131
# b = 25
# print("a =", bin(a))
# c = a << 2;
# print("a nad b  = ", c, bin(c))


a = 131
b = 25

print('a= ', a, ' : ', bin(a), ' b =', b, ' : ', bin(b))
c = 0

c = a & b;  # 1 = 0000 0001
print("result of AND is ", c, ':', bin(c))

c = a | b;  # 155 = 1001 1011
print("result of OR is ", c, ':', bin(c))

c = a ^ b;  # 154 = 10011010
print("result of EXOR is ", c, ':', bin(c))

c = ~a;  # -132 = 1000 0100
print("result of COMPLEMENT is ", c, ':', bin(c))

c = a << 2;  # 240 = 0010 0000 1100
print("result of LEFT SHIFT is ", c, ':', bin(c))

c = a >> 2;  # 32 = 0010 0000
print("result of RIGHT SHIFT is ", c, ':', bin(c))
