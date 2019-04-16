from InfrastructureLayer.AirlineLoadingAreaUserDao import AirlineLoadingAreaUserDao


class AirlineLoadingAreaUser:

    def scanBagTag(self, bagTagId):
        return AirlineLoadingAreaUserDao().scanBagTag(bagTagId)

    def getAllBagsInAirlineLoadingArea(self):
        return AirlineLoadingAreaUserDao().getAllBagsInAirlineLoadingArea()
