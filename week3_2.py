import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset (make sure train.csv is in the same folder)
df = pd.read_csv("Titanic.csv")

# Bar plot: Number of passengers by class
class_counts = df['Pclass'].value_counts().sort_index()
plt.bar(['Class 1', 'Class 2', 'Class 3'], class_counts)
plt.title('Number of Passengers by Class')
plt.xlabel('Pclass')
plt.ylabel('Count')
plt.show()
