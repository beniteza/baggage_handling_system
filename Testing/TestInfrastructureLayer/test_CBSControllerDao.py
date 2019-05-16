import unittest
import requests
from InfrastructureLayer.CBSControllerDao import CBSControllerDao


class TestCBSControllerDao(unittest.TestCase):
    def test_routeBags(self):
        response = CBSControllerDao().routeBags()
        self.assertEqual(response, 'No Bags In The System')

    def test_deactivateJammedBelt(self):
        response = CBSControllerDao().deactivateJammedBelt()
        self.assertEqual(response, 'No Jammed Belt to Deactivate')

    def test_activateBelt(self):
        response = CBSControllerDao().activateBelt()
        self.assertEqual(response, 'No Belt to Activate')


if __name__ == '__main__':
    unittest.main()
