import pandas as p
import seaborn as s
import matplotlib.pyplot as m
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
da=p.read_csv("breastcancer.csv")
da.drop(['id'],axis=1,inplace=True)
da.diagnosis=[1 if i=='M' else 0 for i in da.diagnosis]
x=da.drop(['diagnosis'],axis=1)
y=da.diagnosis.values
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=30)
model1=RandomForestClassifier()
model1.fit(x_train,y_train)
y_pred1=model1.predict(x_test)
print("\nAccuracy of the model using Random Forest Regression alogorithmis",accuracy_score(y_test,y_pred1))
cm=confusion_matrix(y_test,y_pred1)
s.heatmap(cm,annot=True)
m.show()