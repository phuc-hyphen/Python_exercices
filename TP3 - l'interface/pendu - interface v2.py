from tkinter import *
import pendu as pen
#------------------------------------------------------------------------
def check():
    global lettre,cache,mot,label_mot,cache1,label_lettre,passage
    lettre1=lettre.get()
    if (passage==0):
        cache1=pen.compar(lettre1,mot,cache)
        passage=1
    else :
        cache1=pen.compar(lettre1,mot,cache1)
    label_mot.config(text=cache1)
    label_lettre.delete(0,END)
#----------------------------------
vie=5
passage=0
point=0
stockage="   "
liste=pen.choix_list(1)# le choix du niveau
print(liste)


fen= Tk()
fen.title("pendu -V 2")
fen.geometry("720x360")
# générer un mot à partir un liste choisi
mot=pen.gene(liste)
alphabet="abcdefghijklmnopqrstuvwxyz "

# créer un cache qui a la même longueur que le mot choisi
cache=len(mot)*"*"
label_mot=Label(fen, text= cache,font=("Time New Romain",60))
label_mot.pack(pady=20)

lettre=StringVar()
label_lettre=Entry(fen, textvariable=lettre,bg="White",width=20)
label_lettre.pack()

bouton=Button(fen, text="check ",command=check)
bouton.pack()


win=False






fen.mainloop()
# while(vie!=0):
#
#     print("\nLes lettres à votre disponible : ", alphabet)
#     lettre=input("\nQuelle lettre vous voulez deviner : ")
#
#     cache=pen.compar(lettre,mot,cache)
#
#     print("le mot à deviner est : ",cache)
#     alphabet=pen.verification(alphabet,lettre)
#
#     print("Les lettres utilisées : ",stockage)
#     print("Le nombre de vie reste : ",vie)
#
