from __future__ import division
__author__ = 'Noventa'

import matplotlib
matplotlib.use('TkAgg')

import pandas as pd
from pandas import Series, DataFrame
import numpy
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')

''' Didn't need some of the other imports, since using a direct csv reader '''

''' no need to do strinio since we're not working with python 2.7 '''

url = 'http://elections.huffingtonpost.com/pollster/2012-general-election-romney-vs-obama.csv'
source = pd.read_csv(url)

print(source.info())
print(source.head())

sns.factorplot('Affiliation', data=source)
plt.show()

sns.factorplot('Affiliation', data=source, hue='Population')
plt.show()

avg = pd.DataFrame(source.mean())
avg.drop('Number of Observations', axis=0, inplace=True)

std = pd.DataFrame(source.std())
std.drop('Number of Observations', axis=0, inplace=True)
std.head()

avg.plot(yerr=std, kind='bar', legend=False)
plt.show()

poll_avg = pd.concat([avg, std], axis=1)
poll_avg.columns = ['Average', 'STD']
print(poll_avg)

source.plot(x = 'End Date', y=['Obama', 'Romney', 'Undecided'], linestyle='', marker='o')
plt.show()

from datetime import datetime

source['Difference'] = (source.Obama - source.Romney)/100
source.head()

