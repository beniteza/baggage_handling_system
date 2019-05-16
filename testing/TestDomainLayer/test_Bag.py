import unittest
import requests
from DomainLayer.Bag import Bag


class TestBag(unittest.TestCase):
    def test_BagConstructor(self):
        bagTagId = 1337
        bag = Bag(bagTagId)
        self.assertEqual(bag.bagTagId, bagTagId)
        self.assertEqual(bag.position, 'Check In Area')
        self.assertEqual(bag.isBeingRouted, False)


if __name__ == '__main__':
    unittest.main()
