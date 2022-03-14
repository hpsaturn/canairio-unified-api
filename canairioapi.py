from flask import Flask
from flask_restful import Resource, Api, reqparse
from influxdb import InfluxDBClient
from datetime import datetime
import io
import re
import os

app = Flask(__name__)
api = Api(app)

host="influxdb.canair.io"
dbname="canairio"
client = InfluxDBClient(host=host, port=8086, database=dbname)


def addStation(station):
  return { 'station': station }
  

class Stations(Resource):
  def get(self):
    data = []
    # client.query('select "pm25"::field,"U33TTGOTDA585E"::tag from "fixed_stations_01" where time >= now() - 1h')
    rs = client.query('select distinct("name") from (select "pm25","name" from fixed_stations_01 where time>now()-10m)')
    stations_names = [station['distinct'] for station in rs.get_points()]
    for station in stations_names:
      print(station)
      data.append(addStation(station))

    # result = client.query('select * from "fixed_stations_01" WHERE time >= now() - 10m')
    return data, 200  # return data and 200 OK code

api.add_resource(Stations, '/stations')

if __name__ == '__main__':
  app.run(host="0.0.0.0")
