import pandas as p
import matplotlib.pyplot as m
da=p.read_csv("mallcustomers.csv")
x=da.iloc[:,[3,4]].values
from sklearn.cluster import KMeans
li=[]
for i in range(1,11):
    mod=KMeans(n_clusters=i,init='k-means++', random_state=42,n_init=10)
    mod.fit(x)
    li.append(mod.inertia_)
m.plot(range(1,11), li)
m.title("Elbow Method")
m.xlabel('Number of Clusters'); m.ylabel('li'); m.show()
mod=KMeans(n_clusters=5,init='k-means++', random_state=42,n_init=10)
y_pred=mod.fit_predict(x)
m.scatter(x[y_pred==0,0],x[y_pred==0,1],s=100, c='blue', label='Cluster 1')
m.scatter(x[y_pred==1,0],x[y_pred==1,1],s=100,c='g', label='Cluster 2')
m.scatter(x[y_pred==2,0],x[y_pred==2,1],s=100, c='lime', label='Cluster 3')
m.scatter(x[y_pred==3,0],x[y_pred==3,1],s=100, c='red', label='Cluster 4')
m.scatter(x[y_pred==4,0],x[y_pred==4,1],s=100, c='k', label='Cluster 5')
m.scatter(mod.cluster_centers_[:,0],mod.cluster_centers_[:,1],s=300,c='yellow')
m.title("clusters of customers")
m.xlabel("Annual Income"); m.ylabel("Spending Score(1-100)")
m.legend();m.show()
