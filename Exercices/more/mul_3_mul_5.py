Multiple_de_Trois=[]
Multiple_de_Cinq=[]
Multiple_de_Trois_et_de_Cinq=[]
for i in range(1,50):
    if i %3 == 0:
        Multiple_de_Trois.append(i)
    if i %5 == 0 :
        Multiple_de_Cinq.append(i)
    if i %5 == 0 and i% 3 ==0:
        Multiple_de_Trois_et_de_Cinq.append(i)
print(Multiple_de_Trois)
print(Multiple_de_Cinq)
print(Multiple_de_Trois_et_de_Cinq)
