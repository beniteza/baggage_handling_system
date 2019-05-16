import unittest
import requests
from InfrastructureLayer.LoaderDao import LoaderDao


class TestLoaderDao(unittest.TestCase):
    def test_scanBag(self):
        bagTagId = 1337
        bagTag = LoaderDao().scanBagTag(bagTagId)

        self.assertEqual(bagTag['id'], bagTagId)
        self.assertEqual(bagTag['passengerId'], 4)
        self.assertEqual(bagTag['flightId'], 4)
        self.assertEqual(bagTag['weight'], 42)
        self.assertEqual(bagTag['classService'], 'Business Class')

    def test_getAllBagsInAirlineLoadingArea(self):
        bags = LoaderDao().getAllBagsInAirlineLoadingArea('B')
        self.assertNotEqual(len(bags), 0)


if __name__ == '__main__':
    unittest.main()
