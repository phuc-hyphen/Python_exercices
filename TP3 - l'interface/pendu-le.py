import random


# générer un mot à partir de la liste
def gene(liste):
    id=random.randint(0,len(liste)-1)
    mot=liste[id]
    return mot


# comparer la lettre et celles du mot
def compar(lettre,mot,cache):
    global vie,point
    mal=False
    bon=False
    for i in range(len(mot)):
        if(lettre==mot[i]):
            pos=i
            cache=cache[:pos]+lettre+cache[pos+1:]
            bon=True
        else:
            mal=True
    if(mal==True and bon==False):
        print("la lettre est incorrecte")
         # si non un vie perdue
    return cache


# vérifirer que la lettre utilisé est utilisé
def verification(alphabet,lettre):
    global stockage,vie
    exite=False
    no_exite=False
    for i in range(len(alphabet)-1):
        if(lettre==alphabet[i]):
            pos=i
            alphabet=alphabet[:pos]+alphabet[pos+1:]
            stockage = stockage[:pos] + lettre + stockage[pos+1:]
            no_exite=True
        else:
            exite=True
    if(exite==True and no_exite==False):
        print(" la lettre a été utilisée ")
        vie=vie+1
    return alphabet

# des choix de niveau
def choix_list(choix):
    if (choix==1):
        liste = ["legume", "viande", "fruit", "eau"]
    if (choix==2):
        liste = ["accommodant", "informatique", "technologie", "transistor"]
    if (choix==3):
        liste = ["intergouvernementalisations", "anticonstitutionnellement", "contraventionnalisation",
                 "hyperpresidentialisation"]
    return liste

#------------------------------------------------------------------------------------------------------------------------------

