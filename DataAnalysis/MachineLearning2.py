__author__ = 'Executor'

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

import math
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')

from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split

from sklearn import metrics

import statsmodels.api as sm

def logistic(t):
    return 1.0/(1+math.exp((-1.0)*t))

t = np.linspace(-6, 6, 500)

y = np.array([logistic(ele) for ele in t])

plt.plot(t, y)
plt.title(' Logistic Function ')
plt.show()


