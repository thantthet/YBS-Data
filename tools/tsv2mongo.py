#!/usr/bin/env python

import utils
import re
import json
import codecs
from pymongo import MongoClient
import glob

client = MongoClient(username='restheart', password='R3ste4rt!')

def import_stops():
	def normalize_stop(x):
		sid = int(x['id'])
		lat = float(x['lat'])
		lng = float(x['lng'])
		name_mm = x['name_mm']
		name_en = x['name_en']
		road_mm = x['road_mm']
		road_en = x['road_en']
		township_mm = x['township_mm']
		township_en = x['township_en']
		
		return {
			'id': sid,
			'location': {
				'type':'Point',
				'coordinates':[ lng, lat ]
			},
			'lat': lat,
			'lng': lng,
			'name_mm': name_mm,
			'name_en': name_en,
			'road_mm': road_mm,
			'road_en': road_en,
			'township_mm': township_mm,
			'township_en': township_en
		}

	stops = map(normalize_stop, utils.readTsv('../data/stops.tsv'))
	db = client.transit
	db.stops.drop()
	db.stops.insert_many(stops)

def import_routes():
	db = client.transit
	db.routes.drop()

	pattern = '../data/routes/*.json'
	for path in glob.glob(pattern):
		print('Reading from %s' % path)
		with codecs.open(path, 'r', encoding='utf-8') as file:
			route = json.loads(file.read())
			db.routes.insert(route)

import_stops()
import_routes()