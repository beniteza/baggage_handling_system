from flask import request, jsonify
from DomainLayer.CBSController import CBSController


class CBSControllerHandler:
    def routeBags(self):
        response = CBSController().routeBags()
        return jsonify(response)

    def jammed(self):
        response = CBSController().jammed()
        return jsonify(response)

    def deactivateJammedBelt(self):
        response = CBSController().deactivateJammedBelt()
        return jsonify(response)

    def activateBelt(self):
        response = CBSController().activateBelt()
        return jsonify(response)
