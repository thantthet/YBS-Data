#!/usr/bin/env python

import utils
import re
import csv
import json
import codecs
from pymongo import MongoClient

def export_stops(db):
	file = './../data/stops.tsv'
	print('Writing to %s' % file)
	with open(file, 'wb') as file:
		stops = []
		for stop in db.stops.find({}).sort('id'):
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
			
		dw = csv.DictWriter(file, sorted(stops[0].keys()), delimiter='\t')
		dw.writeheader()
		dw.writerows(stops)

def export_routes(db):
	
	def remove_mongo_attrs(x):
		x.pop(u'_id', None)
		x.pop(u'_etag', None)
		x.pop(u'waypoints', None)
		x.pop(u'poi', None)
		x['shape'].pop(u'_id', None)
		return x

	routes = db.routes.find({}).sort('id')
	routes = map(remove_mongo_attrs, routes)

	for route in routes:
		file = ('./../data/routes/route%s.json' % route['route_id'])
		print('Writing to %s' % file)
		with codecs.open(file, 'wb', encoding='utf-8') as file:
			file.write(json.dumps(route, sort_keys=True, indent=2))

if __name__ == '__main__':
	client = MongoClient(username='restheart', password='R3ste4rt!')
	db = client.transit
	export_stops(db)
	export_routes(db)