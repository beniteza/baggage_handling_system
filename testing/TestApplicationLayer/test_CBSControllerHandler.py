import unittest
import requests


class TestCBSControllerHandler(unittest.TestCase):
    def test_routeBags(self):
        response = requests.post(
            "http://localhost:5000/routeBags")
        self.assertEqual(response.json(), 'No Bags In The System')

    def test_deactivateJammedBelt(self):
        response = requests.get(
            "http://localhost:5000/deactivateJammedBelt")
        self.assertEqual(response.json(), 'No Jammed Belt to Deactivate')

    def test_activateBelt(self):
        response = requests.get(
            "http://localhost:5000/activateBelt")
        self.assertEqual(response.json(), 'No Belt to Activate')


if __name__ == '__main__':
    unittest.main()
