from InfrastructureLayer.ClerkDao import ClerkDao


class Clerk:
    def placeBagIntoCB(self, bagId):
        return ClerkDao().placeBagIntoCB(bagId)
