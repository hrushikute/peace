'''

1. Import an algorithm from sklearn
2. decide your dataset(numpy scipy pandas)
3.decide the label
4.decide teh classifier
5,fir a dataset with label
6.predict

'''
# Decision tree.
from sklearn import naive_bayes
import numpy as np
## This for plotting th graph
import matplotlib.pylab as plt

training_dataset=np.array([[120,10],[80,30],[10,40],[5,65],[60,80]])

labels= ['Romantic','Romantic','Action','Action','Action']

predict=np.array([75,5]).reshape(1,-1)

clf=naive_bayes.GaussianNB()
#clf =tree.DecisionTreeClassifier(criterion='gini')

clf.fit(training_dataset,labels)

x=training_dataset[:,0]
y=training_dataset[:,1]

sizeoflable=[50,50,50,50,50]
coloroflabel=[50,50,50,50,50]

#discription of x and Y axis
plt.xlabel("Nummber of kisess")
plt.ylabel("Number of kicks")

plt.style.use('ggplot')
plt.scatter(x,y,sizeoflable,coloroflabel)
plt.colorbar()
#plt.show()


print 'predict data {} to {} lable'.format(predict,clf.predict(predict))

predict =np.array([75,5]).reshape(2,)

x = np.append(x,predict[0])
y = np.append(y,predict[1])

sizeoflable.append(100)
coloroflabel.append(100)

plt.scatter(x,y,sizeoflable,coloroflabel)
plt.show()