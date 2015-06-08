from __future__ import division
__author__ = 'Noventa'


import pandas as pd
from pandas import Series, DataFrame
import numpy
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')

import requests

url = 'http://elections.huffingtonpost.com/pollster/2012-general-election-romney-vs-obama.csv'
source = pd.read_csv(url)

print(source.info())