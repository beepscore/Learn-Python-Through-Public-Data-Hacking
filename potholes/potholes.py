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
from collections import OrderedDict

STREET_ADDRESS = 'STREET ADDRESS'
NUMBER_OF_POTHOLES_FILLED_ON_BLOCK = 'NUMBER OF POTHOLES FILLED ON BLOCK'


def street_block(street_address):
    """ returns a block e.g. '438 W Main' returns 400 """

    # handle file line like 129812 (DictReader row 129810) field is empty ,,,,
    if street_address is None or street_address == '':
        return 0

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
    return str(street_block(street_address)) + ' ' + street_address_tail(street_address)


def number_potholes_filled(number_potholes_filled_string):
    if number_potholes_filled_string is None or number_potholes_filled_string == '':
        potholes_filled = 0
    else:
        # handle file line like 151744 (DictReader row 151742) number_potholes_filled_string '0.3'
        try:
            potholes_filled = int(number_potholes_filled_string)
        except ValueError:
            potholes_filled = 0
    return potholes_filled


def potholes_unsorted(filename):
    f = open(filename)

    potholes = {}
    row_number = 0

    # DictReader reads csv into a dictionary, uses row 0 field names for keys
    for row in csv.DictReader(f):

        # can print to help debug error due to messy input file
        print('row_number', row_number)

        street_address = row[STREET_ADDRESS]
        # Python dictionary key can be a string or an int
        if street_address is None:
            street_address = ''
        street_address_key = street_block_address(street_address)

        number_potholes_filled_string = row[NUMBER_OF_POTHOLES_FILLED_ON_BLOCK]
        potholes_filled = number_potholes_filled(number_potholes_filled_string)

        if street_address_key not in potholes:
            # not in dictionary, so add it
            potholes[street_address_key] = potholes_filled
        else:
            potholes[street_address_key] += potholes_filled

        row_number += 1

    f.close()
    return potholes


def potholes_sorted(filename):
    potholes = potholes_unsorted(filename)
    # convert dict potholes to SortedDict
    # sort by value, decreasing order
    # https://docs.python.org/3/library/collections.html#ordereddict-examples-and-recipes
    # http://stackoverflow.com/questions/613183/sort-a-python-dictionary-by-value (see comments)
    ordered = OrderedDict(sorted(potholes.items(), key=lambda t: t[1], reverse=True))
    return ordered
