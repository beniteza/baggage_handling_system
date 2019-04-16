from InfrastructureLayer import CheckInAreaUserDao


class CheckInAreaUser:
    def placeBagIntoCB(self, bagId):
        CheckInAreaUserDao().placeBagIntoCB(bagId)
