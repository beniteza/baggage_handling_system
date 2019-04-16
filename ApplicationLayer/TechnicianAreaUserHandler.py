from flask import request, jsonify
from DomainLayer.TechnicianAreaUser import TechnicianAreaUser


class TechnicianAreaUserHandler:
    def getJammedSignal(self):
        signal = TechnicianAreaUser().getJammedSignal()
        return jsonify(signal)

    def sendUnjammedSignal(self):
        TechnicianAreaUser().sendUnjammedSignal()
