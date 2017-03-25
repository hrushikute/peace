'''

1. Import an algorithm from sklearn
2. decide your dataset(numpy scipy pandas)
3.decide the label
4.decide teh classifier
5,fir a dataset with label
6.predict

'''
# Decision tree.
from sklearn import svm
import numpy as np

training_dataset=np.array([[120,10],[80,30],[10,40],[5,65],[60,80]])

labels= ['Romantic','Romantic','Action','Action','Action']

predict=np.array([75,5]).reshape(1,-1)

clf=svm.SVC(kernel='linear')
#clf =tree.DecisionTreeClassifier(criterion='gini')

clf.fit(training_dataset,labels)



print 'predict data {} to {} lable'.format(predict,clf.predict(predict))
