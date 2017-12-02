#!flask/bin/python
from flask import Flask, Response
import json

import requests
import urllib2


class MyLocation:
    def __init__(self, **kwargs):
        self.latitude = kwargs.get('latitude')
        self.longitude = kwargs.get('longitude')

    def __str__(self):
        return '( %s,%s )' % (self.latitude, self.longitude)

    def __repr__(self):
        return self.__str__()

app = Flask(__name__)

@app.route('/')
def get_locations():
    return read_locations()

# read geolocation data from the file, and returns a
# list of MyLocation objects created from data in the file
def read_locations():
    locs = []
    for line in urllib2.urlopen('http://108.44.193.253:12000/IP.txt'):
        geo = line.split(",")
        locs.append(MyLocation(latitude=geo[0], longitude=geo[1]))

    print str(locs)

    return Response(json.dumps(locs), mimetype='application/json')

if __name__ == '__main__':
    app.run(debug=True)
