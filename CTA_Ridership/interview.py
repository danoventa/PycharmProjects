import sqlite3 as db
import pandas as pd
import matplotlib

from geopy.distance import vincenty
from pandas import DataFrame, Series


con = db.connect("cta_ridership.db")
cur = con.cursor()

def query_to_df(query):
    df = pd.read_sql(query, con)
    return df

test3 = query_to_df('''Select stop_id, routes from Ridership;''')

def extract_route(blob):

    split_s = blob.split(',')
    return split_s


routes_count = {}
count = 0
for row in test3['routes']:
    routes = extract_route(row)
    count += 1
    for route in routes:
        if route not in routes_count:
            routes_count[route] = 1
        else:
            routes_count[route] += 1

test = Series(routes_count, name='DateValue')

o_test = test.order(ascending=False)
print(o_test)