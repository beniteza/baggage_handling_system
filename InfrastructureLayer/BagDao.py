from InfrastructureLayer.DBconfig import DatabaseConfig
from flask_mysqldb import MySQL

app = DatabaseConfig()
mysql = MySQL(app)


class BagDao:
    def createBagTagQuery(self, passengerId, flightId, weight, classService):
        cur.execute("INSERT INTO bagTags(passengerId, flightId, weight, classService) VALUES (%s, %s, %s, %s)",
                    (passengerId, flightId, weight, classService))
        mysql.connection.commit()

    def getBagTagIdQuery(self):
        cur.execute("SELECT LAST_INSERT_ID();")
        bagTagId = cur.fetchall()[0]['LAST_INSERT_ID()']
        cur.close()
        return bagTagId

    def createBagQuery(self, bagTagId, position, isBeingRouted):
        cur.execute("INSERT INTO bags(bagTagId, position, isBeingRouted) VALUES (%s, %s, %s)",
                    (bagTagId, position, isBeingRouted))
        mysql.connection.commit()

    def getBagIdQuery(self):
        cur.execute("SELECT LAST_INSERT_ID();")
        bagId = cur.fetchall()[0]['LAST_INSERT_ID()']
        cur.close()
        return bagId
