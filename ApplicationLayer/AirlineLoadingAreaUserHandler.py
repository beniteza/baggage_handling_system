from flask import request, jsonify
from DomainLayer.AirlineLoadingAreaUser import AirlineLoadingAreaUser


class AirlineLoadingAreaUserHandler:
    def scanBagTag(self):
        bagTagId = request.form['bagTagId']
        bagTagInfo = AirlineLoadingAreaUser().scanBagTag(bagTagId)
        return jsonify(bagTagInfo)

    def getAllBagsInAirlineLoadingArea(self):
        bags = AirlineLoadingAreaUser().getAllBagsInAirlineLoadingArea()
        return jsonify(bags)
