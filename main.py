#!/usr/bin/env python3

from bus import bus
# from potholes import potholes

bus_url_string = 'http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22'
bus_filename = 'data/output/rt22.xml'


def show_buses():
    bus.download_buses(bus_url_string, bus_filename)
    buses = bus.find_buses(bus_filename)
    bus.map_buses(buses)

# show_buses()

# potholes
# for sample output see test_potholes.py
# holes = potholes.potholes_sorted('data/input/potholes.csv')
