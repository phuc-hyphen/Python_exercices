from libs import Utils
from lib2to3.pgen2 import pgen
from numpy import integer
import streamlit as st
# import plotly.express as px
import st_aggrid as aggrid

st.set_page_config(page_title="Sales", page_icon=":blush:", layout="wide")

df = Utils.get_date_from_excel(
    "Data\Rapport.xlsx", 'Tests', 'openpyxl')

# ------------------------------------- STREAM LIT ----------------------------------------------------------------
st.sidebar.progress(0)
# df
# 'this is text',
st.title(":smirk: TEST rapport")
st.markdown("##")
if st.checkbox("show raw data"):
    st.write(df)
hide_st_style = """
            <style>
            # MainMenu{visibility:hidden;}
            footer {visibility:hidden;}
            header {visibility:hidden;}
            </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

# ------------------------------------- arborences ----------------------------------------------------------------

gb = aggrid.GridOptionsBuilder.from_dataframe(df)
gb.configure_grid_options(rowHeight=50)
gb.configure_pagination()
groupe_prio = df["Priority"].value_counts()
me = groupe_prio["Medium"]

enGrave_jscode = aggrid.JsCode("""
  function(params) {
  	var element = document.createElement("span");
  	var linkElement = document.createElement("b");
    var node= params.node;
    var aggData = node.aggData;
  	var linkText = document.createTextNode(params.value + %d );
  	//link_url = params.value;
  	linkElement.appendChild(linkText);
  	//linkText.title = params.value;
  	// linkElement.href = link_url;
    // linkElement.target = "_blank";
  	element.appendChild(linkElement);
  	return element;
  };
  """ % (me))

test = aggrid.JsCode("""
                    function(params){
                        var mediumSum = 0;
                        params.values.forEach(value =>
                        {
                        if(value === 'Medium')
                            mediumSum += 1;
                        });
                        return mediumSum;
                    }
                     """)
# gb.configure_column("Group", cellRenderer=link_jscode)
gridOptions = gb.build()
gridOptions = {
    "columnDefs": [
        {"field": 'Key', "hide": True},
        {"field": 'Status'},
        {"field": 'Summary'},
        {"field": 'Test Type'},
        {"field": 'Priority', "type": 'PRIORITY'},
        {"field": 'ran', "type": 'number'},
    ],
    "defaultColDef": {
        'flex': 1,
        'resizable': True,
        'filter': True,
    },
    "autoGroupColumnDef": {
        'headerName': "KEY",
        'minWidth': 300,
        'cellRendererParams': {
            # 'suppressCount': True,
            # 'checkbox': True,
            'innerRenderer': enGrave_jscode,
        },

        # "statusBar": {
        #     'statusPanels': [
        #         {'statusPanel': 'agTotalRowCountComponent', "align": 'center'},
        #         {'statusPanel': 'agFilteredRowCountComponent'},
        #         {'statusPanel': 'agSelectedRowCountComponent'},
        #         {'statusPanel': 'agTotalAndFilteredRowCountComponent', "align": 'left'},
        #         {'statusPanel': 'agAggregationComponent'},
        #     ],
        # }
    },
    "columnTypes": {
        'dimension': {
            'enableRowGroup': True,
            'enablePivot': True,
        },
        'number': {
            # 'editable': True,
            #   editing works with strings, need to change string to number
            'valueParser': aggrid.JsCode("""
            function(params){
                return parseInt(params.newValue);}""").js_code,
            'aggFunc': 'sum',
        },
        'PRIORITY': {
            'aggFunc': test,
        }
    },
    # "groupDisplayType" : 'groupRows',
    # "groupRowRenderer":'agGroupCellRenderer',
    # "groupRowRendererParams": { # active this and the autoGroupColumnDef will be disabled
    #     'headerName': "KEY",
    #     'innerRenderer': enGrave_jscode,
    #     'minWidth': 300,

    # }

}

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
    # tree_data=True
)
