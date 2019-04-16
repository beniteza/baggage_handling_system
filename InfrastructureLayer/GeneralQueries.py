from InfrastructureLayer.DBconfig import DatabaseConfig
from flask_mysqldb import MySQL

app = DatabaseConfig()
mysql = MySQL(app)


class GeneralQueries:
    # Make this a general query
    def getLastInsertedIdQuery(self, table):
        cur = mysql.connection.cursor()
        # cur.execute("SELECT LAST_INSERT_ID();")
        # id = cur.fetchall()[0]['LAST_INSERT_ID()']
        cur.execute("SELECT * FROM " + table + " ORDER BY id DESC LIMIT 0, 1")
        id = cur.fetchall()[0]['id']
        cur.close()
        return id
