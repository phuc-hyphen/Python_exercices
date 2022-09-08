from my_xlsx_utils import *
# ignoring warning
warnings.simplefilter(action='ignore', category=UserWarning)

NdF_data = load_workbook("xlsx_manipulation/NdF_Data.xlsx")

NdF_data_sheet = NdF_data["NdF"]

NdF_Project=  load_workbook("xlsx_manipulation/NDF Projets.xlsx")

NdF_re_qualified = NdF_Project["Lignes à requalifier"]

NdF_sheet_dict = build_col_dict(NdF_data_sheet)

NdF_re_dict = build_col_dict(NdF_re_qualified)

for row_qualify in NdF_re_qualified.iter_rows(values_only=True):
    for row_data in NdF_data_sheet.iter_rows():
        if row_qualify[NdF_re_dict["OBJET"]] == row_data[NdF_sheet_dict["OBJET"]].value:
            row_data[NdF_sheet_dict["ElementFrais"]].value = row_qualify[NdF_re_dict["Expense item"]] 
            
NdF_data.save("xlsx_manipulation/NdF_Data.xlsx")