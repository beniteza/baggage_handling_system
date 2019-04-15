from flask import request
from DomainLayer import Bag, BagTag


class BagHandler:
    def checkInBag(self):
        passengerId = request.form['passengerId']
        flightId = request.form['flightId']
        weight = request.form['weight']
        classService = request.form['classService']
        # Create Bag Tag and get its id
        bagTag = BagTag(passengerId, flightId, weight, classService)
        bagTagId = bagTag.getBagTagId()
        # Create Bag
        bag = Bag(bagTagId)
        return bag
