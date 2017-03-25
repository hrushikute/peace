import numpy as np

'''
a = np.array([1,2,3],dtype=float)

print a
print a.dtype
print a.ndim
print a.sum()
print a.shape
print a.std()

b=np.array([2 ,3 ,4],dtype=float)
print a +b
'''

training_DS=np.array([[7,25],[10,27],[6,17],[17,36],[14,52],[10,20]])

label=np.array(['N','Y','N','Y','Y','N'])
sugar=input('Enter thesugar level :')
Age=input('Enter Age :')


target=np.array([sugar,Age])

euclidean_distance=np.sum((training_DS-target)**2,axis=1)**0.5
sorted_distance=np.argsort(euclidean_distance)

check_dit={}

for i in range(3):
    if check_dit.has_key(label[sorted_distance[i]]):
        check_dit[label[sorted_distance[i]]]+=1
    else:
        check_dit[label[sorted_distance[i]]]=1

print 'Sugar Level {} and age {} of user has {} Daibetes' .format(sugar,Age,
                                                                  sorted(check_dit.items(),key=lambda x:x[1],reverse=True)[0][0])