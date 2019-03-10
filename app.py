# from flask_mysqldb import MySQL
# from dbconfig import DatabaseConfig

from instructions import start_screen
from handler.checking_area import Checking_Area
from handler.conveyor_belts import Conveyor_Belts

# app = DatabaseConfig()
# mysql = MySQL(app)

#Global Data
customer = None
scanned_bags = []
sorted_bags_set = []
routes = []
ready_bag_sets = []

end = False
while(not end):
    start_screen()
    option = input('Option: ')
    if(option == '1'):
        print('Scanning Customer...')
        customer = Checking_Area().scan_customer()

    elif(option == '2'):
        print('Scanning Bag...')
        Checking_Area().scan_bag(customer, scanned_bags)

    elif(option == '3'):
        print('Removing Bag...')
        Checking_Area().remove_bag(scanned_bags)

    elif(option == '4'):
        print('Sorting Bags...')
        Checking_Area().sort_bags(scanned_bags, sorted_bags_set)

    elif(option == '5'):
        print('Generating Routes...')
        Checking_Area().gen_routes(routes, sorted_bags_set)

    elif(option == '6'):
        print('Routing Bags...')
        Checking_Area().route_bags(routes, sorted_bags_set, ready_bag_sets)

    elif(option == '7'):
        print('Loading Bags...')
        Conveyor_Belts().load_bags(scanned_bags, len(ready_bag_sets))

    elif(option == '8'):
        print('Sending Bags...')
        Conveyor_Belts().send_bags(sorted_bags_set, ready_bag_sets, routes)

    elif(option == '9'):
        print('Displaying Bags...')
        Checking_Area().display_bags(scanned_bags)

    elif(option == '10'):
        print('Displaying Routes...')
        Checking_Area().display_routes(routes)

    elif(option == '11'):
        print('Goodbye!')
        end = True
    else:
        print('Invalid input. Try again')
        start_screen()
        option = input('Option: ')

# if __name__ == '__main__':
#     app.run(debug=True)
