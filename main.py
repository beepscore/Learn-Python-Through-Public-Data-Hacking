#!/usr/bin/env python3

from bus import bus

url_string = 'http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22'
filename = 'data/output/rt22.xml'

bus.download_buses(url_string, filename)

# bus.find_buses(filename)
