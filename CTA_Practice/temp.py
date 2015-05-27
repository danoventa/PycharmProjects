__author__ = 'Noventa'

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



for str in cols:
    for data in res[cols]:
        cur.execute('''insert into Boardings ({}) values({});'''.format(str, data))

con.commit()