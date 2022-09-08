import pandas as pd
import xlsxwriter
import streamlit as st
import plotly.express as px

# st.set_page_config(page_title= "my pandas", page_icon=":bamboo:")

# read Xls
# df_xls = pd.read_excel('Data/Fake_databases.xls')
# df_xls["new name"] = None
# df_xls.insert(2,"new name",None,True)
# df_xls.assign(test = None)
# df_xls = df_xls.append({'First name':'header', 'Last name':'hidden', 'Address':'nowhere', 'Hire Date':'2021-01-03'}, ignore_index = True)
# df_xls.loc[107] = ['header','hidden','nowhere','2021-01-03']
# df_xls.to_excel("Data/Fake_databases.xlsx",sheet_name='F_data')

def get_date_from_excel(path, sheet, engine):
    df = pd.read_excel(
        io=path,
        # engine=engine,
        sheet_name=sheet,
        # skiprows=3,
        # usecols='A:R',
        nrows=1000
    )
    # df["hour"] = pd.to_datetime(df["Time"], format="%H:%M:%S").dt.hour
    return df
# df = get_date_from_excel(
#     "Data\Rapport.xlsx", 'Tests', 'openpyxl')

# groupe_prio = df["Priority"].value_counts()
# print("medium" + str(groupe_prio["Medium"]))

# me = groupe_prio["Medium"]
me = 15
jscode = '''function(params) {
  	var element = document.createElement("span");
  	var linkElement = document.createElement("b");
  	var linkText = document.createTextNode(params.value + %d );
  	link_url = params.value;
  	linkElement.appendChild(linkText);
  	element.appendChild(linkElement);
  	return element;
  };''' % (me)
  
  
test = """{line %d
      line %d
      line %d}""" % (
      1,
      2,
      3)
print(jscode)