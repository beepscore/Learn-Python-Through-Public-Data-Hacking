#!/usr/bin/env python3

import unittest
from potholes import potholes


class TestPotholes(unittest.TestCase):

    def test_street_block(self):
        self.assertEqual(potholes.street_block('438 W. Belvedere'), 0)
        self.assertEqual(potholes.street_block('9856 Fooby Way'), 9000)
        self.assertEqual(potholes.street_block('12843 Bumpy Rd.'), 12000)
        self.assertEqual(potholes.street_block('1 E MONROE ST'), 0)

    def test_street_address_tail(self):
        self.assertEqual(potholes.street_address_tail('438 W. Belvedere'), 'W. Belvedere')
        self.assertEqual(potholes.street_address_tail('9856 Fooby Way'), 'Fooby Way')

    def test_street_block_address(self):
        self.assertEqual(potholes.street_block_address('419 W. Belvedere'), '0 W. Belvedere')

    def test_number_potholes_filled(self):
        # input file line 129812 (DictReader row 129810) has ,,,,
        self.assertEqual(potholes.number_potholes_filled(''), 0)
        # file line like 151744 (DictReader row 151742) number_potholes_filled_string '0.3'
        self.assertEqual(potholes.number_potholes_filled('0.3'), 0)

    def test_potholes_sorted(self):
        holes = potholes.potholes_sorted('data/input/potholes.csv')
        # http://stackoverflow.com/questions/30250715/how-do-you-get-the-first-3-elements-in-python-ordereddict#30250803
        self.assertEqual(list(holes.items())[0], ('4000 S ASHLAND AVE', 15154))
        self.assertEqual(list(holes.items())[1], ('6000 S ASHLAND AVE', 8659))
        self.assertEqual(list(holes.items())[2], ('5000 S ASHLAND AVE', 8106))
        self.assertEqual(list(holes.items())[3], ('3000 S ASHLAND AVE', 7551))
        self.assertEqual(list(holes.items())[4], ('11000 S DOTY AVE', 6904))
        self.assertEqual(list(holes.items())[5], ('7000 S STATE ST', 6844))

if __name__ == "__main__":
    unittest.main()

