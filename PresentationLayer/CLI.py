from InterfaceOptions import InterfaceOptions

while(True):
    InterfaceOptions().startScreen()
    option = input('Option: ')
    if option == '1':
        InterfaceOptions().checkInBag()
    elif option == '2':
        InterfaceOptions().placeBagIntoCB()
    elif option == '3':
        InterfaceOptions().scanBag()
    elif option == '4':
        InterfaceOptions().getAllBagsInAirlineLoadingArea()
    elif option == '5':
        InterfaceOptions().getJammedSignal()
    elif option == '6':
        InterfaceOptions().sendUnjammedSignal()
    else:
        print('INVALID OPTION')
