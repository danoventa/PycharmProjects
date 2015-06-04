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
#plt.show()

def male_female_child(passenger):
    age, sex = passenger

    if age < 16:
        return 'child'
    else:
        return sex

titanic_df['person'] = titanic_df[['Age', 'Sex']].apply(male_female_child, axis=1)
print(titanic_df[0:10])
#sns.factorplot('Pclass', data=titanic_df, hue='person')
#print(titanic_df[0:10])
#plt.show()
#titanic_df['Age'].hist(bins=70)
#plt.show()
#print(titanic_df['Age'].mean())
#print(titanic_df['person'].value_counts())

#fig = sns.FacetGrid(titanic_df, hue='Sex', aspect=4)
#fig.map(sns.kdeplot, 'Age', shade=True)
#oldest = titanic_df['Age'].max()
#fig.set(xlim=(0, oldest))
#fig.add_legend()
#plt.show()


fig = sns.FacetGrid(titanic_df, hue='person', aspect=4)
fig.map(sns.kdeplot, 'Age', shade=True)
oldest = titanic_df['Age'].max()
fig.set(xlim=(0, oldest))
fig.add_legend()

#plt.show()

fig = sns.FacetGrid(titanic_df, hue='Pclass', aspect=4)
fig.map(sns.kdeplot, 'Age', shade=True)
oldest = titanic_df['Age'].max()
fig.set(xlim=(0, oldest))
fig.add_legend()

#plt.show()

deck = titanic_df['Cabin'].dropna()
print(deck.head())

levels = []
for level in deck:
    levels.append(level[0])

cabin_df = DataFrame(levels)

cabin_df.columns = ['Cabin']

sns.factorplot('Cabin', data=cabin_df, palette='winter_d')
#plt.show()

sns.factorplot('Cabin', data=cabin_df, palette='winter_d')

cabin_df = cabin_df[cabin_df.Cabin != 'T']
sns.factorplot('Cabin', data=cabin_df, palette='summer')
#plt.show()

sns.factorplot('Embarked', data=titanic_df, hue='Pclass', x_order=['C', 'Q', 'S'])
#plt.show()

print(titanic_df.head())
titanic_df['Alone'] = titanic_df.SibSp + titanic_df.Parch
print(titanic_df['Alone'])

titanic_df['Alone'].loc[titanic_df['Alone'] > 0] = 'With Family'
titanic_df['Alone'].loc[titanic_df['Alone'] == 0] = 'Alone'

print(titanic_df.head())
sns.factorplot('Alone', data=titanic_df, palette='Blues')
#plt.show()

titanic_df['Survivor'] = titanic_df.Survived.map({0: 'no', 1: 'yes'})
sns.factorplot('Survivor', data=titanic_df, palette='Set1')
plt.show()

sns.factorplot('Pclass', 'Survived', hue='person', data=titanic_df)
plt.show()

sns.lmplot('Age', 'Survived', data=titanic_df)
plt.show()

sns.lmplot('Age', 'Survived', hue='Pclass', data=titanic_df, palette='winter')
plt.show()

generations = [10, 20, 40, 60, 80]

sns.lmplot('Age', 'Survived', hue='Pclass', data=titanic_df, palette='winter', x_bins=generations)
plt.show()