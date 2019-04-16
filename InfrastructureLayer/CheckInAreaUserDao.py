from InfrastructureLayer.DBconfig import DatabaseConfig
from flask_mysqldb import MySQL

app = DatabaseConfig()
mysql = MySQL(app)


class CheckInAreaUserDao:
    def placeBagIntoCB(self, bagId):
        cur = mysql.connection.cursor()
        position = 'Conveyor Belt System'
        cur.execute("UPDATE `bags` SET `position` = %s WHERE `id` = %s",
                    (position, bagId))
        mysql.connection.commit()
        cur.close()
