import pandas as pd
import matplotlib.pyplot as plt

# Load the Titanic dataset (update the path if needed)
df = pd.read_csv("Titanic.csv")  # Make sure this file is in the same folder as your script

# Drop rows with null Age or Fare
df_scatter = df[['Age', 'Fare']]

# Plot
plt.scatter(df_scatter['Age'], df_scatter['Fare'], color='r', label='Age vs Fare')
plt.title('Titanic Passenger Age vs Fare')
plt.xlabel('Age')
plt.ylabel('Fare')
plt.legend()
plt.show()
