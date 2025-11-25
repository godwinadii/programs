#MULTIVARIATE OUTLIERS
from sklearn.datasets import load_diabetes
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

dp=load_diabetes()
df=pd.DataFrame(dp.data)
df.columns=dp.feature_names

#MULTIVARIATE PLOT
plt.figure(figsize=(18,10))
sns.boxplot(data=df)
plt.ylabel("Values")
plt.title("Multivariate plots")
plt.show()