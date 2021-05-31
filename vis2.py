import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
df = pd.read_csv("Data5.csv")
sns.heatmap(df)
# dfhouse = pd.read_csv("DataHouse.csv")
# dfapart = pd.read_csv("Dataapart.csv")

# print(dfhouse.info())
# print(dfapart.info())
# plt.plot(dfhouse["Area"],dfhouse["Price"], 'g+')
# plt.xlabel('Area')
# plt.ylabel('Price')
#
plt.show()