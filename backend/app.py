#!flask/bin/python
from flask import Flask, jsonify
from flask_cors import CORS, cross_origin

import requests
import urllib2
import sqlite3
import os

from location import IpInfo, Geolocation


app = Flask(__name__)
cors = CORS(app)  # allow all traffic
# connect to the SQLite database that the server connects to
path = os.path.abspath('../server/whereuat.sqlite3')
db = sqlite3.connect(path)  # needs to be an absolute path for connect() function
db.row_factory = sqlite3.Row

# ====================================================================================
# Endpoints
# ====================================================================================
@app.route('/location')
def get_locations():
    locationData = fetch_location()

    response = jsonify(locs = [l.serialize() for l in locationData])
    response.headers.add('Access-Control-Allow-Origin', '*')  # allow CORS
    return response

@app.route('/ip')
def get_ipdata():
    ipdata = fetch_ipinfo()

    response = jsonify(ips = [data.serialize() for data in ipdata])
    response.headers.add('Access-Control-Allow-Origin', '*')  # allow CORS
    return response
# ====================================================================================


# ====================================================================================
# helper functions
# ====================================================================================

# fetches location data from the database and returns a list of MyLocation objects
def fetch_ipinfo():
    info = []
    for row in db.execute('SELECT * FROM ipdata'):
        info.append(transpose_row_to_my_location(row))
    return info

def fetch_location():
    locs = []
    for row in db.execute('SELECT lat, lng FROM ipdata'):
        locs.append(transpose_row_to_geo(row))
    return locs

# takes a Row from a select query and returns a corresponding MyLocation object
def transpose_row_to_my_location(row):
    ip = row['ip']
    hostname = row['host']
    city = row['city']
    country = row['country']
    lat = row['lat']
    lng = row['lng']
    freq = row['freq']
    return IpInfo(ip=ip, 
                      hostname=hostname, 
                      city=city, 
                      country=country, 
                      latitude=lat, 
                      longitude=lng, 
                      freq=freq)

# takes a Row from a select query and returns a corresponding Geolocation object
def transpose_row_to_geo(row):
    lat = row['lat']
    lng = row['lng']
    return Geolocation(latitude=lat, longitude=lng)
# ====================================================================================


# ====================================================================================
# Start the backend Flask app
# ====================================================================================
try:
    app.run(debug=True)
except KeyboardInterrupt:
    # on keyboard interrupt, close our db connection
    db.close()
