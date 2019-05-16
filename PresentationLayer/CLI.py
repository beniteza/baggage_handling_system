from InterfaceOptions import InterfaceOptions

while(True):
    InterfaceOptions().userSelectScreen()
    user = input('User: ')
    if user == '1':
        while(user != 'exit'):
            InterfaceOptions().clerkStartScreen()
            option = input('Option: ')
            if option == '1':
                InterfaceOptions().checkInBag()
            elif option == '2':
                InterfaceOptions().placeBagIntoCB()
            elif option == '3':
                user = 'exit'
            else:
                print('INVALID OPTION')
    elif user == '2':
        while(user != 'exit'):
            InterfaceOptions().loaderStartScreen()
            option = input('Option: ')
            if option == '1':
                InterfaceOptions().scanBag()
            elif option == '2':
                InterfaceOptions().getAllBagsInAirlineLoadingArea()
            elif option == '3':
                InterfaceOptions().getJammedSignal()
            elif option == '4':
                user = 'exit'
            else:
                print('INVALID OPTION')
    elif user == '3':
        while(user != 'exit'):
            InterfaceOptions().technicianStartScreen()
            option = input('Option: ')
            if option == '1':
                InterfaceOptions().getJammedSignal()
            elif option == '2':
                InterfaceOptions().sendUnjammedSignal()
            elif option == '3':
                user = 'exit'
            else:
                print('INVALID OPTION')
    else:
        print('INVALID USER')
