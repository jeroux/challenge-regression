import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("Data5.csv")

print(df.info())
# plt.plot(df["Area"],df["Price"], 'g+')
# plt.xlabel('Area')
# plt.ylabel('Price')
#
# plt.show()