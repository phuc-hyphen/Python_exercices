
import pymysql
conn = pymysql.connect(host='localhost', user='root', passwd=None, db='mysql')
cur = conn.cursor()



cur.execute("create database if not exists locatedb")

cur.execute("use locatedb")
cur.execute("CREATE TABLE IF NOT EXISTS files (nom VARCHAR(64),repertoire VARCHAR(200), date_de_creation VARCHAR(64),date_de_modification VARCHAR(64), taille_ko INT)")

query = "INSERT INTO files (nom,repertoire, date_de_creation,date_de_modification, taille_ko) " \
        "VALUES(%s, %s, %s, %s, %s)"
args = ("fichier.nom", "fichier.repertoire", "fichier.DDC", "fichier.DDM", 24)

cur.execute(query,args)
conn.commit()
# cur.execute("INsert into hello (eye) values (1);")
# cur.execute("drop table hello")


cur.close()
conn.close()