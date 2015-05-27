__author__ = 'Noventa'

import sqlite3 as db
import bokeh as bo
import pandas as pd
import requests
import json

from pandas import Series, DataFrame
from sqlalchemy import create_engine

url = 'https://data.cityofchicago.org/resource/mq3i-nnqe.json'
response = requests.get(url)
text = response.text

res = pd.read_json(url)




print(res)
print(text)


con = db.connect('cta_boarding2.db')
cur = con.cursor()

stop_id = 'stop_id'
alightings = 'alightings'
boardings = 'boardings'
location = 'location'
cross_street = 'cross_street'
daytype = 'daytype'
month = 'month'
on_street = 'on_street'
routes = 'routes'

cols = [stop_id, alightings, boardings, location, cross_street, daytype, month, on_street, routes]

cur.execute('''CREATE TABLE boardings (stop_id INTEGER PRIMARY KEY,
                                       alightings REAL,
                                       boardings REAL,
                                       location BLOB,
                                       cross_street TEXT,
                                       daytype TEXT,
                                       month TEXT,
                                       on_street TEXT,
                                       routes TEXT);''')


''' stop_id is not recognized... '''
for str in cols:
    for data in res[cols]:
        cur.execute('''insert into boardings ({}) values({});'''.format(str, data))

con.commit()