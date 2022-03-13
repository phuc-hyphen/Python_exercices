try:
    text = input("give me a text")
    compte = 0
    for letter in text:
        if letter in "aeiouy":
            compte +=1
    print("nombre de voyelle dans", text, "est", compte)
except:
    print("il y a des erreurs")
