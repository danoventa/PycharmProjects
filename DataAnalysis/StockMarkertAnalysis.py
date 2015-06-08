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

ma_day = [10, 20, 50]

for ma in ma_day:
    column_name = "MA for %s days" %(str(ma))
    AAPL[column_name] = pd.rolling_mean(AAPL['Adj Close'], ma)

AAPL[['Adj Close', 'MA for 10 days', 'MA for 20 days', 'MA for 50 days']].plot(subplots=False, figsize=(10, 4))

plt.show()

AAPL['Daily Return'] = AAPL['Adj Close'].pct_change()
AAPL['Daily Return'].plot(figsize=(10, 4), legend=True, linestyle='--', marker='o')
plt.show()

sns.distplot(AAPL['Daily Return'].dropna(), bins=100, color='purple')
plt.show()

AAPL['Daily Return'].hist(bins=100)
plt.show()

closing_df = DataReader(tech_list, 'yahoo', start, end)['Adj Close']

print(closing_df.head())

tech_rets = closing_df.pct_change()
print(tech_rets.head())

sns.jointplot('GOOG', 'GOOG', tech_rets, kind = 'scatter', color='seagreen')
plt.show()

sns.jointplot('GOOG', 'MSFT', tech_rets, kind='scatter')
plt.show()

sns.pairplot(tech_rets.dropna())
plt.show()

returns_fig = sns.PairGrid(tech_rets.dropna())
returns_fig.map_upper(plt.scatter, color='purple')
returns_fig.map_lower(sns.kdeplot, cmap='cool_d')
returns_fig.map_diag(plt.hist, bins=30)
plt.show()

returns_fig = sns.PairGrid(closing_df)
returns_fig.map_upper(plt.scatter, color='purple')
returns_fig.map_lower(sns.kdeplot, cmap='cool_d')
returns_fig.map_diag(plt.hist, bins=30)
plt.show()

sns.corrplot(tech_rets.dropna(), annot=True)
plt.show()

sns.corrplot(closing_df, annot=True)
plt.show()

''' analyze the risk of a stock '''
rets = tech_rets.dropna()
area = np.pi * 20
plt.scatter(rets.mean(), rets.std(), s = area)
plt.xlabel('Expected Return')
plt.ylabel('Risk')

for label, x, y in zip(rets.columns, rets.mean(), rets.std()):
    plt.annotate(
        label,
        xy = (x, y), xytext = (50, 50),
        textcoords = 'offset points', ha = 'right', va = 'bottom',
        arrowprops = dict(arrowstyle = '-', connectionstyle = 'arc3,rad=-0.3')
    )

plt.show()

print(rets['AAPL'].quantile)

''' montecarlo '''
days = 365
dt = 1/days
mu = rets.mean()['GOOG']
sigma = rets.std()['GOOG']

def stock_monte_carlo( start_price, days, mu, sigma):

    price = np.zeros(days)
    price[0] = start_price

    shock = np.zeros(days)
    drift = np.zeros(days)

    for x in range(1, days):

        shock[x] = np.random.normal(loc=mu*dt, scale=sigma*np.sqrt(dt))
        drift[x] = mu*dt
        price[x] = price[x-1]+(price[x-1] * (drift[x] + shock[x]))

    return price

print(GOOG.head())

start_price = 557.15

for run in range(100):
    plt.plot(stock_monte_carlo(start_price, days, mu, sigma))

plt.xlabel('Days')
plt.ylabel('Price')
plt.title('Montecarlo Analysis for Google')
plt.show()

runs = 10000

simulations = np.zeros(runs)

for runs in range(runs):
    simulations[run] = stock_monte_carlo(start_price, days, mu, sigma)[days-1]

q = np.percentile(simulations, 1)
plt.hist(simulations, bins=200)
plt.figtext(0.6, 0.8, s="Start price: $%.2f" % start_price)
plt.figtext(0.6, 0.7, s="Mean final price: $%.2f" % simulations.mean())
plt.figtext(0.6, 0.6, s="Start price: $%.2f" % (start_price - q,))
plt.figtext(0.15, 0.6, s="Start price: $%.2f" % q)

plt.axvline(x = q, linewidth=4, color='r')
plt.title(u"Final price distribution for google stock after %s days" % days, weight='bold')

plt.show()