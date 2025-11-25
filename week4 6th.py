import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
df = sns.load_dataset('iris')
# plt.figure(figsize=(24,20))
sns.pairplot(df, hue="species")
plt.suptitle('Multivariate plot',y=1.02)
plt.show()
