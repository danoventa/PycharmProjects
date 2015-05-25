__author__ = 'Executor'
import pandas as pa
import numpy as np
from pandas import Series, DataFrame
import json
import requests
import urllib


''' read csv can take in a csv file from a host address.'''
''' Should look something like:
        url = " url "
        response = urllib.urlopen(url)
        data = json.loads(response.read())
        print(data)
'''


url = 'https://data.cityofchicago.org/resource/mq3i-nnqe.json'
response = requests.get(url)
response2 = pa.read_json(url)
data = json.loads(response.text)
dframe = DataFrame(response2)
dframe2 = DataFrame(data)
print(dframe)
print(dframe2)
print(dframe['stop_id'])

