from InfrastructureLayer.DBconfig import DatabaseConfig
from InfrastructureLayer.GeneralQueries import GeneralQueries
from flask_mysqldb import MySQL
import random

app = DatabaseConfig()
mysql = MySQL(app)


class ClerkDao:
    def placeBagIntoCB(self, bagId):
        cur = mysql.connection.cursor()
        isBeingRouted = True
        position = GeneralQueries().randomBeltPosition()
        cur.execute("UPDATE `bags` SET `position` = %s, `isBeingRouted` = %s WHERE `id` = %s",
                    (position, isBeingRouted, bagId))
        mysql.connection.commit()
        cur.close()
        return 'BAG ' + str(bagId) + ' WAS PLACED INTO THE CONVEYOR BELT'
