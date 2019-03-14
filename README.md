# YBS-Data
YBS Data is improved update-to-date version of official lastest YBS data release.

Data are gathered around Facebook/Groups/Pages that are related to YBS. Data validity is by best effort.

### ./data
- **routes.json** is in geojson format contains bus line information by ID, name, bus route as line shape and bus stop IDs in sequence. Bus stop IDs are equals to ID in stops.tsv.
- **stops.tsv** is in tsv format contains stop ID along with name, road, township.

### ./tools
- python scripts for importing/exporting to/from mongo