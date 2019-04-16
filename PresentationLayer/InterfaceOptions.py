import requests


class InterfaceOptions:
    def startScreen(self):
        print(
            """
        Baggage Handling System
        1. Check In Bag
        2. Place Bag Into Conveyor Belt
        3. Scan Bag Tag
        4. View Bags In Airline Loading Area
        5. Check If A Conveyor Belt Is Jammed
        6. Send Unjammed Signal
        """
        )

    def checkInBag(self):
        print('Enter Bag Information...')
        passengerId = input('Passenger Id: ')
        flightId = input('Flight Id: ')
        weight = input('Weight: ')
        print(
            """
        Choose Class of Service:
        1. First Class
        2. Business Class
        3. Premium Economy Class
        4. Economy Class
        """
        )
        classService = ''
        while(True):
            classServiceOption = input('Class of Service: ')
            if classServiceOption == '1':
                classService = 'First Class'
                break
            elif classServiceOption == '2':
                classService = 'Business Class'
                break
            elif classServiceOption == '3':
                classService = 'Premium Economy Class'
                break
            elif classServiceOption == '4':
                classService = 'Economy Class'
                break
            else:
                print('INVALID OPTION')
        requests.post(
            "http://localhost:5000/checkInBag", {"passengerId": passengerId, "flightId": flightId, "weight": weight, "classService": classService})
        # requests.post(
        #     "http://localhost:5000/login", {"username": 'axvi', "password": '123'})
        # print('\nBAG CHECKED IN!\n')

    def placeBagIntoCB(self):
        requests.post(
            "http://localhost:5000/placeBagIntoCB")
        print('\nBAG PLACED INTO CB!\n')

    def scanBag(self):
        bagTagId = input('Bag Tag Id: ')
        requests.post(
            "http://localhost:5000/scanBagTag", {"bagTagId": bagTagId})
        print('\nBAG SCANNED!\n')

    def getAllBagsInAirlineLoadingArea(self):
        requests.get(
            "http://localhost:5000/bagsInLoadingArea")
        print('\nBAGS DISPLAYED!\n')

    def getJammedSignal(self):
        requests.get(
            "http://localhost:5000/getJammedSignal")
        print('\nGOT JAMMED SIGNAL!\n')

    def sendUnjammedSignal(self):
        requests.post(
            "http://localhost:5000/sendUnjammedSignal")
        print('\nSENT UNJAMMED SIGNAL!\n')
