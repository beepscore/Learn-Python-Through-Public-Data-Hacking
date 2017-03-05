#!/usr/bin/env python3

import unittest
from potholes import potholes


class TestPotholes(unittest.TestCase):

    # street_address_trimmed

    def test_street_block(self):
        self.assertEqual(potholes.street_block('438 W. Belvedere'), 400)
        self.assertEqual(potholes.street_block('9856 Fooby Way'), 9800)


    def test_street_address_tail(self):
        self.assertEqual(potholes.street_address_tail('438 W. Belvedere'), 'W. Belvedere')
        self.assertEqual(potholes.street_address_tail('9856 Fooby Way'), 'Fooby Way')


    def test_street_block_address(self):
        self.assertEqual(potholes.street_block_address('419 W. Belvedere'), '400 W. Belvedere')

if __name__ == "__main__":
    u
