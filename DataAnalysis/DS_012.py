__author__ = 'Noventa'

import numpy as np
import pandas as pd
from numpy.random import randn

from scipy import stats

import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')
print(tips.head())

sns.lmplot('total_bill', 'tip', tips)
plt.show()

sns.lmplot('total_bill', 'tip', tips,
           scatter_kws={'marker':'o', 'color':'indianred'},
           line_kws={'linewidth':1, 'color':'blue'})
plt.show()

sns.lmplot('total_bill', 'tip', tips, order=4,
           scatter_kws={'marker':'o', 'color':'indianred'},
           line_kws={'linewidth':1, 'color':'blue'})
plt.show()

sns.lmplot('total_bill', 'tip', tips, fit_reg=False)
plt.show()

tips['tip_perc'] = 100*(tips['tip']/tips['total_bill'])
print(tips.head())

sns.lmplot('size', 'tip_perc', tips)
plt.show()

sns.lmplot('size', 'tip_perc', tips, x_jitter=0.1)
plt.show()

sns.lmplot('size', 'tip_perc', tips, x_estimator=np.mean)
plt.show()

sns.lmplot('total_bill', 'tip_perc', tips, hue='sex', markers=['x', 'o'])
plt.show()

sns.lmplot('total_bill', 'tip_perc', tips, hue='day')
plt.show()


