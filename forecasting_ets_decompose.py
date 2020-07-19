# %%

import numpy as np
import pandas as pd
from matplotlib import pyplot
from pandas.core.tools.numeric import to_numeric
from statsmodels.tsa.seasonal import seasonal_decompose

pyplot.style.use('dark_background')
df = pd.read_csv('data/udacity/07-02-13 Bookings.csv', skiprows=0)

df['Month'] = pd.to_datetime(df['Month'], format='%b').dt.month
df['Date'] = pd.to_datetime(df[['Year', 'Month']].assign(DAY=1), format='%Y%b%d')
data = df[['Date', 'Bookings']]
data = data.set_index('Date')

result = seasonal_decompose(data, model='additive', period=12)
print(result.trend)
print(result.seasonal)
print(result.resid)
print(result.observed)

result.plot()
pyplot.show()
