from my_xlsx_utils import *

# ignoring warning
warnings.simplefilter(action='ignore', category=UserWarning)

NdF_data = load_workbook("NdF_Data_Result.xlsx")

NdF_data_sheet = NdF_data.active

# add_col(NdF_data_sheet, "Doublons")

NdF_sheet_dict = build_col_dict(NdF_data_sheet)

dict_emp={}
list_emp=[]

for row in NdF_data_sheet.iter_rows():
    if row[NdF_sheet_dict["Employee"]].value not in list_emp:
        text = row[NdF_sheet_dict["Employee"]].value.lower().replace(" ", "")
        dict_emp[text] = row[NdF_sheet_dict["Montant"]].value
        list_emp.append(text)
    # else:
    #     row[NdF_sheet_dict["Doublons"]].value = "OUI"
 
# NdF_data.save("NdF_Data_Result_check.xlsx")

print(dict_emp)
      
NdF_data = load_workbook("NdF_Data_B.xlsx")

NdF_data_sheet = NdF_data.active

add_col(NdF_data_sheet,"montant actual")
add_col(NdF_data_sheet,"status")
NdF_sheet_dict = build_col_dict(NdF_data_sheet)

for row_data in NdF_data_sheet.iter_rows():

    emp = str(row_data[NdF_sheet_dict["employee"]].value)
    emp = emp.lower().replace(" ","")
    if emp not in list_emp:
        row_data[NdF_sheet_dict["status"]].value = "not found"
    else:
        row_data[NdF_sheet_dict["montant actual"]].value = dict_emp[emp]

NdF_data.save("NdF_Data_B_check.xlsx")
    




