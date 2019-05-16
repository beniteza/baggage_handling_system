import unittest
import requests


class TestTechnicianHandler(unittest.TestCase):
    def test_getJammedSignal(self):
        response = requests.get(
            "http://localhost:5000/getJammedSignal")
        self.assertEqual(response.json(), 'No Conveyor Belts are Jammed')

    def test_sendUnjammedSignal(self):
        response = requests.post(
            "http://localhost:5000/sendUnjammedSignal")
        self.assertEqual(response.json(), 'No Conveyor Belts are Jammed')


if __name__ == '__main__':
    unittest.main()
