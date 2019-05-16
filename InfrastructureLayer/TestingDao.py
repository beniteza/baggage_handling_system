from InfrastructureLayer.DBconfig import DatabaseConfig
from InfrastructureLayer.GeneralQueries import GeneralQueries
from flask_mysqldb import MySQL
import random

app = DatabaseConfig()
mysql = MySQL(app)


class TestingDao:
    def test_checkInBag(self, passengerId, flightId, weight, classService):
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM bagTags where passengerId = %s and flightId = %s and weight = %s and classService = %s",
                    (passengerId, flightId, weight, classService))
        bagTag = cur.fetchall()
        cur.execute("SELECT * FROM bags where bagTagId = %s",
                    [bagTag[0]['id']])
        bag = cur.fetchall()

        cur.close()
        return bag[0]
