from my_xlsx_utils import *

# ignoring warning
warnings.simplefilter(action='ignore', category=UserWarning)

NdF_data = load_workbook("xlsx_manipulation/data_WD/NdF_Data_Result.xlsx")

NdF_data_sheet = NdF_data.active

if NdF_data_sheet.max_column == 2:
    add_col(NdF_data_sheet, "Expense ID")
    add_col(NdF_data_sheet, "Montant")

add_col(NdF_data_sheet, "Employee")
NdF_sheet_dict = build_col_dict(NdF_data_sheet)

for row in NdF_data_sheet.iter_rows():
    text = row[NdF_sheet_dict["NdF reference"]].value
    if ": projet not found" in text:
        row[NdF_sheet_dict["Employee"]].value =text[:text.find(": projet not found")]
        continue
    if text == None:
        break
    if text != "NdF reference":
        row[NdF_sheet_dict["Expense ID"]].value = text.split(" ")[2].strip(",")
        row[NdF_sheet_dict["Montant"]].value = text.split(" ")[-2]
        row[NdF_sheet_dict["Employee"]].value = text[text.find(
            ", ") + 2: text.find("on ")]


NdF_data.save("xlsx_manipulation/NdF_Data_Result.xlsx")
