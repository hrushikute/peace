import pandas as pd

#s=pd.Series(data,index)
#Series of list of list
s=pd.Series([['Hsk','YSK','ASK'],[30,24,29]],index=('Names','Age'))

print s
#Series of dictionary
cities=pd.Series({'Pune':1000,'Delhi':2000,'Banglore':500,'Nagpur':800,'Danam':None})

print cities[cities >=1000]

'''
print cities.isnull()


df=pd.DataFrame({'Class':['Python','Java'],'City':['Pune','Delhi']})

print df

# Only can access the value based on Cloumn and row and not on row column
df1=pd.DataFrame({'Class':['Python','Java'],'City':['Pune','Delhi']},index=('Firstrow','Second Row'))
print df1
print df1['City']['Firstrow']


df2=df1.transpose()
print df2
print df2['Firstrow']['City']
'''