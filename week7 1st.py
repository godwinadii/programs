import pandas as p
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
# Breast cancer dataset
data = p.read_csv("breastcancer.csv")
data.info()
data.drop(["id"],axis=1,inplace=True)
M=data[data.diagnosis=="M"]
B=data[data.diagnosis=="B"]
data.diagnosis=[1 if i == "M" else 0 for i in data.diagnosis]
x=data.drop(["diagnosis"],axis=1)
y=data.diagnosis.values
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=42)
from sklearn.tree import DecisionTreeRegressor
model=DecisionTreeRegressor()
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
print("\nAccuracy of the model using Decision tree regression algorithmis ",r2_score(y_test,y_pred))
from sklearn.ensemble import RandomForestRegressor
model1 = RandomForestRegressor()
model1.fit(x_train,y_train)
y_pred1 = model1.predict(x_test)
print("\nAccuracy of the model using Random forest regression algorithmis ",r2_score(y_test,y_pred1))
from sklearn.svm import SVR
model2 = SVR(kernel='rbf')
model2.fit(x_train,y_train)
y_pred2 = model2.predict(x_test)
print("\nAccuracy of the model using Support vector regression algorithmis ",r2_score(y_test,y_pred2))