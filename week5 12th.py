#Titanic Dataset Perform: 
#o Visualize missing values as bar plot and matrix plot 
#o Handle Missing values by deleting data objects and attributes 
#o Impute the missing values 

import missingno as ms
import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv("train.csv")

#BAR PLOT
ms.bar(df)
plt.title("Missing values as bar plot")
plt.show()

#Matrix plot
ms.matrix(df)
plt.title("Missing values as matrix plot")
plt.show()

#Missing values deleting data objects
print("\n Before deletion of Missing values data objects \n")
df.info()
missing_obj=df.dropna(axis=0)
print(missing_obj)
print("\n After deletion of Missing values data objects \n")
missing_obj.info()

#Missing values deleting data attributes
print("\n Before deletion of Missing values data attributes \n")
df.info()
missing_att=df.dropna(axis=1)
print(missing_att)
print("\n After deletion of Missing values data attributes \n")
missing_att.info()
#Imputing missing values
print("\n Before imputing values: \n")
df["Age"].info()
df["Age"]=df["Age"].fillna(df["Age"].mode()[0])
print("\n After imputing values: \n")
df["Age"].info()