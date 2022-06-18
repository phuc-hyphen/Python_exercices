from datetime import datetime

from faker import Faker
import xlwt

fk = Faker()
Faker.seed(0)
data = xlwt.Workbook()
page1 = data.add_sheet("employee")

IndexProfile = {
    "First name": 0,
    "Last name": 1,
    "Email": 2,
    "Date embauche": 3,
    "Poste": 4,
    "Degre expertise": 5,
    "Position": 6,
    "Salaire": 7,
    "Genre": 8,
    "Date de naissance": 9,
    "Statut marital": 10,
    "Date statut marital": 11,
    "Calendar de travail": 12,
    "Raison contrat": 13,
    "ID Contrat": 14,
    "Type contrat": 15,
    "Date signature employe": 12,
    "Date signature employeur": 13,
    "Duree essai": 14,
}


# page1.write(0, 0, "First name")
# page1.write(0, 1, "Last name")
# page1.write(0, 2, "Email")
# page1.write(0, 3, "DOB")
# page1.write(0, 4, "Address")
# page1.write(0, 5, "Hire Date")

size = input("Enter the size of databases : \n")
size_int = int(size)

for i in range(1, size_int):
    page1.write(i, 0, fk.first_name())
    page1.write(i, 1, fk.last_name())
    page1.write(i, 2, fk.company_email())
    page1.write(i, 3, str(fk.date_of_birth(tzinfo=None, minimum_age=19, maximum_age=65)))
    page1.write(i, 4, fk.address())
    page1.write(i, 5, str(fk.date_between_dates(date_start=datetime(2019, 1, 1), date_end=datetime(2021, 12, 31))))
data.save("C:\\Formation\\Fake_databases.xls")
