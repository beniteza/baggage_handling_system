from InfrastructureLayer.TechnicianDao import TechnicianDao


class Technician:
    def getJammedSignal(self):
        return TechnicianDao().getJammedSignal()

    def sendUnjammedSignal(self):
        return TechnicianDao().sendUnjammedSignal()
