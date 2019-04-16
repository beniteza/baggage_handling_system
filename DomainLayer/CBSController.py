from InfrastructureLayer.CBSControllerDao import CBSControllerDao


class CBSController:
    def bagsReachedLoadingArea(self):
        CBSControllerDao().bagsReachedLoadingArea()

    def jammed(self):
        CBSControllerDao().jammed()

    def jammedCBChecker(self):
        pass

    def routeBags(self):
        pass

    def deactivateJammedBelt(self, beltId):
        pass

    def sendJammedSignal(self):
        # check if a cb is jammed from the db
        pass

    def rerouteBagsInCBS(self):
        pass

    def activateBelt(self, beltId):
        pass
