import xlwt

book = xlwt.Workbook()

page1 = book.add_sheet("employee")

page1.write(1,1,"premier info")

book.save('C:\\Formation\\tmp.xlsx')