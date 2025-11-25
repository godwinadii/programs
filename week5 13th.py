#For Credit dataset 
# Spot outliers in income using bivariate plot 
# Spot outliers in any feature using boxplot 
# Detect outliers in any one feature using IQR method 
# Treat outliers using Imputation [Mean, Median, Zero] 

import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv("credit risk.csv")
df_orignal=df.copy()
df_mean1=df.copy()
df_median=df.copy()
df_mode=df.copy()

# Spot outliers in income using bivariate plot
plt.scatter(df["person_age"].head(25),df["person_income"].head(25),color="gold")
plt.xlabel("Person Age")
plt.ylabel("Person Income")
plt.title("Spot outliers in income using bivariate plot")
plt.grid(True)
plt.show()

# Spot outliers in any feature using boxplot
plt.boxplot(df["person_income"].head(70))
plt.ylabel("Person Income")
plt.title("Spot outliers in any feature using boxplot")
plt.show()

# Detect outliers in any one feature using IQR method 
q1=df["person_income"].quantile(0.25)
q3=df["person_income"].quantile(0.75)
IQR=q3-q1

#Outlier bounds
lower=q1-1.5*IQR
upper=q3+1.5*IQR

outlier=(df.person_income <=lower) | (df.person_income >=upper)
print("Outliers: \n ",outlier.sum())

#Imputing using mean
inc=df_mean1["person_income"]

out=(inc<=lower)|(inc>=upper)
mean_val =inc[(inc >= lower) & (inc <= upper)].mean()
df_mean1.loc[out, 'person_income'] = int(mean_val)

plt.boxplot(df_mean1['person_income'].head(70))
plt.title("After Mean Imputation")
plt.ylabel("Person Income")
plt.show()

#Imputing using median
inc=df_median["person_income"]

out=(inc<=lower)|(inc>=upper)
median =inc[(inc >= lower) & (inc <= upper)].median()
df_median.loc[out, 'person_income'] = median
plt.boxplot(df_median['person_income'].head(70))
plt.title("After Median Imputation")
plt.ylabel("Person Income")
plt.show()

#Imputing using mode
inc=df_mode["person_income"]

out=(inc<=lower)|(inc>=upper)
mode =inc[(inc >= lower) & (inc <= upper)].mode()[0]
df_mode.loc[out, 'person_income'] = mode

plt.boxplot(df_mode['person_income'].head(70))
plt.title("After Mode Imputation")
plt.ylabel("Person Income")
plt.show()