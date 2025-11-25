import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset("iris")

# Univariate
sns.histplot(iris["sepal_length"], color="skyblue")
plt.title("Sepal Length Distribution")
plt.xlabel("Sepal Length"); plt.ylabel("Frequency")
plt.show()

# Multivariate
fig, axes = plt.subplots(2, 2, figsize=(10, 7))
for ax, col in zip(axes.flat, iris.columns[:-1]):
    sns.boxplot(x="species", y=col, data=iris, ax=ax)
    ax.set_title(f"{col.replace('_',' ').title()} by Species")
plt.tight_layout(); plt.show()
