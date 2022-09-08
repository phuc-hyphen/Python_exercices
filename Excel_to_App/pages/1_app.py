import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Sales", page_icon=":blush:", layout="wide")

# run : streamlit run c:\Formation\Python\Python_exercices\Excel_to_App\app.py


@st.cache  # allow streamlit to get excel only 1 time (shortern memory)
def get_date_from_excel(path, sheet, engine):
    df = pd.read_excel(
        io=path,
        engine=engine,
        sheet_name=sheet,
        skiprows=3,
        usecols='B:R',
        nrows=1000
    )
    df["hour"] = pd.to_datetime(df["Time"], format="%H:%M:%S").dt.hour
    return df


df = get_date_from_excel(
    "Data\supermarkt_sales.xlsx", 'Sales', 'openpyxl')
# st.dataframe(df)

# ------------------------ SIdebar ------------------------

st.sidebar.header("Filter Here: ")
city = st.sidebar.multiselect("select the city :",
                              options=df["City"].unique(),
                              default=df["City"].unique()
                              )

customer_type = st.sidebar.multiselect("select the customer type :",
                                       options=df["Customer_type"].unique(),
                                       default=df["Customer_type"].unique()
                                       )

gender = st.sidebar.multiselect("select the gender :",
                                options=df["Gender"].unique(),
                                default=df["Gender"].unique()
                                )
# querying data ( after @ variables names before are column name)
df_selection = df.query(
    "City == @city & Customer_type == @customer_type & Gender == @gender"
)

st.dataframe(df_selection)  # reset the dataframe

# --------------------- mainpage-------------------------------

st.title(":smirk: SALES DASHBOARD")
st.markdown("##")

# ------------- TOP KPA -------------------------

total_sale = int(df_selection["Total"].sum())
average_rating = round((df_selection["Rating"].mean()), 1)
star_rating = ":star:" * int(round(average_rating, 0))  # drawing star
average_sale_by_trasaction = round(
    (df_selection["Total"].mean()), 2)  # mean = cacul moyen

left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader("Total Sales:")
    st.subheader(f"US $ {total_sale:,}")

with middle_column:
    st.subheader("Average Rating:")
    st.subheader(f"{average_rating} {star_rating}")

with right_column:
    st.subheader("Average SAles per transaction")
    st.subheader(f"US $ {average_sale_by_trasaction}")

st.markdown("-------")

# ------------------ bar chart ----------------

sales_by_production_line = df_selection.groupby(by=["Product line"]).sum()[
    ["Total"]].sort_values(by="Total")

# draww chart
fig_product_sales = px.bar(sales_by_production_line, x="Total", y=sales_by_production_line.index, orientation="h",
                           title="<b>Sales by production line</b>",
                           color_discrete_sequence=[
                               "#0083B8"]*len(sales_by_production_line),
                           template="plotly_white"
                           )
fig_product_sales.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)
# st.plotly_chart(fig_product_sales)

# sales by hour
sales_by_hour = df_selection.groupby(by=["hour"]).sum()[["Total"]]

fig_hourly_sales = px.bar(
    sales_by_hour,
    y="Total",
    x=sales_by_hour.index,
    title="<b>Sales by hour</b>",
    color_discrete_sequence=["#0083B8"]*len(sales_by_hour),
    template="plotly_white"
)
fig_hourly_sales.update_layout(
    xaxis=dict(tickmode="linear"),
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False))
)
# st.plotly_chart(fig_hourly_sales)

left_column, right_column = st.columns(2)
left_column.plotly_chart(fig_product_sales)
right_column.plotly_chart(fig_hourly_sales)

# ---------hide streamlit style --------------------

hide_st_style = """
            <style>
            #MainMenu{visibility:hidden;}
            footer {visibility:hidden;}
            header {visibility:hidden;}
            </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)
