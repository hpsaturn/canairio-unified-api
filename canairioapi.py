from flask import Flask
from flask_restful import Resource, Api, abort, reqparse
from influxdb import InfluxDBClient
import pygeohash as pgh
import os

app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument('station_id')

host = os.environ.get("CANAIRIO_INFLUX_HOST")
port = os.environ.get("CANAIRIO_INFLUX_PORT")
dbname = os.environ.get("CANAIRIO_INFLUX_DBNAME")
ftable = os.environ.get("CANAIRIO_INFLUX_FIXED_STATIONS_TABLE")

client = InfluxDBClient(host=host, port=port, database=dbname)

def abort_if_todo_doesnt_exist(stations, station_id):
    if station_id not in stations:
        abort(404, message="Station id {} doesn't exist".format(station_id))

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

def getHeaderResponse(station, type='FixedStation'):
  """ Get header response
  :param station: station name id
  :return: header response
  """
  response = {'id': station}
  response['station_name'] = station
  response['scientificName'] = 'CanAirIO Air quality Station'
  response['ownerInstitutionCodeProperty'] = 'CanAirIO'
  response['type'] = type
  response['license'] = 'CC BY-NC-SA'
  return response 

def getLocationInfo(field, response={}):
  """ Get location info from field
  :param field: field row data from influxdb
  :return: location info response
  """
  coords = pgh.decode(field['geo'])
  response['locationID'] = field['time']
  response['georeferencedBy'] = 'CanAirIO firmware {}'.format(field['rev'])
  response['georeferencedDate'] = field['time'].format('YYYY-MM-DD HH:mm:ss')
  response['decimalLatitude '] = coords[0]
  response['decimalLongitude '] = coords[1]
  response['geohash'] = field['geo']
  return response

def getMeasurements(station, sdata, response={}, unique=True):
  response['measurements'] = []
  fend = {}
  for s in sdata:
    if s['name'] == station:
      data = []
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
      response['measurements'].append(data)
      fend = s
      if unique:
        break
  return fend

def addStation(station, sdata):
  """ Add a station to API response
  :param station: station name
  :param sdata: all stations data
  :return: station json data
  """
  response = getHeaderResponse(station) 
  fend = getMeasurements(station, sdata, response)
  getLocationInfo(fend, response)
  response['observedOn'] = fend['time'].format('YYYY-MM-DD HH:mm:ss')
  return response

class Station(Resource):
  def get(self, station_id):
    response = getHeaderResponse(station_id)
    rs = client.query('select distinct("name") from (select "name" from {} where time>now()-1h)'.format(ftable))
    stations = [station['distinct'] for station in rs.get_points()]
    abort_if_todo_doesnt_exist(stations, station_id)
    rs = client.query('select * from {} where "name"=\'{}\' AND (time >= now() - 1d)'.format(ftable, station_id))
    sdata = list(rs.get_points())
    fend = getMeasurements(station_id, sdata, response, False)
    getLocationInfo(fend, response)
    response['observedOn'] = fend['time'].format('YYYY-MM-DD HH:mm:ss')
    return response, 200 

class Stations(Resource):
  def get(self):
    response = []
    rs = client.query('select distinct("name") from (select "name" from {} where time>now()-10m)'.format(ftable))
    stations_names = [station['distinct'] for station in rs.get_points()]
    rs = client.query('select * from {} where time>now()-10m'.format(ftable))
    sdata = list(rs.get_points())
    for station in stations_names:
      response.append(addStation(station, sdata))
    return response, 200  # return data and 200 OK code


api.add_resource(Stations, '/stations', '/stations/', '/dwc/stations', '/dwc/stations/')
api.add_resource(Station, '/stations/<string:station_id>', '/dwc/stations/<string:station_id>')

if __name__ == '__main__':
  app.run(host="0.0.0.0")
