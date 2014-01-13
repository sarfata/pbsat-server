#!/usr/bin/python

import json
import datetime, time

from PbSatTracker import PbSatTracker

if __name__ == '__main__':

    tracker = PbSatTracker()
    tracker.update_tles()
    ##p = tracker.tracking_info('ISS', 38.6652, -121.125)
    p = tracker.tracking_info('ISS', 37.57,-122.31)
    print json.dumps(p)

    npt = p['pass'][0]['rise']['time']
    print ""
    print "Next pass time: {} - {} - {}".format(npt, time.strftime("%d %b %Y %H:%M:%S Local", time.localtime(npt)), time.strftime("%d %b %Y %H:%M:%S UTC", time.gmtime(npt)))
    print "Next pass is in {} hour with max altitude {}".format((npt - time.time()) / 3600, p['pass'][0]['transit']['altitude'])
