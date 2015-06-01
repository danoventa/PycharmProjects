__author__ = 'Noventa'

import pandas as pd
from pandas import Series, DataFrame
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import bokeh as bo
from bokeh.charts import show, output_file

titanic_df = pd.read_csv('train.csv')
#print(tit_d.head())

#tit_d.info()

sns.factorplot('Sex', data=titanic_df, hue='Pclass')
plt.show()

def male_female_child(passenger):
    age, sex = passenger

    if age < 16:
        return 'child'
    else:
        return sex

titanic_df['person'] = titanic_df[['Age', 'Sex']].apply(male_female_child, axis=1)
print(titanic_df[0:10])

sns.factorplot('Pclass', data=titanic_df, hue='person')

print(titanic_df[0:10])

plt.show()

titanic_df['Age'].hist(bins=70)
plt.show()

print(titanic_df['Age'].mean())