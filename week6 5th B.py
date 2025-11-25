import pandas as pd
import matplotlib.pyplot as m
import seaborn as s
da=pd.read_csv("dhoni.csv")
m.figure(figsize=(18,10))
s.histplot(da['Runs'], bins=15, kde=True)
m.title('Distribution of Runs Scored')
m.show()
m.figure(figsize=(18,10))
s.barplot(data=da,x='Year',y='Runs',palette='viridis')
m.title('Batting Scores Over the Years')
m.xlabel('Year');m.ylabel('Runs')
m.xticks(rotation=45);m.show()
m.figure(figsize=(18,10))
s.heatmap(data=da.corr(),annot=True,cmap='crest')
m.title("Heatmap on DHONI's stats")
m.show()