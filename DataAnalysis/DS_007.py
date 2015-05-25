__author__ = 'Executor'

import pandas.io.data as pweb
import datetime

prices = pweb.get_data_yahoo(['CVX', 'XOM', 'BP'], start=datetime.datetime(2010, 1, 1),
                             end=datetime.datetime(2013, 1, 1))['Adj Close']
#print(prices)
print(prices.head())

volume = pweb.get_data_yahoo(['CVX', 'XOM', 'BP'], start=datetime.datetime(2010, 1, 1),
                             end=datetime.datetime(2013, 1, 1))['Volume']
print(volume.head())
rets = prices.pct_change()
corr = rets.corr
print(corr)
prices.plot()
import matplotlib.pyplot as plt
plt.show()
import seaborn as sn

sn.corrplot(rets, annot=False, diag_names=False)
plt.show()



