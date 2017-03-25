'''
Kmeans algotrithm for prediction.

Unsuprvised learning.

'''

#Note look for import

from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

coordinates = np.array([[120,10],[80,30],[10,40],[5,65],[110,40]])
kmeans=KMeans(n_clusters=3)
kmeans.fit(coordinates)

centroids=kmeans.cluster_centers_
labels=kmeans.labels_

print 'Printing all the centroids',centroids
print 'Printing all labels',labels

colors=["g.","r.","b."]

for i in range(len(coordinates)):
    print ("coordinate:",coordinates[i],"label:",labels[i])
    plt.plot(coordinates[i][0] ,coordinates[i][1],colors[labels[i]])

plt.scatter(centroids[:,0],centroids[:,1],marker="x",s=150,linewidths=5,zorder=10)

plt.show()