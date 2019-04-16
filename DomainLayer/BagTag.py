from InfrastructureLayer.BagDao import BagDao


class BagTag:
    def __init__(self, passengerId, flightId, weight, classService):
        self.passengerId = passengerId
        self.flightId = flightId
        self.weight = weight
        self.classService = classService
        BagDao().createBagTagQuery(passengerId, flightId, weight, classService)

    def getBagTagId(self):
        return BagDao().getBagTagIdQuery()
