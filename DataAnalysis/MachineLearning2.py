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
plt.show()

sns.factorplot('occupation_husb', data=df, hue='Had_Affair', palette='coolwarm')
plt.show()

occ_dummies = pd.get_dummies(df['occupation'])
hus_occ_dummies = pd.get_dummies(df['occupation_husb'])

print(occ_dummies.head())

occ_dummies.columns = ['occ1', 'occ2', 'occ3', 'occ4', 'occ5', 'occ6']
hus_occ_dummies.columns = ['hocc1', 'hocc2', 'hocc3', 'hocc4', 'hocc5', 'hocc6']

X = df.drop(['occupation', 'occupation_husb', 'Had_Affair'], axis=1)
dummies=pd.concat([occ_dummies, hus_occ_dummies], axis=1)
print(X.head())
print(dummies.head())

X = pd.concat([X, dummies], axis=1)
print(X.head())

Y = df.Had_Affair

print(Y.head())

X = X.drop('occ1', axis=1 )
X = X.drop('hocc1', axis=1 )

X = X.drop('affairs', axis=1)

print(X.head())

print(Y.head())

Y = np.ravel(Y)

print(Y)

log_model = LogisticRegression()

log_model.fit(X, Y)

log_model.score(X, Y)

Y.mean()

coeff_df = DataFrame(zip(X.columns, np.transpose(log_model.coef_)))

print(coeff_df)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y)

log_model2 = LogisticRegression()

log_model2.fit(X_train, Y_train)

class_predict = log_model2.predict(X_test)
print(metrics.accuracy_score(Y_test, class_predict))

