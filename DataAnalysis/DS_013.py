__author__ = 'Noventa'

import numpy as np
from numpy.random import randn
import pandas as pd

from scipy import stats

import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

flights = sns.load_dataset('flights')
print(flights.head())

flights = flights.pivot('month', 'year', 'passengers')
print(flights)

''' Backend error on windows macOS with heat maps... so sad. Will try Bokeh
sns.heatmap(flights)
plt.show()
'''

import bokeh as bo
from bokeh.charts import HeatMap, output_file, show

output_file('heatmap.html')
p = HeatMap(flights, title='Flights')

show(p)
