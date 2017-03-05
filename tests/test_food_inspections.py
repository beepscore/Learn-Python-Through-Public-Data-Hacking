#!/usr/bin/env python3

import unittest
from food_inspections import food_inspections


class TestInspections(unittest.TestCase):

    def test_inspections_sorted(self):
        inspections = food_inspections.inspections_sorted('data/input/Food_Inspections.csv')
        # http://stackoverflow.com/questions/30250715/how-do-you-get-the-first-3-elements-in-python-ordereddict#30250803
        self.assertEqual(len(list(inspections.items())[0]), 2)

if __name__ == "__main__":
    unittest.main()

