import datetime
import glob
import os.path
import time
from datetime import datetime

import os
import pymysql


# DOC :date de création
# DDM : date de modification
class fichier:
    def __init__(self, nom, repertoire, DDC, DDM, taille):
        self.nom = nom
        self.repertoire = repertoire
        self.DDC = datetime.strptime(DDC, '%a %b %d %H:%M:%S %Y')
        self.DDM = datetime.strptime(DDM, '%a %b %d %H:%M:%S %Y')
        self.taille = taille


def Lirefichier(chemin):
    nom = os.path.basename(chemin)
    ddc = time.ctime(os.path.getctime(chemin))
    ddm = time.ctime(os.path.getmtime(chemin))
    st = os.stat(chemin)
    return fichier(nom, chemin, ddc, ddm, st.st_size)


def insertSQL(fichier):
    query = "INSERT INTO files (nom,repertoire, date_de_creation,date_de_modification, taille_ko) " \
            "VALUES(%s, %s, %s, %s, %s)"
    args = (fichier.nom, fichier.repertoire, fichier.DDC, fichier.DDM, fichier.taille / 1024)
    cur.execute(query, args)
    conn.commit()


# iglob(pathname, recursive=False) Same as glob except that it returns an iterator,- so can be much more efficient.
chemin = 'C:\\Formation\\Python\\Exercices'
index = 0
# ---------------------------- init SQL ------------------------
conn = pymysql.connect(host='localhost', user='root', passwd=None, db='mysql')
cur = conn.cursor()
cur.execute("CREATE DATABASE IF NOT EXISTS locatedb")
cur.execute("use locatedb")
cur.execute("CREATE TABLE IF NOT EXISTS files (nom VARCHAR(64),repertoire VARCHAR(200), date_de_creation VARCHAR(64),"
            "date_de_modification VARCHAR(64), taille_ko INT)")

for filename in glob.iglob(chemin + '**\\*.py', recursive=True):
    print('\r (' + str(index) + ')' + filename, end="")
    file = Lirefichier(filename)
    insertSQL(file)
    index += 1

cur.close()
conn.close()
