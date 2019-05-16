import unittest
import requests
from InfrastructureLayer.ClerkDao import ClerkDao


class TestClerkDao(unittest.TestCase):
    def test_placeBagIntoCB(self):
        response = ClerkDao().placeBagIntoCB(1337)
        self.assertEqual(
            response, 'BAG 1337 WAS PLACED INTO THE CONVEYOR BELT')


if __name__ == '__main__':
    unittest.main()
