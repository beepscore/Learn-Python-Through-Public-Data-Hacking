#!/usr/bin/env python3

import urllib.request

# xml library is vulnerable to attacks (xml 'bombs') such as billion laughs
# use defusedxml instead
# https://pypi.python.org/pypi/defusedxml/
# http://stackoverflow.com/questions/38454978/tastypie-usage-of-the-xml-aspects-requires-lxml-and-defusedxml
# from xml.etree.ElementTree import parse
from defusedxml.ElementTree import parse

import webbrowser

url_string = 'http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22'
filename = 'data/output/rt22.xml'


def download_buses(url_string, outfilename):
    u = urllib.request.urlopen(url_string)
    data = u.read()

    f = open(outfilename, 'wb')
    f.write(data)
    f.close()


def bus_id(bus):
    """ given bus xml, returns id as text"""

    id_text = bus.find('id').text
    return id_text


def bus_is_northbound(bus):
    """ given bus xml, returns True if bus is Northbound"""

    dd = bus.find('dd').text
    return  dd is 'Northbound'


def bus_latitude(bus):
    """ given bus xml, returns latitude"""

    latitude = float(bus.find('lat').text)
    return latitude


def bus_longitude(bus):
    """ given bus xml, returns longitude"""

    longitude = float(bus.find('lon').text)
    return longitude


def find_buses(filename):
    """ finds buses meeting criteria """

    # parse xml into a document tree
    doc = parse(filename)

    # find all bus elements
    buses = doc.findall('bus')

    # https://developers.google.com/maps/documentation/staticmaps/
    # http://maps.googleapis.com/maps/api/staticmap?size=500x500&sensor=false&markers=41.98062,-87.668452
    map_url_start = 'http://maps.googleapis.com/maps/api/staticmap?size=500x500&sensor=false'

    # TODO: change to tuple?
    daves_latitude = 41.98062
    daves_longitude = -87.668452

    for bus in buses:
        latitude = bus_latitude(bus)
        longitude = bus_longitude(bus)

        if latitude >= daves_latitude:
            # bus id 4068 41.99755483598852
            print('bus id', bus_id(bus), latitude)

            # f requires python >= 3.6
            markers = f"&markers={latitude}, {longitude}"
            webbrowser.open(map_url_start + markers)

