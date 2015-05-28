__author__ = 'Executor'

import numpy as na
import pandas as pa
from pandas import Series, DataFrame

obj = Series([3, 6, 9, 2])
print(obj)
print(obj.index)

ww2 = Series([800, 400, 300, 200, 430], index=['USSR', 'Germany', 'China', 'Japan', 'USA'])
ww3 = Series([800, 400, 300, 200, 430, 500], index=['USSR', 'Germany', 'China', 'Japan', 'USA', 'Jamaica'])
print(ww2)

# check casualties
print(ww2[ww2>400])

print('USSR' in ww2)
ww2d  = ww2.to_dict()
print(ww2)
print(ww2d)

ww2.update(([300], index='Jamaica'))
print(ww2)

