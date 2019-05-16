from InfrastructureLayer.CBSControllerDao import CBSControllerDao


class CBSController:
    def routeBags(self):
        return CBSControllerDao().routeBags()

    def jammed(self):
        return CBSControllerDao().jammed()

    def jammedCBChecker(self):
        pass

    def deactivateJammedBelt(self, beltId):
        pass

    def sendJammedSignal(self):
        pass

    def rerouteBagsInCBS(self):
        pass

    def activateBelt(self, beltId):
        pass
