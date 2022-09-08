class Rectangle:
    def __init__(self,largeur,longueur):
        self.largeur = largeur
        self.longueur = longueur
        self.description = ""
        self.auteur = "personne"

    def aire(self):
        return self.largeur* self.longueur

    def perimetere(self):
        return 2 * self.largeur + 2 * self.longueur

    def decrire(self,text):
        self.description = text

    def nomAuteur(self,text):
        self.auteur= text

    def redimensionner(self, proportion):
        self.largeur = self.largeur * proportion
        self.longueur = self.longueur * proportion


class Carre(Rectangle):
    def __init__(self,largeur):
        self.largeur = largeur
        self.longueur = largeur

petitRectangle = Rectangle(5, 10)
grandRectangle = Rectangle(30, 60)

print (petitRectangle.aire())
petitRectangle.redimensionner(6)
print (petitRectangle.aire())
print (grandRectangle.aire())

petitCarre = Carre(20)
print ("Aire petitCarre:", petitCarre.aire())

formesGeometriques = {}
formesGeometriques["Carre 1"] = Carre(5)
formesGeometriques["Rectangle 1"] = Rectangle(600,45)
print(formesGeometriques["Rectangle 1"].aire())
