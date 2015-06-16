__author__ = 'Noventa'

import numpy as np
import pandas as pd
from pandas import Series, DataFrame


import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('whitegrid')

from sklearn.datasets import load_boston

boston = load_boston()

print(boston.DESCR)

plt.hist(boston.target, bins=50)

plt.xlabel('Prices in $1000s')
plt.ylabel('Number of Houses')

plt.show()

plt.scatter(boston.data[:, 5], boston.target)


plt.ylabel('Price in $1000s')
plt.xlabel('Number of rooms')

boston_df = DataFrame(boston.data)

boston_df.columns = boston.feature_names

print(boston_df.head())

boston_df['Price'] = boston.target

boston_df.head()

sns.lmplot('RM', 'Price', data=boston_df)
plt.show()

