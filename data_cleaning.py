import pandas as pd
import numpy as np


url = "https://raw.githubusercontent.com/JulienAlardot/challenge-collecting-data/main/Data/database.csv"
df = pd.read_csv("Data3.csv")

del df['Unnamed: 0.1']
del df['Unnamed: 0.1.1']
del df['Unnamed: 0.1.1.1']
del df['Unnamed: 0.1.1.1.1']
del df['Unnamed: 0']

#del df['Unnamed: 0']
#del df['Url']
#del df['Source']

#print(df.head())
#null = df.isnull().sum()
#print(df["Subtype of property"].value_counts())
#df = df.drop(df.index[np.where(df["Subtype of property"] == "building")[0]])
#df = df.drop(df.index[np.where(df["Price"] <= 30000)[0]])
#df = df.drop(df.loc[df['Area'].idxmax()])
#df = df.drop(df['Area'].idxmax())
#url =["https://www.logic-immo.be/fr/vente/maisons-a-vendre/havre-7021/maison-70-chambres-e992c303-35a9-e5d5-fd27-4ae8d0876117.html",
    # "https://www.immoweb.be/fr/annonce/maison/a-vendre/havre/7021/8703998",
    # "https://www.immoweb.be/fr/annonce/immeuble-a-appartements/a-vendre/havre/7021/8951414",
    # "https://www.immoweb.be/fr/annonce/maison/a-vendre/marche-en-famenne/6900/9209135",
    # "https://www.immoweb.be/fr/annonce/immeuble-mixte/a-vendre/schaerbeek/1030/9140569"]

#df2 = df[~df.Url.str.contains('autres-biens')]

#df = df.set_index()
#data_final = df.reset_index()
df.to_csv("Data3.csv")
