import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Titanic.csv")
survivor_data = df.groupby(['Pclass', 'Survived']).size().unstack()
plt.plot(survivor_data.index, survivor_data[0], 'o-r', label='Not Survived')
plt.plot(survivor_data.index, survivor_data[1], 'o-b', label='Survived')
plt.title('Survivors vs Non-Survivors by Class')
plt.xlabel('Pclass')
plt.ylabel('Number of Passengers')
plt.legend()
plt.show()
