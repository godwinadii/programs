#TIME SERIES OUTLIER
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data={
    "Date": ["2023-01-01", "2023-01-02", "2023-01-03", "2023-01-04", "2023-01-05",
            "2023-01-06", "2023-01-07", "2023-01-08", "2023-01-09", "2023-01-10"],
    "Temp": [22.5, 21.8, 23.0, 25.2, 44.5, 22.0, 21.5, 45.0, 23.3, 22.2]
}
    
df=pd.DataFrame(data)

#TIME SERIES OUTLIERS
x=df.Temp
y=df.Date
plt.scatter(x,y)
plt.xlabel("Temp")
plt.ylabel("Date")
plt.title("TIME SERIES OUTLIERS")
plt.show()