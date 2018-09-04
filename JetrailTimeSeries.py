import pandas as pd
import matplotlib.pyplot as plt
from pandas import Series
from datetime import datetime
import numpy as np
import warnings
warnings.filterwarnings("ignore")
from sklearn.metrics import mean_squared_error
from math import sqrt



Train_data_file = "D:/My Work/Data Analysis/dataset/timeSeires/JetRail/Train_SU63ISt.csv"
Test_data_file = "D:/My Work/Data Analysis/dataset/timeSeires/JetRail/Test_0qrQsBZ.csv"
Train_data = pd.read_csv(Train_data_file)
Test_data = pd.read_csv(Test_data_file)

print(Train_data.head(10))
print(Train_data.describe())
print(Train_data.shape)
print(Train_data.info())

# Keep a copy or original
Train_data_orig = Train_data.copy()
Test_data_orig = Test_data.copy()


Train_data['Datetime'] = pd.to_datetime(Train_data.Datetime, format='%d-%m-%Y %H:%M')
Test_data['Datetime'] = pd.to_datetime(Test_data.Datetime, format='%d-%m-%Y %H:%M')
Train_data_orig['Datetime'] = pd.to_datetime(Train_data_orig.Datetime, format='%d-%m-%Y %H:%M')
Test_data_orig['Datetime'] = pd.to_datetime(Test_data_orig.Datetime, format='%d-%m-%Y %H:%M')


#We made some hypothesis for the effect of hour, day, month and year on the passenger count. So, let’s extract the year, month, day and hour from the Datetime to validate our hypothesis.

for i in (Train_data, Test_data, Train_data_orig, Test_data_orig):
    i['year'] = i.Datetime.dt.year
    i['month'] = i.Datetime.dt.month
    i['day'] = i.Datetime.dt.day
    i['Hour'] = i.Datetime.dt.hour

#We made hypotheisis that day of week
Train_data['day_of_week'] = Train_data['Datetime'].dt.dayofweek
temp = Train_data['Datetime']

print(Train_data.head(10))
# weekend make it 0 weekdday make it 1

def WeekendApplyer(row):
    if row.dayofweek == 5 or row.dayofweek == 6:
        return  1
    else:
        return 0

temp2 = Train_data['Datetime'].apply(WeekendApplyer)
Train_data['weekend'] = temp2

Train_data.index = Train_data['Datetime']
df = Train_data.drop('ID', 1)


plt.plot(df.Count, label='Passenger-Count')
plt.title('Time Series')
plt.xlabel("Time (year-month)")
plt.ylabel("Passenger Count")
plt.legend(loc='best')
plt.show()
#

Train_data.groupby('year')['Count'].mean().plot.bar()
plt.show()

Train_data.groupby('month')['Count'].mean().plot.bar()
plt.show()

Train = Train_data.ix['2012-08-25':'2014-06-24']
valid = Train_data.ix['2014-06-24':'2014-09-25']

Train.Count.plot(figsize=(15,8), title='Daily Ridership', fontsize=14, label='train')
valid.Count.plot(figsize=(15,8), title='Daily Ridership', fontsize=14, label='valid')
plt.xlabel("Datetime")
plt.ylabel("Pasenger count")
plt.legend(loc='best')
plt.show()

#prediction using moving average

y_hat_avg = valid.copy()
y_hat_avg['moving_avg_forecast'] = Train['Count'].rolling(10).mean().iloc[-1]  #average of last 10 obbservation
plt.figure(figsize=(15,5))
plt.plot(Train['Count'], label='Train')
plt.plot(valid['Count'], label='Valid')
plt.plot(y_hat_avg['moving_avg_forecast'], label='Moving Average Forecast using 10 observations')
plt.legend(loc='best')
plt.show()

rms = sqrt(mean_squared_error(valid.Count,y_hat_avg['moving_avg_forecast']))
print("With 10 rolling RMSE :{}".format(rms))

