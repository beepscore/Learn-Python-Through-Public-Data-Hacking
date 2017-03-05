#!/usr/bin/env python3

import urllib.request

# xml library is vulnerable to attacks (xml 'bombs') such as billion laughs
# use defusedxml instead
# https://pypi.python.org/pypi/defusedxml/
# http://stackoverflow.com/questions/38454978/tastypie-usage-of-the-xml-aspects-requires-lxml-and-defusedxml
# from xml.etree.ElementTree import parse
from defusedxml.ElementTree import parse

import webbrowser

ID_KEY = "id"
LATITUDE_KEY = "latitude"
LONGITUDE_KEY = "longitude"
DIRECTION_KEY = "direction"


def download_buses(url_string, outfilename):
    u = urllib.request.urlopen(url_string)
    data = u.read()

    f = open(outfilename, 'wb')
    f.write(data)
    f.close()


def bus_is_northbound(bus):
    """ given bus, returns True if bus is Northbound """

    return bus[DIRECTION_KEY] is 'Northbound'


def bus(bus_element):
    """ given a bus_element (an xml parsed element tree element), returns a bus dictionary """
    dict = {}
    dict[ID_KEY] = bus_element.find('id').text
    dict[LATITUDE_KEY] = float(bus_element.find('lat').text)
    dict[LONGITUDE_KEY] = float(bus_element.find('lon').text)
    dict[DIRECTION_KEY] = bus_element.find('dd').text
    return dict


def find_buses(filename):
    """ returns buses meeting criteria """

    # parse xml into a document tree
    doc = parse(filename)

    # find all bus elements
    bus_elements = doc.findall('bus')

    # TODO: change to tuple?
    daves_latitude = 41.98062
    daves_longitude = -87.668452

    selected_buses = []

    for bus_element in bus_elements:
        bus_from_element = bus(bus_element)

        if bus_from_element[LATITUDE_KEY] >= daves_latitude:
            # bus id 4068 41.99755483598852
            print(bus_from_element)
            selected_buses.append(bus_from_element)

    return selected_buses


def map_buses(buses):
    """ opens browser with map image showing bus location """

    # https://developers.google.com/maps/documentation/staticmaps/
    # http://maps.googleapis.com/maps/api/staticmap?size=500x500&sensor=false&markers=41.98062,-87.668452
    map_url_start = 'http://maps.googleapis.com/maps/api/staticmap?size=500x500&sensor=false'

    for bus in buses:
        # f requires python >= 3.6
        markers = f"&markers={bus[LATITUDE_KEY]}, {bus[LONGITUDE_KEY]}"
        webbrowser.open(map_url_start + markers)

