__author__ = 'Executor'

import numpy as np
import pandas as pa
from pandas import Series, DataFrame
import webbrowser

website = 'http://en.wikipedia.org/wiki/NFL_win-loss_records'

# webbrowser.open(website)
nfl_frame = pa.read_clipboard(error_bad_lines=False)

print(nfl_frame)
print(nfl_frame.columns)
print(nfl_frame['First Season'])

print(DataFrame(nfl_frame, columns=['Team', 'First Season', 'Total Games']))
print(DataFrame(nfl_frame, columns=['Team', 'First Season', 'Total Games', 'Stadium']))

print(nfl_frame.head(2))
print(nfl_frame.tail(2))

print(nfl_frame.ix[3])
nfl_frame['Stadium'] = "Levi's Stadium"
print(nfl_frame)

nfl_frame['Stadium'] = np.arange(6)
print(nfl_frame)

stads = Series(["Levs", "atnt"], index=[4, 0])
nfl_frame['Stadium'] = stads
print(nfl_frame)

data = {'City':['LA', 'IL', 'MA'], 'Pop':[800, 300, 494]}
city_frame = DataFrame(data)
print(city_frame)

