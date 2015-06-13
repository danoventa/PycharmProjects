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

