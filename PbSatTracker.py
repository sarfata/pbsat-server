import ephem
import urllib2
import calendar
import math
import logging
import time

class PbSatTracker:
    def __init__(self):
        self.tles = None
        self.tles_timestamp = 0

    def load_tles_from_nasa(self):
        logging.info("Reloading TLEs")
        tle_source = urllib2.urlopen('http://www.amsat.org/amsat/ftp/keps/current/nasabare.txt')
        self.load_tles(tle_source)

    '''get_tles(): returns a hash of ephem.EarthSatellite objects.
    The source should support .readlines()'''
    def load_tles(self, source):
        # grab the latest keps
        lines = source.readlines()
        # strip off the header tokens and newlines
        lines = [item.strip() for item in lines]
        tles = {}
        # clean up the lines
        for i in xrange(0,len(lines)-2,3):
            tles[lines[i]] = ephem.readtle(lines[i], lines[i+1], lines[i+2])

        self.tles = tles

    def update_tles(self):
        # Only download tles once per hour
        if self.tles is None or self.tles_timestamp + 3600 < time.time():
            self.load_tles_from_nasa()
            self.tles_timestamp = time.time()

    def predict_next_pass(self, satellite, obs):
        tr, azr, tt, altt, ts, azs = obs.next_pass(satellite)

        # Caculate position every minute
        positions = []
        while tr < ts:
            obs.date = tr
            satellite.compute(obs)
            positions.append({
                'time': calendar.timegm(ts.tuple()),
                'azimuth': math.degrees(satellite.az),
                'altitude':  math.degrees(satellite.alt)
            })
            #print "%s %4.1f %5.1f" % (tr, math.degrees(iss.alt), math.degrees(iss.az))
            tr = ephem.Date(tr + 60.0 * ephem.second)

        return {
            'rise': {
                'time': calendar.timegm(tr.tuple()),
                'azimuth': math.degrees(azr)
                },
            'transit': {
                'time': calendar.timegm(tt.tuple()),
                'altitude': math.degrees(altt)
            },
            'set': {
                'time': calendar.timegm(ts.tuple()),
                'azimuth': math.degrees(azs)
            },
            'positions': positions
        }

    def tracking_info(self, objectId, latitude, longitude):
        obs = ephem.Observer()
        obs.lat = latitude
        obs.long = longitude
        obs.date = ephem.now()

        return {
            'observer': {
                'datetime': calendar.timegm(obs.date.tuple()),
                'latitude': obs.lat,
                'longitude': obs.long
            },
            'object': objectId,
            'tles_age': int(time.time() - self.tles_timestamp),
            'pass': [ self.predict_next_pass(self.tles[objectId], obs) ]
        }

