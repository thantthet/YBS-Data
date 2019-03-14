import csv
import re

def padZero(route_id):
	m = re.search(r'(\d+)', route_id) # take numbers from id
	if not m:
		return route_id
	if len(m.group(0)) == 1: # if numeric length is 1
		zero_pad = '0%s' % route_id
	else:
		zero_pad = route_id
	return zero_pad

def readCsv(file):
	with open(file) as tsvfile:
		reader = csv.DictReader(tsvfile, dialect='excel')
		for row in reader:
			yield {
				unicode(key, 'utf-8'): unicode(value, 'utf-8') for key, value in row.iteritems()
			}

def readTsv(file):
	with open(file) as tsvfile:
		reader = csv.DictReader(tsvfile, dialect='excel-tab')
		for row in reader:
			yield {
				unicode(key, 'utf-8'): unicode(value, 'utf-8') for key, value in row.iteritems()
			}