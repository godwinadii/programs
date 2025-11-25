import pandas as pd
df=pd.read_csv("Titanic.csv")
print("Before Replacing:\n\n",df['Age'].head(7))
print("\nMean of Age Column:",df['Age'].mean())
dp=df['Age'].fillna(df['Age'].mean())
print("\nAfter Replacing with Mean:\n\n",dp.head(7))
