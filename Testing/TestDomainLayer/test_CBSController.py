import unittest
import requests
from DomainLayer.CBSController import CBSController


class TestCBSController(unittest.TestCase):
    def test_routeBags(self):
        response = CBSController().routeBags()
        self.assertEqual(response, 'No Bags In The System')

    def test_deactivateJammedBelt(self):
        response = CBSController().deactivateJammedBelt()
        self.assertEqual(response, 'No Jammed Belt to Deactivate')

    def test_activateBelt(self):
        response = CBSController().activateBelt()
        self.assertEqual(response, 'No Belt to Activate')


if __name__ == '__main__':
    unittest.main()
