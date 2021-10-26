import pandas as pd
import numpy as np

df = pd.read_csv("test.csv")

types = df.columns.to_series().groupby(df.dtypes).groups
typ = df.dtypes

numerics = []
# numerics = numerics.append()
numerics = [i for i in df.columns if df.dtypes[i] == np.datetime64]
print(numerics)