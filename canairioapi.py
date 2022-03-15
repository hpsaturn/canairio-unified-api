from flask import Flask
from flask_restful import Resource, Api
from influxdb import InfluxDBClient
import pygeohash as pgh
from datetime import datetime
import os

app = Flask(__name__)
api = Api(app)

host = os.environ.get("CANAIRIO_INFLUX_HOST")
port = os.environ.get("CANAIRIO_INFLUX_PORT")
dbname = os.environ.get("CANAIRIO_INFLUX_DBNAME")

client = InfluxDBClient(host=host, port=port, database=dbname)

def getMeasure(field, ftype, fvalue, funit):
  """ Get a measure from a field
  :param field: complete field row data from influxdb
  :param ftype: field type name
  :param fvalue: field name on influxdb
  :param funit: field unit name or symbol
  """
  measure = {'measurementID': field['time']}
  measure['measurementType'] = ftype
  measure['measurementUnit'] = funit
  measure['measurementDeterminedDate '] = field['time'].format('YYYY-MM-DD HH:mm:ss')
  measure['measurementDeterminedBy'] = 'CanAirIO station {}'.format(field['name'])
  try:
    measure['measurementValue'] = field['{}'.format(fvalue)]
  except Exception as e:
    print(e)
    measure['measurementValue'] = 0
  return measure


def addStation(station, sdata):
  """ Add a station to API response
  :param station: station name
  :param sdata: all stations data
  :return: station json data
  """
  response = {'id': station}
  response['station_name'] = station
  response['scientificName'] = 'Air quality fixed station'
  response['ownerInstitutionCodeProperty'] = 'CanAirIO'
  response['type'] = 'PhysicalObject'
  response['license'] = 'CC BY-NC-SA'
  data = []
  fend = {}
  for s in sdata:
    if s['name'] == station:
      data.append(getMeasure(s, 'PM1', 'pm1', 'ug/m3'))
      data.append(getMeasure(s, 'PM2.5', 'pm25', 'ug/m3'))
      data.append(getMeasure(s, 'PM10', 'pm10', 'ug/m3'))
      data.append(getMeasure(s, 'Temperature', 'tmp', 'C'))
      data.append(getMeasure(s, 'Humidity', 'hum', '%'))
      data.append(getMeasure(s, 'Pressure', 'prs', 'hPa'))
      data.append(getMeasure(s, 'CO2', 'co2', 'ppm'))
      data.append(getMeasure(s, 'CO2 Temperature', 'co2tmp', 'C'))
      data.append(getMeasure(s, 'CO2 Humidity', 'co2hum', '%'))
      data.append(getMeasure(s, 'Battery voltage', 'vbat', 'V'))
      data.append(getMeasure(s, 'Geohash', 'geo', ''))
      data.append(getMeasure(s, 'Geohash3', 'geo3', ''))
      data.append(getMeasure(s, 'Version', 'rev', ''))
      fend = s
      break
  response['measurements'] = data
  response['observedOn'] = fend['time'].format('YYYY-MM-DD HH:mm:ss')
  coords = pgh.decode(fend['geo'])
  response['locationID'] = fend['time']
  response['decimalLatitude '] = coords[0]
  response['decimalLongitude '] = coords[1]
  response['georeferencedBy'] = 'CanAirIO firmware {}'.format(fend['rev'])
  response['georeferencedDate'] = fend['time'].format('YYYY-MM-DD HH:mm:ss')
  response['geohash'] = fend['geo']
  return response


class Stations(Resource):
  def get(self):
    response = []
    rs = client.query('select distinct("name") from (select "name" from fixed_stations_01 where time>now()-10m)')
    stations_names = [station['distinct'] for station in rs.get_points()]
    rs = client.query('select * from fixed_stations_01 where time>now()-10m')
    sdata = list(rs.get_points())
    for station in stations_names:
      response.append(addStation(station, sdata))
    return response, 200  # return data and 200 OK code


api.add_resource(Stations, '/stations')

if __name__ == '__main__':
  app.run(host="0.0.0.0")
