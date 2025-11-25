import pandas as pd
df=pd.read_csv("Titanic.csv")
print("\nBefore Droping:\n")
df.info()
df=df.dropna()
print('\n\nAfter Droping:\n')
df.info()
