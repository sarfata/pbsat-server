#!/usr/bin/python

import json

from PbSatTracker import PbSatTracker

if __name__ == '__main__':

    tracker = PbSatTracker()
    tracker.load_tles_from_nasa()
    p = tracker.tracking_info('ISS', 38.6652, -121.125)

    print json.dumps(p)
