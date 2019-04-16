from flask import request
from DomainLayer import CBSController


class CBSControllerHandler:
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
