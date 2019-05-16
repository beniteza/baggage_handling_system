import unittest
import requests


class TestClerkHandler(unittest.TestCase):
    def test_checkInBag(self):
        requests.post(
            "http://localhost:5000/checkInBag", {"passengerId": '5', "flightId": '5', "weight": '55', "classService": 'Premium Economy Class'})

        response = requests.post("http://localhost:5000/test_checkInBag", {
                                 "passengerId": '5', "flightId": '5', "weight": '55', "classService": 'Premium Economy Class'})

        bag = response.json()

        self.assertEqual(bag['position'], 'Check In Area')
        self.assertEqual(bag['isBeingRouted'], False)

    def test_placeBagIntoCB(self):
        requests.post(
            "http://localhost:5000/checkInBag", {"passengerId": '46', "flightId": '5', "weight": '55', "classService": 'Premium Economy Class'})

        responsePlaceIntoCB = requests.post(
            "http://localhost:5000/placeBagIntoCB")

        response = requests.post("http://localhost:5000/test_checkInBag", {
                                 "passengerId": '46', "flightId": '5', "weight": '55', "classService": 'Premium Economy Class'})

        bag = response.json()

        self.assertEqual(
            responsePlaceIntoCB.json(), 'BAG ' + str(bag['id']) + ' WAS PLACED INTO THE CONVEYOR BELT')
        self.assertEqual(bag['id'], bag['id'])
        self.assertEqual(bag['position'][1], 'A')
        self.assertEqual(bag['isBeingRouted'], True)


if __name__ == '__main__':
    unittest.main()
