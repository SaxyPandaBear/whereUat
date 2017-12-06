#!flask/bin/python
from flask import Flask, Response, jsonify
from flask_cors import CORS, cross_origin

import requests
import urllib2
import sqlite3


class MyLocation():
    def __init__(self, **kwargs):
        self.latitude = kwargs.get('latitude')
        self.longitude = kwargs.get('longitude')

    def __str__(self):
        return '( %s,%s )' % (self.latitude, self.longitude)

    def __repr__(self):
        return self.__str__()

    def serialize(self):
        return {
            'latitude': self.latitude,
            'longitude': self.longitude
        }

app = Flask(__name__)

cors = CORS(app)

@app.route('/')
def get_locations():
    return read_locations()

# read geolocation data from the file, and returns a
# list of MyLocation objects created from data in the file
def read_locations():
    my_locs = []
    # note: this expects the file server to be up in order to read from the file.
    try:
        for line in urllib2.urlopen('http://108.44.193.253:12000/IP.txt'):  # hard-coded address
            if line.find(',') > -1:  # try to account for empty lines
                geo = line.split(",")
                my_locs.append(MyLocation(latitude=float(geo[0]), longitude=float(geo[1])))
    except URLError:
        # if the file server is not responsive, or anything else goes wrong, 
        # use text file in this directory, "IP.txt"
        my_locs = []  # start with a fresh list
        with open("IP.txt") as f:
            for line in f.read().splitlines():
                if line.find(",") > -1:
                    geo = line.split(",")
                    my_locs.append(MyLocation(latitude=float(geo[0]), longitude=float(geo[1])))

    # return Response(json.dumps(locs), mimetype='application/json')
    response = jsonify(locs = [l.serialize() for l in my_locs])
    response.headers.add('Access-Control-Allow-Origin', '*')  # allow CORS
    return response

if __name__ == '__main__':
    app.run(debug=True)
