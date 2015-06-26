__author__ = 'Executor'

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')

from sklearn import linear_model
from sklearn.datasets import load_iris

iris = load_iris()

X = iris.data

Y = iris.target

print(iris.DESCR)

iris_data = DataFrame(X, columns=['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width'])
iris_target = DataFrame(Y, columns=['Species'])

def flower(num):
    if num == 0:
        return 'Setosa'
    elif num == 1:
        return 'Vericolour'
    else:
        return 'Virginica'

iris_target['Species'] = iris_target['Species'].apply(flower)
print(iris_target.tail())

iris = pd.concat([iris_data, iris_target], axis=1)

sns.pairplot(iris, hue='Species', size=2)
plt.show()

sns.factorplot('Petal Length', data=iris, hue='Species', size=10)
plt.show()

from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split

logreg = LogisticRegression()

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.4, random_state=3)

logreg.fit(X_train, Y_train)

from sklearn import metrics

Y_pred = logreg.predict(X_test)
print(metrics.accuracy_score(Y_test, Y_pred))

from sklearn.neighbors import KNeighborsClassifier

