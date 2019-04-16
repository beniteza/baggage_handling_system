from InfrastructureLayer.CheckInAreaUserDao import CheckInAreaUserDao


class CheckInAreaUser:
    def placeBagIntoCB(self, bagId):
        CheckInAreaUserDao().placeBagIntoCB(bagId)
