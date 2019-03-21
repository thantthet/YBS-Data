# Yangon Bus Service – YBS Data
YBS Data is improved update-to-date version of officially released version.

Data are gathered around Facebook/Groups/Pages that are related to YBS. Data validity is by best effort.

### ./data
- **./routes/** are json files that contain bus line information by ID, name, bus route as line shape and bus stop IDs in sequence.
	-  Bus stop IDs are equals to ID in `stops.tsv`
	- `shape.geometry` is in geojson LineString format.
	- separated into respective json file for easier git versioning
- **stops.tsv** is in tsv format contains stop ID along with name, road, township.

### ./tools
- python scripts for importing/exporting to/from mongo

## Thanks
- Soe Moe - for helping with data updates
