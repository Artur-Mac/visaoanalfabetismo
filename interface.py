import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(layout="wide")

df = pd.read_excel("datas/tableanalfabet.xlsx")
dfRegions = pd.read_excel("datas/regionsTable_with_coordinates.xlsx")

st.markdown("# Taxa de Analfabetismo no Brasil")
st.divider()

col1, col2 = st.columns([1, 1], gap="large")
with col1:

    col3, col4 = st.columns([1, 1])
    with col3:

        idade = st.selectbox(
            "Idade",
            ["15 anos ou mais", "18 anos ou mais", "25 anos ou mais"],
        )

    with col4:
        ano = st.selectbox(
            "Ano",
            [
                "2012",
                "2013",
                "2014",
                "2015",
                "2016",
                "2017",
                "2018",
                "2019",
                "2020",
                "2021",
            ],
        )

    fig = px.scatter_mapbox(
        dfRegions,
        lat="Latitude",
        lon="Longitude",
        color="Taxa de analfabetismo - 15 anos ou mais de idade 2021",
        size="Taxa de analfabetismo - 15 anos ou mais de idade 2021",
        color_continuous_scale=px.colors.cyclical.IceFire,
        size_max=100,
        zoom=4,
        mapbox_style="carto-positron",
    )

    fig.update_layout(
        width=700,
        height=600,
        margin={"r": 0, "t": 0, "l": 0, "b": 0},
        coloraxis_colorbar=dict(title=""),
    )

    st.plotly_chart(fig)
