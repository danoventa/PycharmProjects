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
print(source.head())

poll_df = source.groupby(['Start Date'], as_index=False).mean()
print(poll_df.head())

poll_df.plot('Start Date', 'Difference', figsize=(12, 4), marker='o', linestyle='-', color='purple')
plt.show()

row_in=0
xlimit = []

for date in poll_df['Start Date']:
    if date[0:7] == '2012-10':
        xlimit.append(row_in)
        row_in += 1
    else:
        row_in += 1

print(min(xlimit))
print(max(xlimit))

poll_df.plot('Start Date', 'Difference', figsize=(12, 4), marker='o', linestyle='-', color='purple', xlim=(329,356))
# dabate 1
plt.axvline(x=329+2, linewidth=4, color='grey')
# debate 2
plt.axvline(x=329+10, linewidth=4, color='grey')
#debate 3
plt.axvline(x=329+21, linewidth=4, color='grey')

plt.show()

