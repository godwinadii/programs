import seaborn as sns
import matplotlib.pyplot as plt

# Load and prepare data
iris = sns.load_dataset("iris")
plt.pie(iris.groupby("species")["sepal_length"].mean(), labels=iris["species"].unique(),
        autopct='%1.1f%%', colors=sns.color_palette("Set3"))
plt.title("Mean Sepal Length by Species"); plt.show()

# Multivariate (first 40 rows)
iris = iris.head(40)
iris.groupby("species").mean(numeric_only=True).plot(
    kind="bar", stacked=True, colormap="Set3", figsize=(12, 7))
plt.title("Multivariate Composition of Iris Species")
plt.xlabel("Species"); plt.ylabel("Mean Value")
plt.legend(title="Variables",loc="upper right"); plt.tight_layout(); plt.show()
