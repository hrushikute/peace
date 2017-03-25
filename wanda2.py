import pandas as pd
import matplotlib.pyplot as plt

raw_data={'Subject':['1','2','3','4','5','6','7','8','9','10'],
          'Marks':[51,34,67,34,78,86,78,23,12,45]}

df=pd.DataFrame(raw_data)

print df

raw_data1={ 'Subject':['1','3','2','4','5'],
            'FirstName':['Alex','Wanga','Fomd','Yuri','carlos'],
            'LastName':['Kus','Urao','Ori','Laz','Eut']}

df2=pd.DataFrame(raw_data1)

print df.merge(df2,on='Subject',how='left')

print df

rating = pd.read_csv(r'/home/hrushi/Dropbox/Ethans 19th November Batch/Day 17/ml-100k/u.data',sep='\t',names=['User Id','Movie Id','Rating','TimeStamp'])

movie = pd.read_csv(r'/home/hrushi/Dropbox/Ethans 19th November Batch/Day 17/ml-100k/u.item',sep='|',names=['Movie Id','Movie Name'],usecols=range(2))

rating_movie=rating.merge(movie,on='Movie Id',how='left')

print rating_movie.head(5)

'''
#print rating_movie.groupby('Movie Name').size().sort_values(ascending=False)[:10]



rating_movie.groupby('Movie Name').size().sort_values(ascending=False)[:5].plot('bar')

plt.show()

#rating_users=pd.read_csv(r'/home/hrushi/Dropbox/Ethans 19th November Batch/Day 17/ml-100k/u.user',sep='|',names=['User Id','Age','Gender'],usecols=range(3))

'''

rating_movie1=rating_movie.head(5).transpose()

print rating_movie1


pd.read_j