from InfrastructureLayer.DBconfig import DatabaseConfig
from flask_mysqldb import MySQL

app = DatabaseConfig()
mysql = MySQL(app)


class GeneralQueries:
    # Make this a general query
    def getLastInsertedIdQuery(self):
        cur = mysql.connection.cursor()
        cur.execute("SELECT LAST_INSERT_ID();")
        id = cur.fetchall()[0]['LAST_INSERT_ID()']
        cur.close()
        return id
