import numpy as np
import pandas as pd
df = pd.DataFrame({
    "date": pd.date_range(start="2022-11-01", periods=5, freq="D"), "temp": np.random.randint(18, 30, size=5)})
print(df)