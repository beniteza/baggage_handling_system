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
    else:
        print('INVALID OPTION')
