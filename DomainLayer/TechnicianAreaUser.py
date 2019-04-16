from InfrastructureLayer.TechnicianAreaUserDao import TechnicianAreaUserDao


class TechnicianAreaUser:
    def getJammedSignal(self):
        return TechnicianAreaUserDao().getJammedSignal()

    def sendUnjammedSignal(self):
        return TechnicianAreaUserDao().sendUnjammedSignal()
