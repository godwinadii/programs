import pandas as pd
df=pd.read_csv("Titanic.csv")
print("Before Filling Null values:\n\n",df.isna().sum())
df=df.fillna(0)
print("\n\nAfter Filling Null Values:\n\n",df.isna().sum())
