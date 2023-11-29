import pandas as pd
import sqlite3

data_url="https://download-data.deutschebahn.com/static/datasets/haltestellen/D_Bahnhof_2020_alle.CSV"
df= pd.read_csv(data_url,sep=';')

df.drop("Status",axis=1,inplace= True)

Verkehr_list=("FV", "RV", "nur DPN")
df = df[df['Verkehr'].isin(Verkehr_list)]

df.Laenge.replace(to_replace=",", value=".", inplace=True,regex=True)
df.Breite.replace(to_replace=",", value=".", inplace=True,regex=True)


df = df.astype({'Laenge':'float'})
df = df.astype({'Breite':'float'})

df = df[(df.Laenge <= 90.0) & (df.Laenge >= -90.0)]



pattern = "^[A-Za-z]{2}:\d*:\d*(?::\d*)?$"

df = df[df['IFOPT'].str.match(pattern, na=False)]

conn = sqlite3.connect('trainstops.sqlite')
cursor = conn.cursor()





df.to_sql('trainstops', conn, if_exists='replace', index=False)

conn.commit()
conn.close()
