import unittest
import requests
from InfrastructureLayer.TechnicianDao import TechnicianDao


class TestTechnicianDao(unittest.TestCase):
    def test_getJammedSignal(self):
        response = TechnicianDao().getJammedSignal()
        self.assertEqual(response, 'No Conveyor Belts are Jammed')

    def test_sendUnjammedSignal(self):
        response = TechnicianDao().sendUnjammedSignal()
        self.assertEqual(response, 'No Conveyor Belts are Jammed')


if __name__ == '__main__':
    unittest.main()
