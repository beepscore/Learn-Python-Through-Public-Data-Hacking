#!/usr/bin/env python3

import unittest
from potholes import potholes


class TestPotholes(unittest.TestCase):

    def test_street_block(self):
        self.assertEqual(potholes.street_block('438 W. Belvedere'), 400)
        self.assertEqual(potholes.street_block('9856 Fooby Way'), 9800)
        # file line 129810
        self.assertEqual(potholes.street_block('1 E MONROE ST'), 0)

    def test_street_address_tail(self):
        self.assertEqual(potholes.street_address_tail('438 W. Belvedere'), 'W. Belvedere')
        self.assertEqual(potholes.street_address_tail('9856 Fooby Way'), 'Fooby Way')

    def test_street_block_address(self):
        self.assertEqual(potholes.street_block_address('419 W. Belvedere'), '400 W. Belvedere')

    def test_potholes_sorted(self):
        holes = potholes.potholes_sorted('data/input/potholes.csv')
        # http://stackoverflow.com/questions/30250715/how-do-you-get-the-first-3-elements-in-python-ordereddict#30250803
        self.assertEqual(list(holes.items())[0], ('6400 S ASHLAND AVE', 3280))
        self.assertEqual(list(holes.items())[1], ('4900 S ASHLAND AVE', 2491))
        self.assertEqual(list(holes.items())[2], ('4800 S ASHLAND AVE', 2472))
        self.assertEqual(list(holes.items())[3], ('7100 W ARCHER AVE', 2342))
        self.assertEqual(list(holes.items())[4], ('4500 S ASHLAND AVE', 2273))
        self.assertEqual(list(holes.items())[5], ('8100 S MARYLAND AVE', 1911))

if __name__ == "__main__":
    unittest.main()

