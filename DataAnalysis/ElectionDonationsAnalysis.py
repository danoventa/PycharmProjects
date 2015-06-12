from __future__ import division

import pandas as pd
from pandas import Series, DataFrame
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')


donor_df = pd.read_csv('Election_Donor_Data.csv', low_memory=False)
print(donor_df.info())