#!/usr/bin/env python3

# pothole data
# https://data.cityofchicago.org/Service-Requests/311-Service-Requests-Pot-Holes-Reported/7as2-ds3y
# download as .csv file, original name 311_Service_Requests_-_Pot_Holes_Reported.csv
# rename file and put in data/input/potholes.csv
# 106 Mb
# fields
# CREATION DATE,STATUS,COMPLETION DATE,SERVICE REQUEST NUMBER,TYPE OF SERVICE REQUEST,CURRENT ACTIVITY,MOST RECENT ACTION,NUMBER OF POTHOLES FILLED ON BLOCK,STREET ADDRESS,ZIP,X COORDINATE,Y COORDINATE,Ward,Police District,Community Area,SSA,LATITUDE,LONGITUDE,LOCATION
# example rows
# 01/01/2011,Completed - Dup,01/03/2011,11-00002110,Pot Hole in Street,,,,7600 S PARNELL AVE,60620,1173863.13003072,1854505.80057442,17,6,69,,41.75607825280598,-87.63853957634103,"(41.75607825280598, -87.63853957634103)"
# 01/01/2011,Completed,01/03/2011,11-00002021,Pot Hole in Street,Dispatch Crew,Pothole Patched,5,1642 W 99TH ST,60643,1166945.42467286,1839061.36263023,19,22,72,,41.71403466751051,-87.66509581640723,"(41.71403466751051, -87.66509581640723)"

import csv

STREET_ADDRESS = 'STREET ADDRESS'
NUMBER_OF_POTHOLES_FILLED_ON_BLOCK = 'NUMBER OF POTHOLES FILLED ON BLOCK'

def street_block(street_address):
    """ returns a block e.g. '438 W Main' returns 400 """

    street_address_components = street_address.split()
    street_address0_int = int(street_address_components[0])
    # integer division. Alternatively could subtract modulo
    return (street_address0_int // 100) * 100


def street_address_tail(street_address):
    street_address_components = street_address.split()
    # discard component[0]
    tail_slice = street_address_components[1:]
    # Python uses join(list), not list.join() so join can be used on any iterable
    return ' '.join(tail_slice)


def street_block_address(street_address):
    street_address_components = street_address.split()
    return str(street_block(street_address)) + ' ' + street_address_tail(street_address)


def potholes_unsorted():
    f = open('data/input/potholes.csv')

    potholes = {}

    # DictReader reads csv into a dictionary, uses row 0 field names for keys
    for row in csv.DictReader(f):

        street_address = row[STREET_ADDRESS]
        # Python dictionary key can be a string or an int
        street_address_key = street_block_address(street_address)

        try:
            number_potholes_filled = row[NUMBER_OF_POTHOLES_FILLED_ON_BLOCK]
        except ValueError:
            number_potholes_filled = 0

        if potholes[street_address_key] is None:
            # not in dictionary, so add it
            potholes[street_address_key] = number_potholes_filled
        else:
            potholes[street_address_key] += number_potholes_filled

    return potholes


