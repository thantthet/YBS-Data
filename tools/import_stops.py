import csv
import sqlite3

db_path = './../data/ybs.db'
con = sqlite3.connect(db_path)
cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS stops;")
cur.execute("CREATE TABLE stops (id INTEGER NOT NULL PRIMARY KEY, lat Decimal(8,6) NOT NULL, lng Decimal(9,6) NOT NULL, name_en TEXT NOT NULL, name_mm TEXT NOT NULL, road_en TEXT NOT NULL, road_mm TEXT NOT NULL, township_en TEXT NOT NULL, township_mm TEXT NOT NULL);")
stops_tsv_path = './../data/stops.tsv'

with open(stops_tsv_path, 'r') as stops_file:
    reader = csv.reader(stops_file, delimiter="\t")
    next(reader)
    cur.executemany(
        "INSERT INTO stops (id, lat, lng, name_en, name_mm, road_en, road_mm, township_en, township_mm) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);",
        reader
    )
con.commit()
con.close()
