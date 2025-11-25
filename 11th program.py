import numpy as np
import pandas as pd

df = pd.DataFrame({
    "date": pd.date_range(start="2022-11-01", periods=21, freq="D"),
    "temp": np.random.randint(18, 30, size=21)
})

print(df.head())

df_weekly = df.resample("W", on="date").mean()
df_weekly.head()