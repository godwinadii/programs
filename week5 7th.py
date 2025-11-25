import pandas as pd
df=pd.read_csv("Titanic.csv")
print("Before Replacing:\n\n",df['Age'].head(7))
print("\nMedian of Age Column:",df['Age'].median())
dp=df['Age'].fillna(df['Age'].median())
print("\nAfter Replacing with Mean:\n\n",dp.head(7))
