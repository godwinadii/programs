import pandas as pd
import matplotlib.pyplot as m
import seaborn as s

# --- Load and preprocess the data ---
da = pd.read_csv("matches.csv")
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
#Transformation
categorical_columns = ['city', 'team1', 'team2', 'toss_winner',
'toss_decision', 'result', 'player_of_match', 'venue', 'umpire1',
'umpire2','winner','date']
label_encoders = {}
for column in categorical_columns:
    label_encoders[column] = LabelEncoder()
da[column] = label_encoders[column].fit_transform(da[column])
X = da.drop('winner', axis=1)
y = da['winner']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,
random_state=42)
print("Train set:", X_train.shape, y_train.shape)
print("Test set:", X_test.shape, y_test.shape)
