import streamlit as st
import pandas as pd


st.title("Data Science Report")
st.header("Week 3 of CAP 2757")
st.subheader("Prof. Greg Reis")
st.divider()

originalData, correlation, threeDplot, otherCharts, maps = st.tabs(
    ["Structured Data", "Correlation", "3D Charts", "Other Charts", "Maps"]
)

with originalData:
    df = pd.read_csv("datasets/biscayne_bay_water_quality2.csv")
    st.subheader("Original Dataset")
    st.dataframe(df)

    st.divider()
    st.subheader("Descriptive Statistics")
    st.dataframe(df.describe())

