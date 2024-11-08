import pandas as pd

# Carregar o DataFrame do arquivo Excel
df = pd.read_excel("datas/regionsTable.xlsx")
df = df[:-1]
# Dicionário com as coordenadas de latitude e longitude para cada região
coordinates = {
    "Norte": {"Latitude": -3.4168, "Longitude": -65.8561},
    "Nordeste": {"Latitude": -7.1970, "Longitude": -39.3073},
    "Centro-Oeste": {"Latitude": -15.5989, "Longitude": -56.0969},
    "Sudeste": {"Latitude": -20.4697, "Longitude": -43.7544},
    "Sul": {"Latitude": -27.2423, "Longitude": -52.3336}
}

# Adicionar as colunas de latitude e longitude ao DataFrame
df['Latitude'] = df['Região'].map(lambda x: coordinates[x]['Latitude'])
df['Longitude'] = df['Região'].map(lambda x: coordinates[x]['Longitude'])

# Salvar o DataFrame atualizado em um novo arquivo Excel
df.to_excel("datas/regionsTable_with_coordinates.xlsx", index=False)

# Imprimir o DataFrame atualizado
print(df)