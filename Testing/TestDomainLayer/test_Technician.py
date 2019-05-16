import unittest
import requests
from DomainLayer.Technician import Technician


class TestTechnician(unittest.TestCase):
    def test_getJammedSignal(self):
        response = Technician().getJammedSignal()
        self.assertEqual(response, 'No Conveyor Belts are Jammed')

    def test_sendUnjammedSignal(self):
        response = Technician().sendUnjammedSignal()
        self.assertEqual(response, 'No Conveyor Belts are Jammed')


if __name__ == '__main__':
    unittest.main()
