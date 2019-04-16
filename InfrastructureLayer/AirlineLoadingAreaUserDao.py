from InfrastructureLayer.DBconfig import DatabaseConfig
from flask_mysqldb import MySQL

app = DatabaseConfig()
mysql = MySQL(app)


class AirlineLoadingAreaUserDao:
    def scanBagTag(self, bagTagId):
        cur = mysql.connection.cursor()
        result = cur.execute("SELECT * FROM bagTags where id = %s", [bagTagId])
        bagTag = cur.fetchall()
        cur.close()
        if result == 0:
            print('\n\nINVALID TAG\n\n')
            return 'Invalid Tag'
        print('\n\n')
        print(bagTag)
        print('\n\n')
        return bagTag

    def getAllBagsInAirlineLoadingArea(self):
        cur = mysql.connection.cursor()
        result = cur.execute(
            "SELECT * FROM bags WHERE position = 'Airline Loading Area'")
        bags = cur.fetchall()
        cur.close()
        if result == 0:
            print('\n\nNo Bags Have Arrived\n\n')
            return 'No Bags Have Arrived'
        print('\n\n')
        print(bags)
        print('\n\n')
        return bags
