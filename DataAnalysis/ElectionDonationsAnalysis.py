from __future__ import division

import pandas as pd
from pandas import Series, DataFrame
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')


donor_df = pd.read_csv('/Users/Noventa/Election_Donor_Data.csv', low_memory=False)
print(donor_df.info())

donor_df.head()

donor_df['contb_receipt_amt'].value_counts()

don_mean = donor_df['contb_receipt_amt'].mean()
don_std = donor_df['contb_receipt_amt'].std()

print('The average donation was %.2f with std %.2f' %(don_mean, don_std))

top_donor = donor_df['contb_receipt_amt'].copy()

top_donor.sort()
print(top_donor)

top_donor = top_donor[top_donor > 0]


top_donor.sort()
top_donor.head()

com_don = top_donor[top_donor < 2500]

com_don.hist(bins=100)

plt.show()

candidates = donor_df.cand_nm.unique()

print(candidates)


party_map = {'Bachmann, Michelle': 'Republican',
           'Cain, Herman': 'Republican',
           'Gingrich, Newt': 'Republican',
           'Huntsman, Jon': 'Republican',
           'Johnson, Gary Earl': 'Republican',
           'McCotter, Thaddeus G': 'Republican',
           'Obama, Barack': 'Democrat',
           'Paul, Ron': 'Republican',
           'Pawlenty, Timothy': 'Republican',
           'Perry, Rick': 'Republican',
           "Roemer, Charles E. 'Buddy' III": 'Republican',
           'Romney, Mitt': 'Republican',
           'Santorum, Rick': 'Republican'}

donor_df['Party'] = donor_df.cand_nm.map(party_map)


donor_df = donor_df[donor_df.contb_receipt_amt > 0]
donor_df.head()

donor_df.groupby('cand_nm')['contb_receipt_amt'].count()

donor_df.groupby('cand_nm')['contb_receipt_amt'].sum()
cand_amount = donor_df.groupby('cand_nm')['contb_receipt_amt'].sum()
i = 0
for don in cand_amount:
    print('The candidate %s raised %.0f dollars' %(cand_amount.index[i], don))
    print('\n')
    i += 1

cand_amount.plot(kind='bar')

donor_df.groupby('Party')['contb_receipt_amt'].sum().plot(kind='bar')

occupation_df = donor_df.pivot_table('contb_receipt_amt', index='contbr_occupation', columns = 'Party', aggfunc='sum')
occupation_df.head()

occupation_df.tail()
print(occupation_df.shape)

occupation_df = occupation_df[occupation_df.sum(1) > 1000000]
print(occupation_df.shape)

occupation_df.plot(kind='bar')
occupation_df.plot(kind='barh', figsize=(10, 12), cmap='seismic')

plt.show()

occupation_df.drop(['INFORMATION REQUESTED PER BEST EFFORTS', 'INFORMATION REQUESTED'], axis = 0, inplace = True)
occupation_df.loc['CEO'] = occupation_df.loc['CEO'] + occupation_df.loc['C.E.O.']

occupation_df.drop('C.E.O.', inplace=True)

occupation_df.plot(kind='barh', figsize=(10, 12), cmap='seismic')

plt.show()


