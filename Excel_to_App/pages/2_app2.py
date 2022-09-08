
from numpy import integer
import pandas as pd
import streamlit as st
# import plotly.express as px
import json
import st_aggrid as aggrid

st.set_page_config(page_title="Sales", page_icon=":blush:", layout="wide")


@st.cache  # allow streamlit to get excel only 1 time (shortern memory)
def get_date_from_excel(path, sheet, engine):
    df = pd.read_excel(
        io=path,
        engine=engine,
        sheet_name=sheet,
        # skiprows=3,
        # usecols='A:R',
        nrows=1000
    )
    # df["hour"] = pd.to_datetime(df["Time"], format="%H:%M:%S").dt.hour
    return df


df = get_date_from_excel(
    "Data\Rapport.xlsx", 'Tests', 'openpyxl')

st.sidebar.progress(0)
# df
# 'this is text',
st.title(":smirk: TEST rapport")
st.markdown("##")
if st.checkbox("show raw data"):
    st.write(df)
hide_st_style = """
            <style>
            #MainMenu{visibility:hidden;}
            footer {visibility:hidden;}
            header {visibility:hidden;}
            </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

gb = aggrid.GridOptionsBuilder.from_dataframe(df)
gridOptions = gb.build()

gridOptions["columnDefs"] = [
    {"field": 'Key', "hide": True},
    {"field": 'Status'},
    {"field": 'Summary'},
    {"field": 'Test Type'},
    {"field": 'Priority'},
    {"field": 'ran', "type": 'number'
     #  "cellRenderer":
     #      aggrid.JsCode("""
     #         function(params){
     #             return `<span>${params.value}</span>`;
     #   }""").js_code,
     #  "cellRendererParams": {
     #      "innerRendererParams": {"foo": 'bar'},
     #  }

     },
    
    
]
gridOptions["defaultColDef"] = {
    "flex": 1,
    "resizable": True,
},
gridOptions["autoGroupColumnDef"] = {
    "headerName": "KEY",
    "minWidth": 1000,
    "cellRendererParams": {
        "suppressCount": True,
        "checkbox": True,
        "innerRenderer": aggrid.JsCode(""" p => '<b>' + p.value + '</b>'""").js_code,
    },
    "filter": True,
},
# gridOptions["statusBar"] = {
#     "statusPanels": [
#         {"statusPanel": 'agTotalAndFilteredRowCountComponent', "align": 'left'},
#         {"statusPanel": 'agTotalRowCountComponent', "align": 'center'},
#         {"statusPanel": 'agFilteredRowCountComponent'},
#         {"statusPanel": 'agSelectedRowCountComponent'},
#         {"statusPanel": 'agAggregationComponent'},
#     ],
# },
# gridOptions["groupDisplayType"] = 'groupRows'
# gridOptions["groupRowRenderer"] = 'agGroupCellRenderer'
# gridOptions["groupRowRendererParams"] = {
#     # "innerRenderer": aggrid.JsCode("""
#     #     function(params){
#     #         var eGui = document.createElement('div');
#     #         eGui.style.display = 'inline-block';
#     #         var node = params.node;
#     #         var aggData = node.aggData;
#     #         var html = '';
#     #         html += '<span class="random">RAN_NUMB</span>';
#     #         html = html.replace(/RAN_NUMB/g, "2021")
#     #         eGui.innerHTML = html;
#     #   }""").js_code,
#     "rowDrag": True,
#     "suppressCount": True,
# }
# gridOptions["columnTypes"] = {
#     "number": {
#         "editable": True,
#         #   editing works with strings, need to change string to number
#         "valueParser": aggrid.JsCode("""
#             function(params){
#                 return parseInt(params.newValue);
#       }""").js_code,
#         "aggFunc": 'sum',
#     },
# },


gridOptions["animateRows"] = True
gridOptions["treeData"] = True
gridOptions["groupDefaultExpanded"] = -1

gridOptions["getDataPath"] = aggrid.JsCode(""" 
    function(data){
        return data["key"].split("/");
  }""").js_code

r = aggrid.AgGrid(
    df,
    gridOptions=gridOptions,
    height=1200,
    allow_unsafe_jscode=True,
    enable_enterprise_modules=True,
    filter=True,
    update_mode=aggrid.GridUpdateMode.SELECTION_CHANGED,
    # ['streamlit', 'light', 'dark', 'blue', 'fresh', 'material']
    theme="material",
    # theme={
    #     "font-size": "17px",
    #     },
    tree_data=True
)
