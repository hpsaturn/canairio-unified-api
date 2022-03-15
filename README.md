# CanAirIO Unified API

Initial API version for mobile and fixed CanAirIO stations

## Overview

We have a JSON API for the CanAirIO fixed stations, for now it only has two endpoints, the first one for get all current stations that are online right now with the last publication, `stations` and the second one for retrieve the complete data of each station in the last hour. The output is a [DarwinCore](https://dwc.tdwg.org/terms/) record.

## Stations list

endpoint: [http://api.canair.io:8080/dwc/stations](http://api.canair.io:8080/dwc/stations)

Sample request for retreive all stations:

```bash
curl -G http://api.canair.io:8080/dwc/stations
```

Sample output of one station only:

```json
[{
	"id": "EZTTTGOTD78432",
	"station_name": "EZTTTGOTD78432",
	"scientificName": "CanAirIO Air quality Station",
	"ownerInstitutionCodeProperty": "CanAirIO",
	"type": "FixedStation",
	"license": "CC BY-NC-SA",
	"measurements": [
		[{
			"measurementID": "2022-03-15T16:29:07.913361Z",
			"measurementType": "PM1",
			"measurementUnit": "ug/m3",
			"measurementDeterminedDate ": "2022-03-15T16:29:07.913361Z",
			"measurementDeterminedBy": "CanAirIO station EZTTTGOTD78432",
			"measurementValue": 10
		}, {
			"measurementID": "2022-03-15T16:29:07.913361Z",
			"measurementType": "PM2.5",
			"measurementUnit": "ug/m3",
			"measurementDeterminedDate ": "2022-03-15T16:29:07.913361Z",
			"measurementDeterminedBy": "CanAirIO station EZTTTGOTD78432",
			"measurementValue": 18
		}, {
			"measurementID": "2022-03-15T16:29:07.913361Z",
			"measurementType": "PM10",
			"measurementUnit": "ug/m3",
			"measurementDeterminedDate ": "2022-03-15T16:29:07.913361Z",
			"measurementDeterminedBy": "CanAirIO station EZTTTGOTD78432",
			"measurementValue": 27
		}, {
			"measurementID": "2022-03-15T16:29:07.913361Z",
			"measurementType": "Temperature",
			"measurementUnit": "C",
			"measurementDeterminedDate ": "2022-03-15T16:29:07.913361Z",
			"measurementDeterminedBy": "CanAirIO station EZTTTGOTD78432",
			"measurementValue": 24.1
		}, {
			"measurementID": "2022-03-15T16:29:07.913361Z",
			"measurementType": "Humidity",
			"measurementUnit": "%",
			"measurementDeterminedDate ": "2022-03-15T16:29:07.913361Z",
			"measurementDeterminedBy": "CanAirIO station EZTTTGOTD78432",
			"measurementValue": 36.6
		}, {
			"measurementID": "2022-03-15T16:29:07.913361Z",
			"measurementType": "Pressure",
			"measurementUnit": "hPa",
			"measurementDeterminedDate ": "2022-03-15T16:29:07.913361Z",
			"measurementDeterminedBy": "CanAirIO station EZTTTGOTD78432",
			"measurementValue": 0.0
		}, {
			"measurementID": "2022-03-15T16:29:07.913361Z",
			"measurementType": "CO2",
			"measurementUnit": "ppm",
			"measurementDeterminedDate ": "2022-03-15T16:29:07.913361Z",
			"measurementDeterminedBy": "CanAirIO station EZTTTGOTD78432",
			"measurementValue": 0
		}, {
			"measurementID": "2022-03-15T16:29:07.913361Z",
			"measurementType": "CO2 Temperature",
			"measurementUnit": "C",
			"measurementDeterminedDate ": "2022-03-15T16:29:07.913361Z",
			"measurementDeterminedBy": "CanAirIO station EZTTTGOTD78432",
			"measurementValue": 0.0
		}, {
			"measurementID": "2022-03-15T16:29:07.913361Z",
			"measurementType": "CO2 Humidity",
			"measurementUnit": "%",
			"measurementDeterminedDate ": "2022-03-15T16:29:07.913361Z",
			"measurementDeterminedBy": "CanAirIO station EZTTTGOTD78432",
			"measurementValue": 0.0
		}, {
			"measurementID": "2022-03-15T16:29:07.913361Z",
			"measurementType": "Battery voltage",
			"measurementUnit": "V",
			"measurementDeterminedDate ": "2022-03-15T16:29:07.913361Z",
			"measurementDeterminedBy": "CanAirIO station EZTTTGOTD78432",
			"measurementValue": 4.96
		}, {
			"measurementID": "2022-03-15T16:29:07.913361Z",
			"measurementType": "Geohash",
			"measurementUnit": "",
			"measurementDeterminedDate ": "2022-03-15T16:29:07.913361Z",
			"measurementDeterminedBy": "CanAirIO station EZTTTGOTD78432",
			"measurementValue": "ezty5zs"
		}, {
			"measurementID": "2022-03-15T16:29:07.913361Z",
			"measurementType": "Geohash3",
			"measurementUnit": "",
			"measurementDeterminedDate ": "2022-03-15T16:29:07.913361Z",
			"measurementDeterminedBy": "CanAirIO station EZTTTGOTD78432",
			"measurementValue": "ezt"
		}, {
			"measurementID": "2022-03-15T16:29:07.913361Z",
			"measurementType": "Version",
			"measurementUnit": "",
			"measurementDeterminedDate ": "2022-03-15T16:29:07.913361Z",
			"measurementDeterminedBy": "CanAirIO station EZTTTGOTD78432",
			"measurementValue": "v0.5.2r907"
		}]
	],
	"locationID": "2022-03-15T16:29:07.913361Z",
	"georeferencedBy": "CanAirIO firmware v0.5.2r907",
	"georeferencedDate": "2022-03-15T16:29:07.913361Z",
	"decimalLatitude ": 43.28,
	"decimalLongitude ": -2.99,
	"geohash": "ezty5zs",
	"observedOn": "2022-03-15T16:29:07.913361Z"
}]
```

## Station data

endpoint: [http://api.canair.io:8080/dwc/stations/station_id](http://api.canair.io:8080/dwc/stations/station_id)

Request sample for station with id: U33TTGOTDA585E:  

```bash
curl -G http://api.canair.io:8080/dwc/stations/U33TTGOTDA585E
```

Sample output for this station:

```json
{
	"id": "U33TTGOTDA585E",
	"station_name": "U33TTGOTDA585E",
	"scientificName": "CanAirIO Air quality Station",
	"ownerInstitutionCodeProperty": "CanAirIO",
	"type": "FixedStation",
	"license": "CC BY-NC-SA",
	"measurements": [
		[{
			"measurementID": "2022-03-15T16:45:34.835070Z",
			"measurementType": "PM1",
			"measurementUnit": "ug/m3",
			"measurementDeterminedDate ": "2022-03-15T16:45:34.835070Z",
			"measurementDeterminedBy": "CanAirIO station U33TTGOTDA585E",
			"measurementValue": 3
		}, {
			"measurementID": "2022-03-15T16:45:34.835070Z",
			"measurementType": "PM2.5",
			"measurementUnit": "ug/m3",
			"measurementDeterminedDate ": "2022-03-15T16:45:34.835070Z",
			"measurementDeterminedBy": "CanAirIO station U33TTGOTDA585E",
			"measurementValue": 5
		}, {
			"measurementID": "2022-03-15T16:45:34.835070Z",
			"measurementType": "PM10",
			"measurementUnit": "ug/m3",
			"measurementDeterminedDate ": "2022-03-15T16:45:34.835070Z",
			"measurementDeterminedBy": "CanAirIO station U33TTGOTDA585E",
			"measurementValue": 6
		}, {
			"measurementID": "2022-03-15T16:45:34.835070Z",
			"measurementType": "Temperature",
			"measurementUnit": "C",
			"measurementDeterminedDate ": "2022-03-15T16:45:34.835070Z",
			"measurementDeterminedBy": "CanAirIO station U33TTGOTDA585E",
			"measurementValue": 22.86
		}, {
			"measurementID": "2022-03-15T16:45:34.835070Z",
			"measurementType": "Humidity",
			"measurementUnit": "%",
			"measurementDeterminedDate ": "2022-03-15T16:45:34.835070Z",
			"measurementDeterminedBy": "CanAirIO station U33TTGOTDA585E",
			"measurementValue": 31.43
		}, {
			"measurementID": "2022-03-15T16:45:34.835070Z",
			"measurementType": "Pressure",
			"measurementUnit": "hPa",
			"measurementDeterminedDate ": "2022-03-15T16:45:34.835070Z",
			"measurementDeterminedBy": "CanAirIO station U33TTGOTDA585E",
			"measurementValue": 1019.78
		}, {
			"measurementID": "2022-03-15T16:45:34.835070Z",
			"measurementType": "CO2",
			"measurementUnit": "ppm",
			"measurementDeterminedDate ": "2022-03-15T16:45:34.835070Z",
			"measurementDeterminedBy": "CanAirIO station U33TTGOTDA585E",
			"measurementValue": 0
		}, {
			"measurementID": "2022-03-15T16:45:34.835070Z",
			"measurementType": "CO2 Temperature",
			"measurementUnit": "C",
			"measurementDeterminedDate ": "2022-03-15T16:45:34.835070Z",
			"measurementDeterminedBy": "CanAirIO station U33TTGOTDA585E",
			"measurementValue": 0.0
		}, {
			"measurementID": "2022-03-15T16:45:34.835070Z",
			"measurementType": "CO2 Humidity",
			"measurementUnit": "%",
			"measurementDeterminedDate ": "2022-03-15T16:45:34.835070Z",
			"measurementDeterminedBy": "CanAirIO station U33TTGOTDA585E",
			"measurementValue": 0.0
		}, {
			"measurementID": "2022-03-15T16:45:34.835070Z",
			"measurementType": "Battery voltage",
			"measurementUnit": "V",
			"measurementDeterminedDate ": "2022-03-15T16:45:34.835070Z",
			"measurementDeterminedBy": "CanAirIO station U33TTGOTDA585E",
			"measurementValue": 4.97
		}, {
			"measurementID": "2022-03-15T16:45:34.835070Z",
			"measurementType": "Geohash",
			"measurementUnit": "",
			"measurementDeterminedDate ": "2022-03-15T16:45:34.835070Z",
			"measurementDeterminedBy": "CanAirIO station U33TTGOTDA585E",
			"measurementValue": "u33dcu0"
		}, {
			"measurementID": "2022-03-15T16:45:34.835070Z",
			"measurementType": "Geohash3",
			"measurementUnit": "",
			"measurementDeterminedDate ": "2022-03-15T16:45:34.835070Z",
			"measurementDeterminedBy": "CanAirIO station U33TTGOTDA585E",
			"measurementValue": "u33"
		}, {
			"measurementID": "2022-03-15T16:45:34.835070Z",
			"measurementType": "Version",
			"measurementUnit": "",
			"measurementDeterminedDate ": "2022-03-15T16:45:34.835070Z",
			"measurementDeterminedBy": "CanAirIO station U33TTGOTDA585E",
			"measurementValue": "v0.5.3r908"
		}],
		[{
			"measurementID": "2022-03-15T16:47:34.767315Z",
			"measurementType": "PM1",
			"measurementUnit": "ug/m3",
			"measurementDeterminedDate ": "2022-03-15T16:47:34.767315Z",
			"measurementDeterminedBy": "CanAirIO station U33TTGOTDA585E",
			"measurementValue": 4
		}, {
			"measurementID": "2022-03-15T16:47:34.767315Z",
			"measurementType": "PM2.5",
			"measurementUnit": "ug/m3",
			"measurementDeterminedDate ": "2022-03-15T16:47:34.767315Z",
			"measurementDeterminedBy": "CanAirIO station U33TTGOTDA585E",
			"measurementValue": 5
		}, {
			"measurementID": "2022-03-15T16:47:34.767315Z",
			"measurementType": "PM10",
			"measurementUnit": "ug/m3",
			"measurementDeterminedDate ": "2022-03-15T16:47:34.767315Z",
			"measurementDeterminedBy": "CanAirIO station U33TTGOTDA585E",
			"measurementValue": 6
		}, {
			"measurementID": "2022-03-15T16:47:34.767315Z",
			"measurementType": "Temperature",
			"measurementUnit": "C",
			"measurementDeterminedDate ": "2022-03-15T16:47:34.767315Z",
			"measurementDeterminedBy": "CanAirIO station U33TTGOTDA585E",
			"measurementValue": 22.85
		}, {
			"measurementID": "2022-03-15T16:47:34.767315Z",
			"measurementType": "Humidity",
			"measurementUnit": "%",
			"measurementDeterminedDate ": "2022-03-15T16:47:34.767315Z",
			"measurementDeterminedBy": "CanAirIO station U33TTGOTDA585E",
			"measurementValue": 30.87
		}, {
			"measurementID": "2022-03-15T16:47:34.767315Z",
			"measurementType": "Pressure",
			"measurementUnit": "hPa",
			"measurementDeterminedDate ": "2022-03-15T16:47:34.767315Z",
			"measurementDeterminedBy": "CanAirIO station U33TTGOTDA585E",
			"measurementValue": 1019.79
		}, {
			"measurementID": "2022-03-15T16:47:34.767315Z",
			"measurementType": "CO2",
			"measurementUnit": "ppm",
			"measurementDeterminedDate ": "2022-03-15T16:47:34.767315Z",
			"measurementDeterminedBy": "CanAirIO station U33TTGOTDA585E",
			"measurementValue": 0
		}, {
			"measurementID": "2022-03-15T16:47:34.767315Z",
			"measurementType": "CO2 Temperature",
			"measurementUnit": "C",
			"measurementDeterminedDate ": "2022-03-15T16:47:34.767315Z",
			"measurementDeterminedBy": "CanAirIO station U33TTGOTDA585E",
			"measurementValue": 0.0
		}, {
			"measurementID": "2022-03-15T16:47:34.767315Z",
			"measurementType": "CO2 Humidity",
			"measurementUnit": "%",
			"measurementDeterminedDate ": "2022-03-15T16:47:34.767315Z",
			"measurementDeterminedBy": "CanAirIO station U33TTGOTDA585E",
			"measurementValue": 0.0
		}, {
			"measurementID": "2022-03-15T16:47:34.767315Z",
			"measurementType": "Battery voltage",
			"measurementUnit": "V",
			"measurementDeterminedDate ": "2022-03-15T16:47:34.767315Z",
			"measurementDeterminedBy": "CanAirIO station U33TTGOTDA585E",
			"measurementValue": 4.96
		}, {
			"measurementID": "2022-03-15T16:47:34.767315Z",
			"measurementType": "Geohash",
			"measurementUnit": "",
			"measurementDeterminedDate ": "2022-03-15T16:47:34.767315Z",
			"measurementDeterminedBy": "CanAirIO station U33TTGOTDA585E",
			"measurementValue": "u33dcu0"
		}, {
			"measurementID": "2022-03-15T16:47:34.767315Z",
			"measurementType": "Geohash3",
			"measurementUnit": "",
			"measurementDeterminedDate ": "2022-03-15T16:47:34.767315Z",
			"measurementDeterminedBy": "CanAirIO station U33TTGOTDA585E",
			"measurementValue": "u33"
		}, {
			"measurementID": "2022-03-15T16:47:34.767315Z",
			"measurementType": "Version",
			"measurementUnit": "",
			"measurementDeterminedDate ": "2022-03-15T16:47:34.767315Z",
			"measurementDeterminedBy": "CanAirIO station U33TTGOTDA585E",
			"measurementValue": "v0.5.3r908"
		}]
	],
	"locationID": "2022-03-15T16:47:34.767315Z",
	"georeferencedBy": "CanAirIO firmware v0.5.3r908",
	"georeferencedDate": "2022-03-15T16:47:34.767315Z",
	"decimalLatitude ": 52.54,
	"decimalLongitude ": 13.44,
	"geohash": "u33dcu0",
	"observedOn": "2022-03-15T16:47:34.767315Z"
}
```

## Setup 

```bash
python3 -m venv .venv
cd .venv/ && source bin/activate
python -m pip install --upgrade setuptools
pip install -r requirements.txt
```
