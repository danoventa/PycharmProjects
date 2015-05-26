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
#plt.show()

sns.lmplot('total_bill', 'tip', tips,
           scatter_kws={'marker':'o', 'color':'indianred'},
           line_kws={'linewidth':1, 'color':'blue'})
#plt.show()

sns.lmplot('total_bill', 'tip', tips, order=4,
           scatter_kws={'marker':'o', 'color':'indianred'},
           line_kws={'linewidth':1, 'color':'blue'})
#plt.show()

sns.lmplot('total_bill', 'tip', tips, fit_reg=False)
#plt.show()

tips['tip_perc'] = 100*(tips['tip']/tips['total_bill'])
print(tips.head())

sns.lmplot('size', 'tip_perc', tips)
#plt.show()

sns.lmplot('size', 'tip_perc', tips, x_jitter=0.1)
#plt.show()

sns.lmplot('size', 'tip_perc', tips, x_estimator=np.mean)
#plt.show()

sns.lmplot('total_bill', 'tip_perc', tips, hue='sex', markers=['x', 'o'])
#plt.show()

sns.lmplot('total_bill', 'tip_perc', tips, hue='day')
#plt.show()


''' Does not work, something wrong with how the statsmodel is implemented in the API, or installed on my machine. .
    or it just doesn't work with python 3.4... I've installed it a few times, in a few different ways, still no
    dice! '''
#sns.lmplot('total_bill', 'tip_perc', tips, lowess=True, line_kws={'color':'black'})
#plt.show()

sns.regplot('total_bill', 'tip_perc', tips)
plt.show()

fig, (axis1, axis2) = plt.subplots(1, 2, sharey=True)
sns.regplot('total_bill', 'tip_perc', tips, ax=axis1)
sns.violinplot(tips['tip_perc'], tips['size'], color='Reds_r', ax=axis2)
plt.show()