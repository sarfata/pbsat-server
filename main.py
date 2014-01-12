""" Google App Engine top level script

Provides data for the Pebble Satellite tracker
"""

import os
import sys

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def hello(name=None):
  """ Return hello template at application root URL."""
  return "Hello World!"
