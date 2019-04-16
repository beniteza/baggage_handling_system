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
            print('\n\nNo Conveyor Belts are Jammed\n\n')
            return 'No Conveyor Belts are Jammed'
        print('\n\nConveyor Belt Jammed!\n\n')
        return 'Conveyor Belt Jammed!'

    def sendUnjammedSignal(self):
        cur = mysql.connection.cursor()
        cur.execute("UPDATE `conveyorBelt` SET `isJammed` = %s WHERE `isJammed` = %s",
                    (False, True))
        mysql.connection.commit()
        cur.close()
        print('\n\nConveyor Belt Was Unjammed!\n\n')
        return 'Conveyor Belt Was Unjammed!'
