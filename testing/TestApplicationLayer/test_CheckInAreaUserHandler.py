from InfrastructureLayer.DBconfig import DatabaseConfig
from flask_mysqldb import MySQL
import unittest
import requests

app = DatabaseConfig()
mysql = MySQL(app)


class TestCheckInAreaUserHandler(unittest.TestCase):
    def test_checkInBag(self):
        response = requests.post(
            "http://localhost:5000/checkInBag", {"passengerId": '55', "flightId": '55', "weight": '55', "classService": 'Premium Economy Class'})

        cur = mysql.connection.cursor()
        result = cur.execute("SELECT * FROM bags where passengerId = %s and flightId = %s and weight = %s and classService = %s",
                             ('55', '55', '55', 'Premium Economy Class'))
        bag = cur.fetchall()

        print(bag)
        cur.execute("DELETE * FROM bags where id = %s", [bag['id']])
        cur.close()

        self.assertEqual(bag['id'], bag['id'])
        self.assertEqual(bag['position'], 'Check in Area')
        self.assertEqual(bag['isBeingRouted'], False)

    def test_placeBagIntoCB(self):
        response = requests.post(
            "http://localhost:5000/placeBagIntoCB")
        self.assertEqual(
            response.json(), 'BAG WAS PLACED INTO THE CONVEYOR BELTs')


if __name__ == '__main__':
    unittest.main()
