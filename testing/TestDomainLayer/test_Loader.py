import unittest
import requests
from DomainLayer.Loader import Loader


class TestLoader(unittest.TestCase):
    def test_scanBag(self):
        bagTagId = 1337
        bagTag = Loader().scanBagTag(bagTagId)

        self.assertEqual(bagTag['id'], bagTagId)
        self.assertEqual(bagTag['passengerId'], 4)
        self.assertEqual(bagTag['flightId'], 4)
        self.assertEqual(bagTag['weight'], 42)
        self.assertEqual(bagTag['classService'], 'Business Class')

    def test_getAllBagsInAirlineLoadingArea(self):
        bags = Loader().getAllBagsInAirlineLoadingArea('B')
        self.assertNotEqual(len(bags), 0)


if __name__ == '__main__':
    unittest.main()
