from InfrastructureLayer.DBconfig import DatabaseConfig
from flask_mysqldb import MySQL

app = DatabaseConfig()
mysql = MySQL(app)


class CheckInAreaUserDao:
    def placeBagIntoCB(self, bagId):
        cur = mysql.connection.cursor()
        position = 'Conveyor Belt System'
        isBeingRouted = True
        cur.execute("UPDATE `bags` SET `position` = %s, `isBeingRouted` = %s WHERE `id` = %s",
                    (position, isBeingRouted, bagId))
        mysql.connection.commit()
        cur.close()
