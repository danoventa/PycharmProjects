__author__ = 'Noventa'



import matplotlib
matplotlib.use('TkAgg')
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
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

print(titanic_df['person'].value_counts())

fig = sns.FacetGrid(titanic_df, hue='Sex', aspect=4)
fig.map(sns.kdeplot, 'Age', shade=True)
oldest = titanic_df['Age'].max()
fig.set(xlim=(0, oldest))
fig.add_legend()
plt.show()


fig = sns.FacetGrid(titanic_df, hue='person', aspect=4)
fig.map(sns.kdeplot, 'Age', shade=True)
oldest = titanic_df['Age'].max()
fig.set(xlim=(0, oldest))
fig.add_legend()

plt.show()

fig = sns.FacetGrid(titanic_df, hue='Pclass', aspect=4)
fig.map(sns.kdeplot, 'Age', shade=True)
oldest = titanic_df['Age'].max()
fig.set(xlim=(0, oldest))
fig.add_legend()

plt.show()
