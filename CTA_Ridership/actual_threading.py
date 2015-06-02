__author__ = 'Noventa'

import pandas as pd
import sqlite3 as db
import threading as th
import time

from geopy.distance import vincenty
from decimal import Decimal
from queue import Queue
from threading import Thread

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
loc = 'location'
max = Decimal(0.0)
visited = {}
x_p = -1
y_p = 0


''' max value object to be used with the threading.'''
class Max_Value(object):
    def __init__(self, max=0.0):
        self.lock = th.Lock()
        self.value = max
    def max_value(self, new_max):
        self.lock.acquire()
        try:
            self.value = new_max
        finally:
            self.lock.release()

'''calculate and use the thread safe object '''
def calculate_max(px, py, max_obj):
    distance = vincenty(px, py).miles.real
    if distance > max_obj.value:

        max_obj.max_value(new_max=distance)
        print(max_obj.value)

max = Max_Value()
start_time = time.time()
for row_x in test1[loc]:
    loc_x = extract_location(row_x)
    x_p += 1
    y_p = 0

    for row_y in test1[loc]:
        if  y_p > x_p:
            loc_y = extract_location(row_y)
            t = Thread(target=calculate_max, args=(loc_x, loc_y, max))
            t.start()
        y_p += 1

''' don't particularly understand this purpose.'''
main_thread = th.currentThread()
for t in th.enumerate():
    if t is not main_thread:
        t.join()

total_time = time.time().real - start_time.real
print("Total Time: " + total_time)
print("Max Value: " + max.max_value)