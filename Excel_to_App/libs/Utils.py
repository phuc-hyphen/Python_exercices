import pandas as pd
import streamlit as st


@st.cache  # allow streamlit to get excel only 1 time (shortern memory)
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
