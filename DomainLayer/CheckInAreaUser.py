from InfrastructureLayer.CheckInAreaUserDao import CheckInAreaUserDao


class CheckInAreaUser:
    def placeBagIntoCB(self, bagId):
        return CheckInAreaUserDao().placeBagIntoCB(bagId)
