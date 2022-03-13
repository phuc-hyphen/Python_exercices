from faker import Faker
from faker import Factory

fakerFR = Factory.create('fr_FR')

myFactory = Faker()
print ("Texte aléatoire " ,  myFactory.text())

print (myFactory.words())
print (myFactory.name())
print (myFactory.month())
print (myFactory.sentence())
print (myFactory.state())
print (myFactory.random_number())


# https://faker.readthedocs.io/en/latest/locales/fr_FR.html
# print ("Texte aléatoire FR" ,  fakerFR.text())
# print (fakerFR.words())
# print (fakerFR.name())
# print (fakerFR.month())
# print (fakerFR.sentence())
# print (fakerFR.street_name())
# print (fakerFR.street_address())
# print (fakerFR.region())
# print (fakerFR.department_number())
print (fakerFR.city())
# print (fakerFR.department())
# print (fakerFR.postcode())
print (fakerFR.address())
# print (fakerFR.random_number())
date_de_naissance = fakerFR.date_of_birth(tzinfo=None, minimum_age=20, maximum_age=100)
print (date_de_naissance)
print ("Metier " ,  fakerFR.job())



