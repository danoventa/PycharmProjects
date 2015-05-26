__author__ = 'Noventa'

import pandas as pd
from pandas import Series, DataFrame
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import bokeh as bo
from bokeh.charts import show, output_file

tit_d = pd.read_csv('train.csv')
#print(tit_d.head())

#tit_d.info()

sns.factorplot('Sex', data=tit_d, hue='Pclass')
plt.show()

def male_female_child(passenger):
    age, sex = passenger

    if age < 16:
        return 'child'
    else:
        return sex

tit_d['person'] = tit_d[['Age', 'Sex']].apply(male_female_child, axis=1)
print(tit_d[0:10])

sns.factorplot('Pclass', data=tit_d, hue='person')

