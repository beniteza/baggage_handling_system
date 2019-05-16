from flask import request
from DomainLayer.Bag import Bag
from DomainLayer.BagTag import BagTag


class BagHandler:
    def createBag(self, passengerId, flightId, weight, classService):
        bagTag = BagTag(passengerId, flightId, weight, classService)
        bagTagId = bagTag.getBagTagId()
        Bag(bagTagId)
        return 'BAG CHECKED IN. BAG TAG ID = ' + str(bagTagId)
