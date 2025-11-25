import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Titanic.csv")
gender_counts = df['Sex'].value_counts()
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.2f%%')
plt.title('Gender Distribution on Titanic')
plt.show()
