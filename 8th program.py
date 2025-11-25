import pandas as pd
df = pd.DataFrame({"Name": ['Bangalore', 'Mumbai', 'Delhi'], "temp": [20,30,24]})
print(df)
df.melt()
df.pivot(columns='Name', values='temp')