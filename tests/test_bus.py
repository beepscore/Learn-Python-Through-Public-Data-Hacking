#!/usr/bin/env python3

import unittest
from bus import bus


class TestBus(unittest.TestCase):

    def test_find_buses(self):
        bus_filename = 'data/input/rt22_test.xml'
        buses = bus.find_buses(bus_filename)
        self.assertEqual(len(buses), 4)
        self.assertEqual(buses[0]['id'], '4386')
        self.assertEqual(buses[1]['latitude'], 41.99501180013021)
        self.assertEqual(buses[1]['longitude'], -87.67002522786458)
        self.assertEqual(buses[3]['direction'], 'Northbound')


if __name__ == "__main__":
    unittest.main()

