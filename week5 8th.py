import pandas as pd
df=pd.read_csv("Titanic.csv")
print("Before Replacing:\n\n",df['Age'].head(7))
print("\nMode of Age Column:",df['Age'].mode()[0])
dp=df['Age'].fillna(df['Age'].mode()[0])
print("\nAfter Replacing with Mode:\n\n",dp.head(7))
