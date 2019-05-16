from InfrastructureLayer.DBconfig import DatabaseConfig
from flask_mysqldb import MySQL

app = DatabaseConfig()
mysql = MySQL(app)


class TechnicianDao:
    def getJammedSignal(self):
        cur = mysql.connection.cursor()
        result = cur.execute(
            "SELECT * FROM conveyorBelt WHERE isJammed = %s", [True])
        jammedBelt = cur.fetchall()
        cur.close()
        if result == 0:
            return 'No Conveyor Belts are Jammed'
        jammedBelt = jammedBelt[0]
        return jammedBelt

    def sendUnjammedSignal(self):
        cur = mysql.connection.cursor()
        result = cur.execute(
            "SELECT * FROM conveyorBelt WHERE isJammed = %s", [True])

        if result == 0:
            return 'No Conveyor Belts are Jammed'

        cur.execute("UPDATE `conveyorBelt` SET `isJammed` = %s WHERE `isJammed` = %s",
                    (False, True))
        mysql.connection.commit()
        cur.close()
        return 'Conveyor Belt Was Unjammed!'
