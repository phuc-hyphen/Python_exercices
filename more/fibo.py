
fibo1 = 0
fibo2 = 1
for i in range (50):
    fibo = fibo2 + fibo1
    fibo1,fibo2 = fibo2,fibo
    print(fibo)