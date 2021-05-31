import pandas as pd
import numpy as np

pd.set_option('display.max_colwidth', None)
pd.set_option("display.max_columns", None)

df = pd.read_csv("Data6.csv")
print(df.loc[df['Garden Area'].idxmax()])

print((df.nlargest(10,'Garden Area')['Garden Area']))
#
# print(df.loc[df['Url']== "https://www.immoweb.be/fr/annonce/autres-biens/a-vendre/anvers/2000/8214725"])
# print(df["Type of property"].describe())