
def cherche_e(mot):
	exis=False
	for i in range(len(mot)) : 
		if(mot[i]=='e'):
			exis=True
	if exis :
		print("	Oui, votre mot contient la lettre e")
	else:
		print("	Non, votre mot ne contient pas la lettre e")

def lettre_b(mot):
	compte=0
	for i in range(len(mot)):
		if (mot[i]=='b'):
			compte+=1
	return compte

def intercale(mot):
	mot_inter=""
	for i in range (len(mot)):
		if(i+1==len(mot)):
			mot_inter += mot[i]
		else:
			mot_inter += mot[i] + "_"

	return mot_inter

def inverse(mot):
	mot_inver=""
	for i in range (1,len(mot)):

		mot_inver += mot[-i]

	mot_inver += mot[0]

	return mot_inver

def palindrome(mot):
	if (mot==inverse(mot)):
		print(" Ce mot est un palindrome ")
	else:
		print(" ce mot n'est pas palindrome ")
#-----------------------------------------------------------------#

mot= input("votre mot : ")
cherche_e(mot)
print(" Le nombre de la lettre b : ",lettre_b(mot))
print(" Le mot intercale par * est : ",intercale(mot))
print(" Le mot inversé est : ", inverse(mot))
palindrome(mot)

