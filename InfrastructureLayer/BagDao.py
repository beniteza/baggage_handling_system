from InfrastructureLayer.DBconfig import DatabaseConfig
from InfrastructureLayer.GeneralQueries import GeneralQueries
from flask_mysqldb import MySQL

app = DatabaseConfig()
mysql = MySQL(app)


class BagDao:
    def createBagTagQuery(self, passengerId, flightId, weight, classService):
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO bagTags(passengerId, flightId, weight, classService) VALUES (%s, %s, %s, %s)",
                    (passengerId, flightId, weight, classService))
        mysql.connection.commit()

    # Make this a general query
    def getBagTagIdQuery(self):
        bagTagId = GeneralQueries().getLastInsertedIdQuery()
        return bagTagId

    def createBagQuery(self, bagTagId, position, isBeingRouted):
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO bags(bagTagId, position, isBeingRouted) VALUES (%s, %s, %s)",
                    (bagTagId, position, isBeingRouted))
        mysql.connection.commit()

    def getBagIdQuery(self):
        bagId = GeneralQueries().getLastInsertedIdQuery()
        return bagId
