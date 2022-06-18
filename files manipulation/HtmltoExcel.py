import codecs
import xlwt
from bs4 import BeautifulSoup


def strip_until(s, first):
    try:
        start = s.index(first)
        return s[0:start]
    except ValueError:
        return s

def find_between_r(s, first, last):
    try:
        start = s.rindex(first) + len(first)
        end = s.rindex(last, start)
        return s[start:end]
    except ValueError:
        return ""

file = codecs.open("Katalon-LoginLogout.html", "r", "utf-8")
# # Parse the html file
soup = BeautifulSoup(file, 'html.parser')
table = soup.find("table")

# The first tr contains the field names.
# ------------ get title ------------------------------
title = soup.tr.text
# --------------------get datas -------------------------------
datas = []
for row in table.find_all("tr"):
    for cols in row.find_all("td"):
        subs = find_between_r(str(cols), "<td>", "</td>")
        data = strip_until(subs, "<datalist>")
        datas.append(data)
        print(data)
# write in excel

book = xlwt.Workbook()
page1 = book.add_sheet("rapport katalon")
page1.write(0,1,"Command")
page1.write(0,2,"Comment")
page1.write(0,3,"Value")
page1.write(0,0,"Rapport : " + title)
row = 1
col = 1
for i in range(1,len(datas)):
    # print("data ",i,":",datas[i])
    page1.write(row, col, datas[i])
    col+=1
    if col > 3:
        col=1
        row+=1

book.save("C:\\Formation\\faker_databases.xls")
