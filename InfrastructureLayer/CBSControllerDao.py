from InfrastructureLayer.DBconfig import DatabaseConfig
from InfrastructureLayer.RouteBagsHelper import routeBagsHelper, rerouteHelper
from flask_mysqldb import MySQL
import random
import time

app = DatabaseConfig()
mysql = MySQL(app)


class CBSControllerDao:
    def routeBags(self):
        return routeBagsHelper()

    def rerouteBagsInCBS(self, rerouteJammedBags):
        return rerouteHelper(rerouteJammedBags)

    def jammed(self):
        cur = mysql.connection.cursor()
        result = cur.execute(
            "select * from conveyorBelt where `isJammed` = 1")

        if result == 0:
            isJammed = True
            level = random.randint(1, 3)
            beltType = random.randint(1, 4)
            if beltType == 1:
                beltType = 'A'
            elif beltType == 2:
                beltType = 'B'
            elif beltType == 3:
                beltType = 'C'
            elif beltType == 4:
                beltType = 'D'
            cur.execute(
                "UPDATE `conveyorBelt` SET `isJammed` = %s WHERE level = %s and type = %s", (isJammed, level, beltType))
            mysql.connection.commit()

            self.rerouteBagsInCBS(False)
            time.sleep(20)
            self.rerouteBagsInCBS(True)

        cur.close()
        return 'Belt was jammed'

    def deactivateJammedBelt(self):
        cur = mysql.connection.cursor()
        result = cur.execute(
            "select * from conveyorBelt where `isJammed` = 1")

        if result == 0:
            return 'No Jammed Belt to Deactivate'

        isActive = False
        cur.execute(
            "UPDATE `conveyorBelt` SET `isActive` = %s WHERE `isJammed` = 1", [isActive])
        mysql.connection.commit()

        cur.close()
        return 'Belt was deactivated'

    def activateBelt(self):
        cur = mysql.connection.cursor()
        result = cur.execute(
            "select * from conveyorBelt where `isActive` = 0")

        if result == 0:
            return 'No Belt to Activate'

        isActive = True
        cur.execute(
            "UPDATE `conveyorBelt` SET `isActive` = %s WHERE `isActive` = 0", [isActive])
        mysql.connection.commit()

        cur.close()
        return 'Belt was Activated'
