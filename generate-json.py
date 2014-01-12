#!/usr/bin/python

import sys
import math
import ephem
import json
import calendar, time
import urllib2




def get_tles(source):
 '''get_tles(): returns a hash of ephem.EarthSatellite objects.
 The source should support .readlines()'''

 # grab the latest keps
 lines = source.readlines()

 # strip off the header tokens and newlines
 lines = [item.strip() for item in lines]

 tles = {}
 # clean up the lines
 for i in xrange(0,len(lines)-2,3):
  tles[lines[i]] = ephem.readtle(lines[i], lines[i+1], lines[i+2])

 return tles

def get_passes(satellite, obs):
  passes = []

  tr, azr, tt, altt, ts, azs = obs.next_pass(satellite)

  print "Next pass time: {}".format(tr)
  passes.append({
    'rise': {
      'time': calendar.timegm(tr.tuple()),
      'azimuth': azr
    },
    'transit': {
      'time': calendar.timegm(tt.tuple()),
      'altitude': altt
    },
    'set': {
      'time': calendar.timegm(ts.tuple()),
      'azimuth': azs
    }
  })

  obs.date = tr + ephem.minute

  return passes

if __name__ == '__main__':
  tle_source = urllib2.urlopen('http://www.amsat.org/amsat/ftp/keps/current/nasabare.txt')
  tles = get_tles(tle_source)

  obs = ephem.Observer()
  obs.lat = '38.6652'
  obs.long = '-121.125'
  obs.date = ephem.now()
  print json.dumps({
    'observer': {
      'datetime': calendar.timegm(obs.date.tuple()),
      'latitude': math.degrees(obs.lat),
      'longitude': math.degrees(obs.long)
    },
    'passes': {
      'ISS': get_passes(tles['ISS'], obs)
    }
  })

