from faker import Faker
import csv
import random

f = open("datas.csv", "w", encoding='UTF8', newline='')
writer = csv.writer(f, delimiter=';')

fk = Faker("FR_fr")
Faker.seed(0)

headers = ["nom", "prenom", "matricule", "date_de_naissance", "rue", "code", "ville", "telephone", "email"]
writer.writerow(headers)

data = []
for i in range(0, 1000):
    data.append(fk.first_name())
    data.append(fk.last_name())
    # data.append(random.randint(1000,99999))
    data.append(fk.address())
    data.append(str(fk.date_of_birth(tzinfo=None, minimum_age=20, maximum_age=100)))
    data.append(fk.street_address())
    data.append(fk.postcode())
    data.append(fk.department_name())
    data.append(fk.phone_number())
    data.append(fk.company_email())
    writer.writerow(data)
    data.clear()
