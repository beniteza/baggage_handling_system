from InfrastructureLayer.DBconfig import DatabaseConfig
from flask_mysqldb import MySQL

app = DatabaseConfig()
mysql = MySQL(app)


class TechnicianAreaUserDao:
    def getJammedSignal(self):
        cur = mysql.connection.cursor()
        result = cur.execute(
            "SELECT * FROM conveyorBelt WHERE isJammed = %s", [True])
        cur.close()
        if result == 0:
            return 'No Conveyor Belts are Jammed'
        return 'Conveyor Belt Jammed!'

    def sendUnjammedSignal(self):
        cur = mysql.connection.cursor()
        cur.execute("UPDATE `conveyorBelt` SET `isJammed` WHERE `isJammed` = %s",
                    (False, True))
        mysql.connection.commit()
        cur.close()
