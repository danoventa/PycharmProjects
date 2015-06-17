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

X = boston_df.RM

X = np.vstack(boston_df.RM)

print(X.shape)

Y = boston_df.Price

X = np.array([value, 1] for value in X)

m, b = np.linalg.lstsq(X, Y)[0]

plt.plot(boston_df.RM, boston_df.Price, 'o')

x = boston_df.RM

plt.plot(x, m*x + b, 'r', label='Best Fit Line')

plt.show()


result = np.linalg.lstsq(X, Y)

error_total = result[1]
rmse = np.sqrt(error_total/len(X))

print('The root mean square error was %.2f' %rmse)

import sklearn
from sklearn.linear_model import LinearRegression

lreg = LinearRegression()
''' Linear Regressions() is an estimator '''

X_multi = boston_df.drop('Price', 1)
Y_target = boston_df.Price

lreg.fit(X_multi, Y_target)
print('The estimated intercept coefficient is %.2f ' %lreg.intercept_)
print('the number of coefficients used was %d' %len(lreg.coef_))

coeff_df = DataFrame(boston_df.columns)
coeff_df.columns = ['Features']

coeff_df['Coefficient Estimate'] = pd.Series(lreg.coef_)
print(coeff_df)

X_train, X_test, Y_train, Y_test = sklearn.cross_validation.train_test_split(X, boston_df.Price)

print(X_train.shape, X_test.shape, Y_train.shape, Y_test.shape)

lreg = LinearRegression()
lreg.fit(X_train, Y_train)

pred_train = lreg.predict(X_train)
pred_test = lreg.predict(X_test)

print('fit a model Z_train, and calculate the MSE with Y_train: %.2f' %np.mean((Y_train-pred_train)**2))
print('fits a model X_train, and calculate MSE with X_test and Y_test: %.2f' %np.mean((Y_test-pred_test)**2))


train = plt.scatter(pred_train, (pred_train - Y_train), c='b', alpha=0.5)

test = plt.scatter(pred_test, (pred_test-Y_test), c='r', alpha=0.5)

plt.hlines(y=0, xmin=-10, xmax=10)

plt.legent((train, test), ('Training', 'Test'), loc='lower left')

plt.title('Residual Plots')

import statsmodels.api as sm
