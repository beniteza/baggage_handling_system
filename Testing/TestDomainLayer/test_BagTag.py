import unittest
import requests
from DomainLayer.BagTag import BagTag


class TestBagTag(unittest.TestCase):
    def test_BagTagConstructor(self):
        passengerId = 88
        flightId = 88
        weight = 88
        classService = 'Economy Class'
        bagTag = BagTag(passengerId, flightId, weight, classService)
        self.assertEqual(bagTag.passengerId, passengerId)
        self.assertEqual(bagTag.flightId, flightId)
        self.assertEqual(bagTag.weight, weight)
        self.assertEqual(bagTag.classService, classService)


if __name__ == '__main__':
    unittest.main()
