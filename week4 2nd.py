import pandas as pd
from sklearn.datasets import load_iris

df = pd.DataFrame(load_iris().data, columns=load_iris().feature_names)
print("Covariance:\n", df.cov())
print("\nCorrelation:\n", df.corr())
