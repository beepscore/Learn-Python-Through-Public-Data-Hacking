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

def street_address_trimmed(street_address):
    address_number = int(street_address.split()[0])
    return address_number // 100

def populate_potholes():
    f = open('data/input/potholes.csv')
    # DictReader reads csv into a dictionary, uses row 0 field names for keys
    for row in csv.DictReader(f):

        street_address = row[STREET_ADDRESS]
        try:
            number_potholes_filled = row[NUMBER_OF_POTHOLES_FILLED_ON_BLOCK]
        except ValueError:
            number_potholes_filled = 0
