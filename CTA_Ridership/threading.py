import sqlite3 as db
import pandas as pd
import time
import seaborn as sns
import matplotlib
import numpy as np
import bokeh as bo
import bisect as bi
import bintrees as bt
import _thread

from matplotlib.pyplot import plot
from decimal import Decimal
from geopy.distance import vincenty
from pandas import DataFrame
from queue import Queue



con = db.connect("cta_ridership.db")
cur = con.cursor()

def query_to_df(query):
    df = pd.read_sql(query, con)
    return df

def extract_location(blob):
    strip_s = blob.strip('()')
    split_s = strip_s.split(', ')
    return split_s

test1 = query_to_df('''SELECT stop_id, location FROM Ridership;''')
print(test1)

test3 = query_to_df('''Select stop_id from Ridership;''')

loc = 'location'
max = Decimal(0.0)
visited = {}
x_pos = -1
y_pos = 0

def calculate_distance (x, y):
    distance = vincenty(x, y).miles.real
    return distance
complete_time = time.time()
start_time = time.time()
for row_x in test1[loc]:
    loc_x = extract_location(row_x)
    x_pos += 1
    y_pos = 0
    end_time = time.time()
    run_time = end_time.real - start_time.real
    start_time = time.time()
    print(run_time)

    for row_y in test1[loc]:
        if  y_pos > x_pos:
            loc_y = extract_location(row_y)
            distance = _thread.start_new_thread(calculate_distance, (loc_x, loc_y))
            if distance > max:
                max = distance
                print(max)
        y_pos += 1
total_time =  time.time().real - complete_time.real

print('total elapsed time: ', total_time)
print('max: ', max)



