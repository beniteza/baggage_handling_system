from flask import request, jsonify
from DomainLayer.CBSController import CBSController


class CBSControllerHandler:
    def routeBags(self):
        response = CBSController().routeBags()
        return jsonify(response)

    def jammed(self):
        response = CBSController().jammed()
        return jsonify(response)

    def jammedCBChecker(self):
        pass

    def deactivateJammedBelt(self, beltId):
        pass

    def sendJammedSignal(self):
        pass

    def rerouteBagsInCBS(self):
        pass

    def activateBelt(self, beltId):
        pass
