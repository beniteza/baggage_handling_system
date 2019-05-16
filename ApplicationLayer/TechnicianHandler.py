from flask import request, jsonify
from DomainLayer.Technician import Technician


class TechnicianHandler:
    def getJammedSignal(self):
        signal = Technician().getJammedSignal()
        return jsonify(signal)

    def sendUnjammedSignal(self):
        result = Technician().sendUnjammedSignal()
        return jsonify(result)
