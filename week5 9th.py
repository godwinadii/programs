#UNIVARIATE OUTLIER

from sklearn.datasets import load_diabetes
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

dp=load_diabetes()
df=pd.DataFrame(dp.data)
df.columns=dp.feature_names

#BOX PLOT
sns.boxplot(df["bmi"])
plt.xlabel("BMI")
plt.ylabel("VALUES")
plt.show()

#CALCULATING OUTLIERS
q1=df["bmi"].quantile(0.25)
q3=df["bmi"].quantile(0.75)
IQR=q3-q1

#SETTING OUTLIERS BOUNDARIES
lower_bound=q1-1.5*IQR
upper_bound=q3+1.5*IQR

#PRINT OF OUTLIERS
outliers= df [(df.bmi <=lower_bound) | (df.bmi>=upper_bound)]
print("Outliers: \n ",outliers)