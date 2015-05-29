import sqlite3 as db
import pandas as pd
import time

from decimal import Decimal
from geopy.distance import vincenty



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
x_p = -1
y_p = 0

def calculate_distance (x, y):
    distance = vincenty(x, y).miles.real
    return distance

complete_time = time.time()
for row_x in test1[loc]:
    loc_x = extract_location(row_x)
    x_p += 1
    y_p = 0

    for row_y in test1[loc]:
        if  y_p > x_p:
            loc_y = extract_location(row_y)
            distance = vincenty(loc_x, loc_y).miles.real
            if distance > max:
                max = distance
        y_p += 1

total_time =  time.time().real - complete_time.real

print('total elapsed time: ', total_time)
print('max: ', max)



