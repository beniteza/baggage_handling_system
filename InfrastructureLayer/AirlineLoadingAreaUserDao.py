from InfrastructureLayer.DBconfig import DatabaseConfig
from flask_mysqldb import MySQL

app = DatabaseConfig()
mysql = MySQL(app)


class AirlineLoadingAreaUserDao:
    def scanBagTag(self, bagTagId):
        cur = mysql.connection.cursor()
        result = cur.execute("SELECT * FROM bag where id = %s", [bagTagId])
        bagTag = cur.fetchall()
        cur.close()
        if result == 0:
            return 'Invalid Tag'
        return bagTag

    def getAllBagsInAirlineLoadingArea(self):
        cur = mysql.connection.cursor()
        position = 'Airline Loading Area'
        result = cur.execute(
            "SELECT * FROM bags WHERE position = %s", [position])
        bags = cur.fetchall()
        cur.close()
        if result == 0:
            return 'No Bags Have Arrived'
        return bags
