import pandas as pd
import plotly.express as px


df = pd.read_excel("datas/tableanalfabet.xlsx")

dfRegions = pd.read_excel("datas/regionsTable_with_coordinates.xlsx")

fig = px.scatter_map(
    dfRegions,
    lat="Latitude",
    lon="Longitude",
    color="Taxa de analfabetismo - 15 anos ou mais de idade 2021",
    size="Taxa de analfabetismo - 15 anos ou mais de idade 2021",
    color_continuous_scale=px.colors.cyclical.IceFire,
    size_max=300,
    zoom=10,
)
fig.show()
