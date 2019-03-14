#!/usr/bin/env python

import utils
import re
import csv
import json
import codecs

def convert_stops():
  def jsonlize(x):
    x['id'] = int(x['id'])
    x['lat'] = float(x['lat'])
    x['lng'] = float(x['lng'])
    return x
  tsv_path = './../data/stops.txt'
  json_path = './../data/stops.json'
  print 'Reading from %s' % tsv_path
  rows = utils.readTsv(tsv_path)
  with open(json_path, 'wb') as json_file:
    print 'Writing to %s' % json_path
    json_file.write(json.dumps(map(jsonlize, rows)))

convert_stops()