# CanAirIO Unified API

Initial API version for mobile and fixed CanAirIO stations

## Overview

We have a JSON API for the CanAirIO fixed stations, for now it only has two endpoints, the first one for get all current stations that are online right now with the last publication, `stations` and the second one for retrieve the complete rawdata of each station.

## Stations list

endpoint: `http://api.canair.io:8080/stations`  

Sample request for retreive all stations:

```bash
curl -G http://api.canair.io:8080/stations
```

Sample output of one station only:

```json
[{
	"id": "D2GESP32DE15232",
	"station_name": "D2GESP32DE15232",
	"scientificName": "Air quality fixed station",
	"ownerInstitutionCodeProperty": "CanAirIO",
	"type": "PhysicalObject",
	"license": "CC BY-NC-SA",
	"measurements": [{
		"measurementID": "2022-03-15T14:19:42.960198Z",
		"measurementType": "PM1",
		"measurementUnit": "ug/m3",
		"measurementDeterminedDate ": "2022-03-15T14:19:42.960198Z",
		"measurementDeterminedBy": "CanAirIO station D2GESP32DE15232",
		"measurementValue": 10
	}],
	"locations": {
		"locationID": "2022-03-15T14:19:42.960198Z",
		"georeferencedBy": "CanAirIO firmware v0.5.2r907",
		"georeferencedDate": "2022-03-15T14:19:42.960198Z",
		"decimalLatitude ": 5.53,
		"decimalLongitude ": -73.61,
		"geohash": "d2gxmn3"
	},
	"observedOn": "2022-03-15T14:19:42.960198Z"
}]
```


## Station data

endpoint: `http://api.canair.io:8080/stations/station_id`  

Request sample for station with id: U33TTGOTDA585E:  

```bash
curl -G http://api.canair.io:8080/stations/U33TTGOTDA585E
```

Sample output for this station:

```json
{
	"id": "U33TTGOTDA585E",
	"station_name": "U33TTGOTDA585E",
	"scientificName": "Air quality fixed station",
	"ownerInstitutionCodeProperty": "CanAirIO",
	"type": "PhysicalObject",
	"license": "CC BY-NC-SA",
	"rawdata": [{
		"time": "2022-03-15T14:43:34.470417Z",
		"alt": -60.93,
		"bat": 100,
		"co2": 0,
		"co2hum": 0.0,
		"co2tmp": 0.0,
		"gas": 171.21,
		"geo": "u33dcu0",
		"geo3": "u33",
		"heap": 67396,
		"hum": 33.82,
		"mac": "24:6F:28:7A:58:5E",
		"name": "U33TTGOTDA585E",
		"name_1": "U33TTGOTDA585E",
		"pm1": 5,
		"pm10": 7,
		"pm25": 6,
		"prs": 1020.62,
		"rev": "v0.5.3r908",
		"rssi": -55,
		"tmp": 22.83,
		"vbat": 4.91
	}, {
		"time": "2022-03-15T14:47:34.683233Z",
		"alt": -60.6,
		"bat": 100,
		"co2": 0,
		"co2hum": 0.0,
		"co2tmp": 0.0,
		"gas": 171.38,
		"geo": "u33dcu0",
		"geo3": "u33",
		"heap": 67248,
		"hum": 34.0,
		"mac": "24:6F:28:7A:58:5E",
		"name": "U33TTGOTDA585E",
		"name_1": "U33TTGOTDA585E",
		"pm1": 5,
		"pm10": 7,
		"pm25": 6,
		"prs": 1020.56,
		"rev": "v0.5.3r908",
		"rssi": -57,
		"tmp": 22.83,
		"vbat": 4.89
	}],
	"locations": {
		"locationID": "2022-03-15T14:43:34.470417Z",
		"georeferencedBy": "CanAirIO firmware v0.5.3r908",
		"georeferencedDate": "2022-03-15T14:43:34.470417Z",
		"decimalLatitude ": 52.54,
		"decimalLongitude ": 13.44,
		"geohash": "u33dcu0"
	},
	"observedOn": "2022-03-15T14:43:34.470417Z"
}
```

## Setup 

```bash
python3 -m venv .venv
cd .venv/ && source bin/activate
python -m pip install --upgrade setuptools
pip install -r requirements.txt
```
