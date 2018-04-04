"""
@author: Satyajit Pattnaik

"""

from fbprophet import Prophet
import numpy as np
import pandas as pd

df = pd.read_csv('raw_data.csv')

df = df.rename(columns={'Value': 'y', 'Timestamp':'ds'})

df['y_orig'] = df['y'] # to save a copy of the original data..you'll see why shortly. 
# log-transform y
df['y'] = np.log(df['y'])

model = Prophet() #instantiate Prophet
model.fit(df) #fit the model

''' 
Valid values for freq:
        'year': 'A',
        'quarter': 'Q',
        'month': 'M',
        'day': 'D',
        'hour': 'H',
        'minute': 'T',
        'second': 'S',
        'millisecond': 'L',
        'microsecond': 'U',
        'nanosecond': 'N'}
'''


future_data = model.make_future_dataframe(periods=6, freq = '60T') #make the future dataframe 

forecast_data = model.predict(future_data) #Prediction

#Converting the data back to original
forecast_data_orig = forecast_data # make sure we save the original forecast data
forecast_data_orig['yhat'] = np.exp(forecast_data_orig['yhat'])
forecast_data_orig['yhat_lower'] = np.exp(forecast_data_orig['yhat_lower'])
forecast_data_orig['yhat_upper'] = np.exp(forecast_data_orig['yhat_upper'])

df['y_log']=df['y'] #copy the log-transformed data to another column
df['y']=df['y_orig']

model.plot(forecast_data_orig)