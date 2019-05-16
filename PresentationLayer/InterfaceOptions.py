import requests


class InterfaceOptions:
    def userSelectScreen(self):
        print(
            """
        User Login
        1. Clerk
        2. Loader
        3. Technician
        """
        )

    def clerkStartScreen(self):
        print(
            """
        CLERK - Baggage Handling System
        1. Check In Bag
        2. Place Bag Into Conveyor Belt
        3. Exit
        """
        )

    def loaderStartScreen(self):
        print(
            """
        LOADER - Baggage Handling System
        1. Scan Bag Tag
        2. View Bags In Airline Loading Area
        3. Check If A Conveyor Belt Is Jammed
        4. Exit
        """
        )

    def technicianStartScreen(self):
        print(
            """
        TECHNICIAN - Baggage Handling System
        1. Check If A Conveyor Belt Is Jammed
        2. Send Unjammed Signal
        3. Exit
        """
        )

    # def startScreen(self):
    #     print(
    #         """
    #     Baggage Handling System
    #     1. Check In Bag
    #     2. Place Bag Into Conveyor Belt
    #     3. Scan Bag Tag
    #     4. View Bags In Airline Loading Area
    #     5. Check If A Conveyor Belt Is Jammed
    #     6. Send Unjammed Signal
    #     """
    #     )

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
        response = requests.post(
            "http://localhost:5000/checkInBag", {"passengerId": passengerId, "flightId": flightId, "weight": weight, "classService": classService})

        print('\n')
        print(response.text)

    def placeBagIntoCB(self):
        response = requests.post(
            "http://localhost:5000/placeBagIntoCB")
        print('\n')
        print(response.text)

    def scanBag(self):
        bagTagId = input('Bag Tag Id: ')
        scannedBag = requests.post(
            "http://localhost:5000/scanBagTag", {"bagTagId": bagTagId})
        print('\n')
        print(scannedBag.text)

    def getAllBagsInAirlineLoadingArea(self):
        print(
            """
        Choose Airline:
        1. A
        2. B
        3. C
        4. D
        """
        )
        airline = ''
        while(True):
            airlineOption = input('Airline: ')
            if airlineOption == '1':
                airline = 'A'
                break
            elif airlineOption == '2':
                airline = 'B'
                break
            elif airlineOption == '3':
                airline = 'C'
                break
            elif airlineOption == '4':
                airline = 'D'
                break
            else:
                print('INVALID OPTION')
        bags = requests.post(
            "http://localhost:5000/bagsInLoadingArea", {"airline": airline})
        print('\n')
        print(bags.text)

    def getJammedSignal(self):
        jammedBelt = requests.get(
            "http://localhost:5000/getJammedSignal")
        print('\n')
        print(jammedBelt.text)

    def sendUnjammedSignal(self):
        response = requests.post(
            "http://localhost:5000/sendUnjammedSignal")
        print('\n')
        print(response.text)
