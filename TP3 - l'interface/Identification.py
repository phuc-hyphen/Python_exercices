from tkinter import *

def compar():
    global Mdp,iden
    # récupérer des liste à partir des fichiers
    f = open("identifier", "r")
    list_iden = f.read().splitlines()
    f2=open("mot_de_passe","r")
    list_mdp = f2.read().splitlines()
    # récupérer des variables dans le case
    iden=iden.get()
    mdp=Mdp.get()
    deca=3
    bon=False
    mau=False
    for i in range(0,len(list_iden)):
        if(iden==list_iden[i]): # identification en 1 position précise
            word=list_mdp[i]
            if(mdp==descript(word,deca)):# mdp déscripté en meme position
                bon=True
    if(bon==False):
        reponse = Label(fen,text="Identification ou mot de passe est incorrect !", width=35, height=1, fg='BLACK')
        reponse.place(x=0, y=80)
    else:
        reponse = Label(fen,text="Identification ou mot de passe est correct !", width=35, height=1, fg='BLACK')
        reponse.place(x=0, y=80)

def clear():
    global case_mdp, case_iden
    case_mdp.delete(0,END) # effacer les bars // case_mdp.insert(0,"")
    case_iden.delete(0,END)

def script(text,deca):
    list = []
    for i in range(len(text)):
        temps = ord(text[i])  # transform en chiffre ASCII
        temps = temps + deca  # ajouter un décalage
        lettre = chr(temps)  # transform en lettre
        list.append(lettre)  # récupérer dans un list

    mot_scrip = ''.join(list)  # regrouper en un mot
    return mot_scrip

def descript(text,deca):
    list = []
    for i in range(len(text)):
        temps = ord(text[i])  # transform en chiffre ASCII
        temps = temps - deca  # ajouter un décalage
        lettre = chr(temps)  # transform en lettre
        list.append(lettre)  # récupérer dans un list

    mot_descrip = ''.join(list)  # regrouper en un mot
    return mot_descrip

#-------------------------------------------------------------------------------------------#
fen=Tk()
fen.title("l'accueil")
fen.geometry("300x150")

ligne=Canvas(fen,width=300,height=300)
ligne.create_line(0,75,300,75,width=4,fill='BLUE')
ligne.pack()

identifi=Label(fen,text = "Identification :",width=20,height=1,fg='BLACK')
identifi.place(x=5,y=30)

iden=StringVar()
case_iden=Entry(fen,textvariable=iden,width=20,bg='WHITE',fg='BLACK')
case_iden.place(x=140,y=30)


mdp=Label(fen,text = "Mot de passe :",width=20,height=1,fg='BLACK')
mdp.place(x=5,y=50)

Mdp=StringVar()
case_mdp=Entry(textvariable=Mdp,width=20,bg='WHITE',fg='BLACK')
case_mdp.config(show="*") # mettre des lettres sous la forme *
case_mdp.place(x=140,y=50)

bouton=Button(fen,text="Check",width=20,fg='BLACK',command= compar)
bouton.place(x=10,y=100)

bouton=Button(fen,text="Reset",width=20,fg='BLACK',command= clear)
bouton.place(x=150,y=100)

fen.mainloop()

