from InfrastructureLayer.DBconfig import DatabaseConfig
from flask_mysqldb import MySQL
import random

app = DatabaseConfig()
mysql = MySQL(app)


class GeneralQueries:
    def getLastInsertedIdQuery(self, table):
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM " + table + " ORDER BY id DESC LIMIT 0, 1")
        id = cur.fetchall()[0]['id']
        cur.close()
        return id

    def randomBeltPosition(self):
        level = random.randint(1, 3)
        beltType = 'A'
        # beltType = random.randint(1, 4)
        # if beltType == 1:
        #     beltType = 'A'
        # elif beltType == 2:
        #     beltType = 'B'
        # elif beltType == 3:
        #     beltType = 'C'
        # elif beltType == 4:
        #     beltType = 'D'
        position = str(level) + beltType
        return position
