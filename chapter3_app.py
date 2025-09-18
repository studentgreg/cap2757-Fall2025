import streamlit as st # web app/dashboard development
import pandas as pd # manipulating tabular data
import plotly.express as px # data visualization
from streamlit import plotly_chart

st.title("Data Science Report")
st.header("Exploratory Data Analysis")
st.subheader("Prof. Greg Reis")
st.divider()

originalData, correlation, threeDplot, otherCharts, maps = st.tabs(
    ["Structured Data", "Correlation", "3D Charts", "Other Charts", "Maps"]
)

df = pd.read_csv("datasets/biscayne_bay_water_quality2.csv")

with originalData:
    st.subheader("Original Dataset")
    st.dataframe(df)

    st.divider()
    st.subheader("Descriptive Statistics")
    st.dataframe(df.describe())

with correlation:
    st.subheader("Correlation")
    fig1 = px.scatter(df,
                      x="Total Water Column (m)",
                      y="Temperature (c)",
                      color="ODO mg/L")
    st.plotly_chart(fig1)

with threeDplot:
    st.subheader("3D Charts")
    fig2 = px.scatter_3d(df,
                         x="Longitude",
                         y="Latitude",
                         z="Total Water Column (m)",
                         color="Temperature (c)")
    fig2.update_scenes(zaxis_autorange="reversed")
    st.plotly_chart(fig2)

with otherCharts:
    st.subheader("Line Chart")
    col1, col2 = st.columns(2,border=True)
    with col1:
        color = st.color_picker("Choose a color", "#081E3F")
        parameter = st.selectbox("Choose a water parameter",options=[
            "Total Water Column (m)", "Vehicle Speed (kn)",
            "Salinity (ppt)", "Temperature (c)", "pH", "ODO mg/L"
        ])
    with col2:
        fig3 = px.line(df,
                       x=df.index,
                       y=parameter)
        fig3.update_traces(line_color=color)
        st.plotly_chart(fig3)

with maps:
    st.subheader("Maps")
