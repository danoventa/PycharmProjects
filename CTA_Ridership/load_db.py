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

con = db.connect("cta_ridership.db")
cur = con.cursor()
cur.execute('''CREATE TABLE Ridership (stop_id INTEGER,
                                       alightings REAL,
                                       boardings REAL,
                                       location BLOB,
                                       cross_street TEXT,
                                       daytype TEXT,
                                       month_beginning TEXT,
                                       on_street TEXT,
                                       routes TEXT);''')

with open('CTA_Ridership.csv','rt') as f:
    dr = csv.DictReader(f)
    to_db = [(row[stop_id], row[alightings], row[boardings], row[location], row[cross_street], row[daytype], row[month_beginning], row[on_street], row[routes]) for row in dr]

cur.executemany('''INSERT INTO ridership (stop_id, alightings, boardings, location, cross_street, daytype, month_beginning, on_street, routes)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);''', to_db)

con.commit()