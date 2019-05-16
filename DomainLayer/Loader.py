from InfrastructureLayer.LoaderDao import LoaderDao


class Loader:

    def scanBagTag(self, bagTagId):
        return LoaderDao().scanBagTag(bagTagId)

    def getAllBagsInAirlineLoadingArea(self, airline):
        return LoaderDao().getAllBagsInAirlineLoadingArea(airline)
