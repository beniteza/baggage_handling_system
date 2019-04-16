from flask import request
from DomainLayer.CBSController import CBSController


class CBSControllerHandler:
    def bagsReachedLoadingArea(self):
        CBSController().bagsReachedLoadingArea()

    def jammed(self):
        CBSController().jammed()

    def jammedCBChecker(self):
        pass

    def routeBags(self):
        pass

    def deactivateJammedBelt(self, beltId):
        pass

    def sendJammedSignal(self):
        pass

    def rerouteBagsInCBS(self):
        pass

    def activateBelt(self, beltId):
        pass
