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

df = sm.datasets.fair.load_pandas().data

print(df.head())

def affair_check(x):
    if x != 0:
        return 1
    else:
        return 0

df['Had_Affair'] = df['affairs'].apply(affair_check)

print(df.head())

df.groupby('Had_Affair').mean()

sns.factorplot('age', data=df, hue='Had_Affair', palette='coolwarm')


sns.factorplot('yrs_married', data=df, hue='Had_Affair', palette='coolwarm')

sns.factorplot('children', data=df, hue='Had_Affair', palette='coolwarm')

sns.factorplot('educ', data=df, hue='Had_Affair', palette='coolwarm')

sns.factorplot('religious', data=df, hue='Had_Affair', palette='coolwarm')

sns.factorplot('rate_marriage', data=df, hue='Had_Affair', palette='coolwarm')

sns.factorplot('occupation', data=df, hue='Had_Affair', palette='coolwarm')


sns.factorplot('affairs', data=df, hue='Had_Affair', palette='coolwarm')


sns.factorplot('occupation_husb', data=df, hue='Had_Affair', palette='coolwarm')
plt.show()

