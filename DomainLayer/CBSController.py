from InfrastructureLayer.CBSControllerDao import CBSControllerDao


class CBSController:
    def routeBags(self):
        return CBSControllerDao().routeBags()

    def jammed(self):
        return CBSControllerDao().jammed()

    def deactivateJammedBelt(self):
        return CBSControllerDao().deactivateJammedBelt()

    def activateBelt(self):
        return CBSControllerDao().activateBelt()
