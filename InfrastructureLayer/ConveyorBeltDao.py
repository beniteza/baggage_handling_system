from InfrastructureLayer.DBconfig import DatabaseConfig
from flask_mysqldb import MySQL

app = DatabaseConfig()
mysql = MySQL(app)


class ConveyorBeltDao:
    def activateConveyorBelt(self):
        pass

    def deactivateConveyorBelt(self):
        pass

    def jamConveyorBelt(self):
        pass

    def unjamConveyorBelt(self):
        pass
