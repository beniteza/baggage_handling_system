from InfrastructureLayer.TestingDao import TestingDao


class Testing:
    def test_checkInBag(self, passengerId, flightId, weight, classService):
        return TestingDao().test_checkInBag(passengerId, flightId, weight, classService)
