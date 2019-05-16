from flask import request, jsonify
from DomainLayer.Loader import Loader


class LoaderHandler:
    def scanBagTag(self):
        bagTagId = request.form['bagTagId']
        bagTagInfo = Loader().scanBagTag(bagTagId)
        return jsonify(bagTagInfo)

    def getAllBagsInAirlineLoadingArea(self):
        airline = request.form['airline']
        bags = Loader().getAllBagsInAirlineLoadingArea(airline)
        return jsonify(bags)
