""" Google App Engine top level script

Provides data for the Pebble Satellite tracker
"""

import os
import sys
import json
import logging

from flask import Flask
from flask import request

from lib.PbSatTracker import PbSatTracker

app = Flask(__name__)

# Configure global logging for production and dev
logging.basicConfig(level=logging.DEBUG)

# Enable logging on heroku
from logging import StreamHandler
file_handler = StreamHandler()
app.logger.setLevel(logging.INFO)  # set the desired logging level here
app.logger.addHandler(file_handler)

@app.route('/')
def index():
    return "Please visit https://github.com/sarfata/pbsat-server for more info."

tracker = PbSatTracker()

@app.route('/<sat>')
def tracking_info(sat):
    latitude = float(request.args.get('latitude'))
    longitude = float(request.args.get('longitude'))

    if latitude is None or longitude is None:
        return json.dumps({ "error": "Invalid latitude / longitude" })

    try:
        tracker.update_tles()
    except Exception as e:
        return json.dumps({ "error": "Unable to load TLEs ({}).".format(e) })

    try:
        p = tracker.tracking_info(sat, latitude, longitude)
    except Exception as e:
        return json.dumps({ "error": "Unable to predict passes for {} at {}/{} ({}).".format(sat, latitude, longitude, e) })
    return json.dumps(p)

if __name__ == '__main__':
    app.debug = True
    app.run()
