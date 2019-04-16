from InfrastructureLayer.DBconfig import DatabaseConfig
from flask_mysqldb import MySQL
import unittest
import requests

app = DatabaseConfig()
mysql = MySQL(app)


class TestAirlineLoadingAreaUserHandler(unittest.TestCase):
    def test_scanBag(self):
        bagTagId = 3
        response = requests.post(
            "http://localhost:5000/scanBagTag", {"bagTagId": bagTagId})

        bagTag = response.json()

        self.assertEqual(bagTag['id'], bagTagId)
        self.assertEqual(bagTag['passengerId'], 3)
        self.assertEqual(bagTag['flightId'], 54)
        self.assertEqual(bagTag['weight'], 234)
        self.assertEqual(bagTag['classService'], 'Business Class')


if __name__ == '__main__':
    unittest.main()
