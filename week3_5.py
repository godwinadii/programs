import matplotlib.pyplot as plt
import numpy as np

# 1. Prepare Your Data
# Let's use the 'Age' column from your provided train.csv data.
# We'll manually extract some ages for this simple example.
# In a real scenario, you'd load the CSV and extract the column.
ages = [22, 38, 26, 35, 35, 54, 2, 27, 14, 4, 58, 20, 39, 14, 55, 2, 31, 35, 34, 15, 28, 8, 38, 19, 40, 66, 28, 42, 21, 18, 14, 40, 27, 3, 19, 18, 7, 21, 49, 29, 65, 21, 28.5, 5, 11]

# You might have missing values (like 'np.nan' in a real dataset).
# For a simple histogram, it's best to remove them.
ages = [age for age in ages if not np.isnan(age)]

# 2. Plot the Histogram
plt.hist(ages, bins=10, edgecolor='black') # 'bins' controls the number of bars
plt.title('Age Distribution of Passengers')
plt.xlabel('Age')
plt.ylabel('Number of Passengers')
plt.grid(axis='y', alpha=0.75) # Optional: adds a grid
plt.show()
