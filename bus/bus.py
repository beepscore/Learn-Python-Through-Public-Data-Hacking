#!/usr/bin/env python3

import urllib.request

# xml library is vulnerable to attacks (xml 'bombs') such as billion laughs
# use defusedxml instead
# https://pypi.python.org/pypi/defusedxml/
# from xml.etree.ElementTree import parse
from defusedxml.etree.ElementTree import parse

import webbrowser

url_string = 'http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22'
filename = 'data/output/rt22.xml'

def download_buses(url_string, outfilename):
    u = urllib.request.urlopen(url_string)
    data = u.read()

    f = open(outfilename, 'wb')
    f.write(data)
    # 4431
    f.close()

def find_buses(filename):
    # finds buses meeting criteria

    # parse xml into a document tree
    doc = parse(filename)

    # find all bus elements
    buses = doc.findall('bus')

    # documentation 'https://developers.google.com/maps/documentation/staticmaps/'
    map_url = 'https://developers.google.com/maps/documentation/staticmaps/'

    # TODO: change to tuple?
    daves_latitude = 41.98062
    daves_longitude = -87.668452

    for bus in buses:
        dd = bus.find('dd').text
        is_northbound = dd is 'Northbound'
        latitude = float(bus.find('lat').text)
        if latitude >= daves_latitude:
            # bus id 4068 41.99755483598852
            print('bus id', bus.find('id').text, latitude, 'dd', dd)
            webbrowser.open(map_url)
