__author__ = 'Executor'

import numpy as np
import pandas as pa
from pandas import Series, DataFrame


arr = np.array([[1, 2, np.nan], [np.nan, 3, 4]])
dframe1 = DataFrame(arr, index=['A', 'B'], columns=['One', 'Two', 'Three'])
print(dframe1.sum())
print(dframe1.sum(axis=1))
print(dframe1.min())
print(dframe1)
print(dframe1.idxmin())

print(dframe1)
print(dframe1.cumsum())

print(dframe1.describe())

from IPython.display import YouTubeVideo
YouTubeVideo('xGbpuFNR1ME')
YouTubeVideo('4EXNedimDMs')

