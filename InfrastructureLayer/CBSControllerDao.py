from InfrastructureLayer.DBconfig import DatabaseConfig
from flask_mysqldb import MySQL

app = DatabaseConfig()
mysql = MySQL(app)


class CBSControllerDao:
    def bagsReachedLoadingArea(self):
        cur = mysql.connection.cursor()
        position = 'Airline Loading Area'
        isBeingRouted = False
        cur.execute("UPDATE `bags` SET `position` = %s, `isBeingRouted` = %s WHERE `position` != 'Airline Loading Area' AND `position` != 'Check In Area' ",
                    (position, isBeingRouted))
        mysql.connection.commit()
        cur.close()

    def jammed(self):
        cur = mysql.connection.cursor()
        isJammed = True
        cur.execute(
            "UPDATE `conveyorBelt` SET `isJammed` = %s WHERE id != 0", [isJammed])
        mysql.connection.commit()
        cur.close()

    def jammedCBChecker(self):
        pass

    def routeBags(self):
        pass

    def deactivateJammedBelt(self, beltId):
        pass

    def sendJammedSignal(self):
        pass

    def rerouteBagsInCBS(self):
        pass

    def activateBelt(self, beltId):
        pass
