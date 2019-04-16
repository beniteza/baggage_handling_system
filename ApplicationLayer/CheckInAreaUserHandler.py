from flask import request, jsonify
from ApplicationLayer.BagHandler import BagHandler
from DomainLayer.CheckInAreaUser import CheckInAreaUser
from DomainLayer.Bag import Bag, getBagId
from DomainLayer.BagTag import BagTag


class CheckInAreaUserHandler:
    def checkInBag(self):
        passengerId = request.form['passengerId']
        flightId = request.form['flightId']
        weight = request.form['weight']
        classService = request.form['classService']
        result = BagHandler().createBag(passengerId, flightId, weight, classService)
        return jsonify(result)

    def placeBagIntoCB(self):
        bagId = getBagId()
        result = CheckInAreaUser().placeBagIntoCB(bagId)
        return jsonify(result)
