import math

training_dataset={1:(2,3),2:(3,7),3:(6,7),4:(7,6),5:(4,2),6:(10,3)}

x=input('Enter the X value :')
y=input('Enter the Y value :')

target =(x,y)
key_distance={}
'''
tr_ds={}
counter=1
infile=open(r'points.txt')
for line in infile.readline():
    print line ,counter
    tr_ds[counter]=line
    counter+=1
    continue

print tr_ds
'''
for key,value in training_dataset.iteritems():
    length=len(value)
    sum=0
    for i in range(length):
        sum=sum+(target[i]-value[i])**2
    euclidean_distance=math.sqrt(sum)
    key_distance[key]=euclidean_distance

target_Set=training_dataset[sorted(key_distance.items(),key= lambda x:x[1])[0][0]]
print target_Set