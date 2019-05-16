import unittest
import requests
from DomainLayer.Clerk import Clerk


class TestClerk(unittest.TestCase):
    def test_placeBagIntoCB(self):
        response = Clerk().placeBagIntoCB(1337)
        self.assertEqual(
            response, 'BAG 1337 WAS PLACED INTO THE CONVEYOR BELT')


if __name__ == '__main__':
    unittest.main()
