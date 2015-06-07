from __future__ import division
__author__ = 'Executor'

import pandas as pd
from pandas import Series, DataFrame
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('whitegrid')

from pandas.io.data import DataReader
from datetime import datetime



tech_list = ['AAPL', 'GOOG', 'MSFT', 'AMZN']
end = datetime.now()
start = datetime(end.year - 1, end.month, end.day)

for stock in tech_list:
    globals()[stock] = DataReader(stock, 'yahoo', start, end)

#print(AAPL)

print(AAPL.describe())
AAPL.info()

AAPL['Adj Close'].plot(legend=True, figsize=(10, 4))
plt.show()

AAPL['Volume'].plot(legend=True, figsize=(10, 4))
plt.show()