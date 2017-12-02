#!flask/bin/python
from flask import Flask

class MyLocation:
    def __init__(self, **kwargs):
        self.latitude = kwargs.get('latitude')
        self.longitude = kwargs.get('longitude')

app = Flask(__name__)

@app.route('/')
def get_locations():
    return read_locations()

# read geolocation data from the file, and returns a
# list of MyLocation objects created from data in the file
def read_locations():
    with open('file', 'r') as file:
        locs = file.read().splitlines()
    return locs

if __name__ == '__main__':
    app.run(debug=True)

