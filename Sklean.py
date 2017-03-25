from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import matplotlib.pyplot as plt

clf= KNeighborsClassifier()

data_set=np.array([[3,104],[2,100],[1,81],[100,10],[99,5],[98,2]])
label=['R','R','R','A','A','A']

clf.fit(data_set,label)

target=np.array([[10,99]])

print "Type of movie is: {}".format(clf.predict(target))

x_axis=data_set[:,0]
y_axis=data_set[:,1]
color=[10,10,10,100,100,100,300]
size=[40,40,40,40,40,40,100]

x_axis=np.append(x_axis,target[:,0])
y_axis=np.append(y_axis,target[:,1])

plt.xlabel('Number of Kicks')
plt.ylabel('Number of Kisses')

plt.style.use('ggplot')
plt.scatter(x_axis,y_axis,color,size)
plt.show()