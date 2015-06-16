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
