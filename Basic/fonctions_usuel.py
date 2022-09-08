
print (round (13/3))
print (abs(-15))

print (len("bonjour à tous"))
texte = "bonjour à tous."
print (texte.upper())
print (texte.capitalize())

texte = "1251456"
print(texte.isalnum())
texte = "abcde"
print(texte.isalpha())

print(texte.find("d"))

texte = "Bonjour à Tous"
print (texte.lower())


print(min(3,2,5))
print (min('c','a','b'))

print(max(3,2,5))
print (max('Paris','Londres','New York'))

print (sorted(('Paris','Londres','New York')))

print (sum ([4/3, 2/3, 1/3, 1/3, 1/3]))


a = True
print (type(a))

a = 12
print (type(a))

a = "Bonjour"
print (type(a))

a = ' Mug '
print (a.strip())
print (a.rstrip())
print (a.lstrip())

texte = "Bonjour à tous"
print (texte.replace("o", "0", 1))

print (texte.split(" "))
couleurs = ["bleu", "vert", "jaune", "blanc", "noir"]
print ('-'.join(couleurs))