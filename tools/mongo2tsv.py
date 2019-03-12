#!/usr/bin/env python

import utils
import re
import csv
from pymongo import MongoClient

def export_stops(db):
  coll = db.stops
  file = './../data/stops.txt'
  print 'Writing to %s' % file
  with open(file, 'wb') as stopsTxt:
    stops = []
    for stop in coll.find({}).sort('id'):
      props = {
        'id': stop['id'],
        'name_en': format(stop['name_en']),
        'name_mm': format(stop['name_mm']).encode('utf-8'),
        'road_en': format(stop['road_en']),
        'road_mm': format(stop['road_mm']).encode('utf-8'),
        'township_en': format(stop['township_en']),
        'township_mm': format(stop['township_mm']).encode('utf-8'),
        'lat': stop['lat'],
        'lng': stop['lng']
      }
      stops.append(props)
    with open('./../data/stops.tsv', 'wb') as file:
      dw = csv.DictWriter(file, sorted(stops[0].keys()), delimiter='\t')
      dw.writeheader()
      dw.writerows(stops)

client = MongoClient(username='restheart', password='R3ste4rt!')
db = client.transit
export_stops(db)