
from openpyxl import Workbook

# # save  the workbook in the dataframe

# workbook = Workbook()
# sheet = workbook.active

# sheet["A1"] = "hello"
# sheet["B1"] = "world!"

# workbook.save(filename="hello_world.xlsx")


#  read_excel
import warnings
from openpyxl import load_workbook
# ignoring warning
warnings.simplefilter(action='ignore', category=UserWarning)

workbook = load_workbook(filename="xlsx_manipulation/NDF_Projets_V2.xlsx")
# to see all the sheets you have available to work with.
# print(workbook.sheetnames) 

# # selects sheets
first_sheet = workbook.active # the first available sheet

sheet_data2 = workbook["sheet_names"] # with the sheet names

# # To return the actual value of a cell
# sheet["A1"].value
# sheet.cell(row=10, column=6).value
print(sheet_data["A1"].value)


