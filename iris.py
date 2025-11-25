import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("IRIS.csv")

species_count = df['species'].value_counts()
langs = species_count.index.tolist()
students = species_count.values.tolist()

plt.figure(figsize=(6, 4))
plt.bar(langs, students, color='green')
plt.title("Bar: Count of Each Iris Species")
plt.xlabel("Species")
plt.ylabel("Count")
plt.show()

plt.figure(figsize=(6, 4))
plt.scatter(df['sepal_length'], df['sepal_width'], color='purple', alpha=0.6)
plt.title("Scatter: Sepal Length vs Sepal Width")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.show()

plt.figure(figsize=(6, 4))
plt.plot(df['petal_length'][:50], 'o-r')
plt.title("Line: Petal Length of First 50 Samples")
plt.xlabel("Sample Index")
plt.ylabel("Petal Length")
plt.show()

plt.figure(figsize=(6, 4))
plt.hist(df['petal_width'], bins=15, color='orange', edgecolor='black')
plt.title("Histogram: Petal Width Distribution")
plt.xlabel("Petal Width")
plt.ylabel("Frequency")
plt.show()

plt.figure(figsize=(6, 6))
plt.pie(students, labels=langs, autopct='%1.1f%%', colors=['lightblue', 'lightgreen', 'lightcoral'])
plt.title("Pie: Iris Species Distribution")
plt.axis('equal')