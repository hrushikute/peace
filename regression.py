import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets,linear_model


#load  the daibetes data set
daibetes=datasets.load_diabetes()

print daibetes

#use only one feature
daibetes_X =daibetes.data[:,2].reshape(len(daibetes.data),1)

#split the data into training or test dat set

daibetes_X_train= daibetes_X[:-20]
daibetes_X_test=daibetes_X[-20:]

#split the target into trianing /test sets

daibetes_y_train=daibetes.target[:-20]
daibetes_y_test=daibetes.target[-20:]

#Create a liner regeression object

regr=linear_model.LinearRegression()


# Train the model using the training sets

regr.fit(daibetes_X_train,daibetes_y_train)


#plot outputs

plt.scatter(daibetes_X_test,daibetes_y_test,color='black')
plt.plot(daibetes_X_test,regr.predict(daibetes_X_test),color='blue',linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()