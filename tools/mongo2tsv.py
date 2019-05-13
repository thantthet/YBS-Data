#!/usr/bin/env python


"""
	Script for exporting from mongodb to stops.tsv and routes{id}.tsv files
"""

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
				'id': 			stop['id'],
				'name_en': 		stop['name_en'],
				'name_mm': 		stop['name_mm'].encode('utf-8'),
				'road_en': 		stop['road_en'] if 'road_en' in stop else '',
				'road_mm': 		(stop['road_mm'] if 'road_mm' in stop else '').encode('utf-8'),
				'township_en': 	stop['township_en'],
				'township_mm': 	(stop['township_mm'] if 'township_mm' in stop else '').encode('utf-8'),
				'lat': 			stop['lat'],
				'lng': 			stop['lng']
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