y_hat_avg = valid.copy()
y_hat_avg['moving_avg_forecast'] = Train['Count'].rolling(30).mean().iloc[-1]  #average of last 10 obbservation
plt.figure(figsize=(15,5))
plt.plot(Train['Count'], label='Train')
plt.plot(valid['Count'], label='Valid')
plt.plot(y_hat_avg['moving_avg_forecast'], label='Moving Average Forecast using 30 observations')
plt.legend(loc='best')
plt.show()

rms = sqrt(mean_squared_error(valid.Count,y_hat_avg['moving_avg_forecast']))
print("With 30 rolling RMSE :{}".format(rms))

y_hat_avg = valid.copy()
y_hat_avg['moving_avg_forecast'] = Train['Count'].rolling(80).mean().iloc[-1]  #average of last 10 obbservation
plt.figure(figsize=(15,5))
plt.plot(Train['Count'], label='Train')
plt.plot(valid['Count'], label='Valid')
plt.plot(y_hat_avg['moving_avg_forecast'], label='Moving Average Forecast using 80 observations')
plt.legend(loc='best')
plt.show()

rms = sqrt(mean_squared_error(valid.Count,y_hat_avg['moving_avg_forecast']))
print("With 80 rolling RMSE :{}".format(rms))


# Simple Exponential Smoothing Here the predictions are made by assigning larger weight to the recent values and lesser weight to the old values.

from statsmodels.tsa.api import Holt,SimpleExpSmoothing

y_hat_avg = valid.copy()
fit2 = SimpleExpSmoothing(np.asarray(Train['Count'])).fit(smoothing_level=0.6, optimized=False)
y_hat_avg['SES'] = fit2.forecast(len(valid))
plt.figure(figsize=(16,8))
plt.plot(Train['Count'], label='Train')
plt.plot(valid['Count'], label='Valid')
plt.plot(y_hat_avg['SES'], label='SES')
plt.legend(loc='best')
plt.show()
rms = sqrt(mean_squared_error(valid.Count,y_hat_avg['SES']))
print("SES RMSE :{}".format(rms))

#Holts linear trend model

import statsmodels.api as sm
sm.tsa.seasonal_decompose(Train.Count).plot()
result = sm.tsa.stattools.adfuller(Train_data.Count)
plt.show()

y_hat_avg = valid.copy()
fit1 = Holt(np.asarray(Train['Count'])).fit(smoothing_level=0.3, smoothing_slope=0.1)
y_hat_avg['Holt_linear'] = fit1.forecast(len(valid))
plt.figure(figsize=(16,8))
plt.plot(Train['Count'], label='Train')
plt.plot(valid['Count'], label='Valid')
plt.plot(y_hat_avg['Holt_linear'], label='Holt linear')
plt.legend(loc='best')
plt.show()

rms = sqrt(mean_squared_error(valid.Count,y_hat_avg['Holt_linear']))
print("Holt Linear  RMSE :{}".format(rms))

#  Parameter tuning for ARIMA model

from statsmodels.tsa.stattools import adfuller
def test_stationary(timeserires):
    #Determining rolling statistics
    rolmean = pd.rolling_mean(timeserires, window=24) #24 hours on each day
    rolstd = pd.rolling_std(timeserires, window=24)

    #Plot rolling statistics
    orig = plt.plot(timeserires, color='blue', label='Original')
    mean = plt.plot(rolmean, color='red', label='Rolling Mean')
    std = plt.plot(rolstd, color='red', label='Rolling Standard Deviation')
    plt.legend(loc='best')
    plt.title("Rolling Meand and Standard Deviation")
    plt.show(block=False)

    #perform Dicky fuller test :
    print('Results of Dickey-Fuller test :')
    dftest = adfuller(timeserires,autolag='AIC')
    dfoutput = pd.Series(dftest[0:4], index=['Test Statistic', 'p-value', '#Lags Used', 'Number of Observations used'])
    for key, value in dftest[4].items():
        dfoutput['Critical Value (%s) '%key] = value
    print(dfoutput)

from matplotlib.pylab import rcParams
rcParams['figure.figsize'] =20,10
test_stationary(Train_data_orig['Count'])

