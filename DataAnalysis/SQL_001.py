__author__ = 'Noventa'

import sqlite3
import pandas as pd

con = sqlite3.connect("sakila.db")
sql_query = '''SELECT * FROM customer '''

df = pd.read_sql(sql_query, con)
print(df)

def sql_to_df(sql_query):
    df = pd.read_sql(sql_query, con)

    return df

query = '''SELECT first_name, last_name FROM customer; '''
print(sql_to_df(query).head())



