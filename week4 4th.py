import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

iris = pd.read_csv("iris.csv")

features = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
titles = [
    "Comparison of Sepal Length by Species",
    "Comparison of Sepal Width by Species",
    "Comparison of Petal Length by Species",
    "Comparison of Petal Width by Species"
]

plt.figure(figsize=(18, 10))

for i, (feature, title) in enumerate(zip(features, titles), 1):
    plt.subplot(2, 2, i)
    sns.barplot(x="species", y=feature, data=iris, palette="Set3")
    plt.title(title)

plt.tight_layout()
plt.show()
