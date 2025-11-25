import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/Komal/OneDrive/Desktop/5th sem/Titanic.csv")

df_clean = df.dropna(subset=['Age', 'Fare'])

pclass_count = df['Pclass'].value_counts().sort_index()
class_labels = ['Class 1', 'Class 2', 'Class 3']
class_values = pclass_count.values.tolist()

plt.figure(figsize=(6, 4))
plt.bar(class_labels, class_values, color='skyblue')
plt.title("Passenger Count by Class")
plt.xlabel("Passenger Class")
plt.ylabel("Number of Passengers")
plt.tight_layout()
plt.show()

plt.figure(figsize=(6, 4))
plt.scatter(df_clean['Age'], df_clean['Fare'], color='red', alpha=0.6)
plt.title("Age vs Fare (Titanic)")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.tight_layout()
plt.show()

fare_50 = df['Fare'].head(50)
passenger_indices = list(range(1, 51))

plt.figure(figsize=(6, 4))
plt.plot(passenger_indices, fare_50, marker='o', linestyle='-', color='green')
plt.title("Fare of First 50 Passengers")
plt.xlabel("Passenger Index")
plt.ylabel("Fare")
plt.tight_layout()
plt.show()

plt.figure(figsize=(6, 4))
plt.hist(df_clean['Age'], bins=20, color='orange', edgecolor='black')
plt.title("Age Distribution of Passengers")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

gender_counts = df['Sex'].value_counts()
gender_labels = gender_counts.index.tolist()
gender_sizes = gender_counts.values.tolist()

plt.figure(figsize=(6, 6))
plt.pie(gender_sizes, labels=gender_labels, autopct='%1.2f%%', colors=['lightblue', 'pink'])
plt.title("Gender Distribution on Titanic")
plt.axis('equal')
plt.tight_layout()
plt.show()
