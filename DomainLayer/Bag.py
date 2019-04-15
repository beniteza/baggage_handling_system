from InfrastructureLayer import BagDao


class Bag:
    def __init__(self, bagTagId):
        self.bagTagId = bagTagId
        self.position = 'Check In Area'
        self.isBeingRouted = False
        BagDao().createBagQuery(self.bagTagId, self.position, self.isBeingRouted)

    def getBagId(self):
        return BagDao().getBagIdQuery()
