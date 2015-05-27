import csv, sqlite3 as db

stop_id = 'stop_id'
alightings = 'alightings'
boardings = 'boardings'
location = 'location'
cross_street = 'cross_street'
daytype = 'daytype'
month_beginning = 'month_beginning'
on_street = 'on_street'
routes = 'routes'

con = db.connect("cta_boardings.db")
cur = con.cursor()
cur.execute('''CREATE TABLE boardings (stop_id INTEGER,
                                       alightings REAL,
                                       boardings REAL,
                                       location BLOB,
                                       cross_street TEXT,
                                       daytype TEXT,
                                       month_beginning TEXT,
                                       on_street TEXT,
                                       routes TEXT);''')

with open('CTA_Ridership.csv','rt') as fin:
    dr = csv.DictReader(fin)
    to_db = [(i[stop_id], i[alightings], i[boardings], i[location], i[cross_street], i[daytype], i[month_beginning], i[on_street], i[routes]) for i in dr]

cur.executemany('''INSERT INTO boardings (stop_id, alightings, boardings, location, cross_street, daytype, month_beginning, on_street, routes)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);''', to_db)

con.commit()