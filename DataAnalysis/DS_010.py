__author__ = 'Noventa'

import numpy as np
import pandas as pd
from numpy.random import randn

from scipy import stats

import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

dataset1 = randn(100)
dataset2 = randn(80)

plt.hist(dataset1)
plt.show()
plt.hist(dataset2, color='indianred')
plt.show()
plt.hist(dataset1, normed=True, color='indianred', alpha=0.5, bins=20)
plt.hist(dataset2, normed=True, alpha=0.5, bins=20)
plt.show()
data1 = randn(1000)
data2 = randn(1000)

sns.jointplot(data1, data2, kind='hex')
plt.show()