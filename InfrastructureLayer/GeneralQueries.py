from InfrastructureLayer.DBconfig import DatabaseConfig
from flask_mysqldb import MySQL

app = DatabaseConfig()
mysql = MySQL(app)


class GeneralQueries:
    def getLastInsertedIdQuery(self, table):
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM " + table + " ORDER BY id DESC LIMIT 0, 1")
        id = cur.fetchall()[0]['id']
        cur.close()
        return id
