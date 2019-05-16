from InfrastructureLayer.DBconfig import DatabaseConfig
from flask_mysqldb import MySQL

app = DatabaseConfig()
mysql = MySQL(app)


class LoaderDao:
    def scanBagTag(self, bagTagId):
        cur = mysql.connection.cursor()
        result = cur.execute("SELECT * FROM bagTags where id = %s", [bagTagId])
        bagTag = cur.fetchall()
        cur.close()
        if result == 0:
            return 'Invalid Tag'
        return bagTag

    def getAllBagsInAirlineLoadingArea(self, airline):
        cur = mysql.connection.cursor()
        result = cur.execute(
            "SELECT * FROM bags WHERE position = 'Airline Loading Area'")
        bags = cur.fetchall()
        if result == 0:
            return 'No Bags Have Arrived'

        bagsInLoadingArea = []
        for bag in bags:
            bagTagId = bag['bagTagId']

            cur.execute(
                "select flightId from bagTags where `id` = %s", [bagTagId])
            flightId = cur.fetchall()

            cur.execute(
                "select airline from flights where `id` = %s", [flightId[0]['flightId']])
            bagAirline = cur.fetchall()

            if airline == bagAirline[0]['airline']:
                bagsInLoadingArea.append(bag)
        cur.close()
        return bagsInLoadingArea
