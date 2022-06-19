import json
import sqlite3
import os

db_path = './../data/ybs.db'
con = sqlite3.connect(db_path)
cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS routes;")
cur.execute("DROP TABLE IF EXISTS coordinates;")
cur.execute("DROP TABLE IF EXISTS route_stops;")
cur.execute(
    "CREATE TABLE routes (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, route_id_name TEXT NOT NULL, color TEXT(6) NOT NULL, name TEXT NOT NULL);")
cur.execute(
    "CREATE TABLE coordinates (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,route_id BIGINT UNSIGNED NOT NULL, lat Decimal(8,6) NOT NULL, lng Decimal(9,6) NOT NULL, FOREIGN KEY (route_id) REFERENCES routes(id));")
cur.execute(
    "CREATE TABLE route_stops (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,route_id BIGINT UNSIGNED NOT NULL, stop_id BIGINT UNSIGNED NOT NULL, FOREIGN KEY (route_id) REFERENCES routes(id), FOREIGN KEY (stop_id) REFERENCES stops(id));")

route_directory = './../data/routes/'
for filename in os.listdir(route_directory):
    if filename.endswith(".json"):
        with open(route_directory + filename) as data_file:
            data = json.load(data_file)
            cur.execute(
                "INSERT INTO routes (route_id_name, color, name) VALUES (?, ?, ?);", (data['route_id'], data['color'], data['name']))
            route_id = cur.lastrowid
            cur.executemany(
                "INSERT INTO coordinates (route_id, lat, lng) VALUES (?, ?, ?);",
                [(route_id, coord[0], coord[1]) for coord in data['shape']['geometry']['coordinates']])
            cur.executemany(
                "INSERT INTO route_stops (route_id, stop_id) VALUES (?, ?);", [(route_id, shop_id) for shop_id in data['stops']])
con.commit()
con.close()
