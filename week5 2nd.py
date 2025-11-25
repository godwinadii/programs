import pandas as pd
import numpy as np
df=pd.read_csv("Titanic.csv")
print(df.isna().sum())
#Replacing all NaN values with -1
df=df.replace({np.nan:-1})
print("\n\n\n")
print(df.isna().sum())
