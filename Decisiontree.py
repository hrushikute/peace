from sklearn import tree
import numpy as np

# Data set naming

#Female - 0 Male -1
#Passed out 12 -0 in 12th - 1
#JEE Coaching - 0 No JEE Coaching 1

data_Set=np.array([[0,1,1],[1,1,1],[1,0,1],[1,0,0],[1,0,0],[0,1,1],[0,1,1],[0,1,1],[0,1,1],[1,0,0]])

lables=['Selected','Selected','Selected','Selected','Selected','Not Selected','Not Selected','Not Selected', 'NotSelected','Not Selected']

x_test=np.array([[0,0,1]])

model=tree.DecisionTreeClassifier()
model.fit(data_Set,lables)

model.score(data_Set,lables)
predicted=model.predict(x_test)

print predicted