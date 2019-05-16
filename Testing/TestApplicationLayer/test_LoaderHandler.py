import unittest
import requests


class TestLoaderHandler(unittest.TestCase):
    def test_scanBag(self):
        bagTagId = 19
        response = requests.post(
            "http://localhost:5000/scanBagTag", {"bagTagId": bagTagId})

        bagTag = response.json()

        self.assertEqual(bagTag['id'], bagTagId)
        self.assertEqual(bagTag['passengerId'], 4)
        self.assertEqual(bagTag['flightId'], 4)
        self.assertEqual(bagTag['weight'], 42)
        self.assertEqual(bagTag['classService'], 'Business Class')

    def test_getAllBagsInAirlineLoadingArea(self):
        response = requests.post(
            "http://localhost:5000/bagsInLoadingArea", {"airline": 'B'})
        bags = response.json()
        self.assertNotEqual(len(bags), 0)


if __name__ == '__main__':
    unittest.main()
