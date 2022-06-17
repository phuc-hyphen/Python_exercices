class Credit:
    def __init__(self,montant,duree):
        self.montant = montant
        self.duree_year = duree
    def taux(self):
        if self.duree_year <= 7:
            return 0.92
        elif self.duree_year <= 10:
            return 1.1
        elif self.duree_year <= 15:
            return 1.38
        elif self.duree_year <= 20:
            return 1.6
        else:
            return -1
    def mensualite(self):
        __mensualite = 0        # __ to diffirenciate name of variable and name of the function
        duree_month = self.duree_year*12
        if self.montant == 0:
            return 0
        __taux = self.taux()
        if (__taux == -1):
            return 0
        if __taux == 0:
            return self.montant / (self.duree_year*12)
        __taux = __taux/1200
        # return round(self.montant*__taux*(1-1/(1-(1+__taux)**duree_month)), 2)

        return round((self.montant * __taux * (1 + __taux)**duree_month) / ((1 + __taux)**duree_month - 1),2)
    def coute_total(self):
        return round(self.mensualite() * self.duree_year*12 - self.montant,2);

credit = Credit(100000,20)
print("mensualité",credit.mensualite())
print("coute total",credit.coute_total())