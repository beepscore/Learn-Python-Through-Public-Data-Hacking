#!/usr/bin/env python3

import unittest
from potholes import potholes


class TestPotholes(unittest.TestCase):

    # street_address_trimmed

    def test_street_address_trimmed(self):
        self.assertEqual(potholes.street_address_trimmed('438 W. Belvedere'), 4)
        self.assertEqual(potholes.street_address_trimmed('9856 Fooby Way'), 98)


if __name__ == "__main__":
    u
