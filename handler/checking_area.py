from entity.customer import Customer
from entity.bag import Bag
from entity.bag_set import Bag_Set
from entity.route import Route

class Checking_Area:
    def scan_customer(self):
        customer = Customer()
        print(customer)
        return customer

    def scan_bag(self, customer, scanned_bags):
        if customer != None:
            bag = Bag(customer)
            scanned_bags.append(bag)
            print(bag)
        else:
            print('\nNO CUSTOMER SELECTED. TRY AGAIN')

    def remove_bag(self, scanned_bags):
        num_bags = len(scanned_bags)
        if num_bags > 0:
            scanned_bags.pop(num_bags - 1)
        else:
            print('\nTHERE ARE NO BAGS')
    
    #Max of 500 pounds per set
    def sort_bags(self, scanned_bags, sorted_bags_set):
        num_bags = len(scanned_bags)
        if num_bags > 0:
            max_weight = 500
            current_fragile_weight = 0
            current_non_frag_weight = 0
            fragile_set = []
            non_fragile_set = []
            for bag in scanned_bags:
                if bag.isFragile:
                    if bag.weight + current_fragile_weight <= max_weight:
                        fragile_set.append(bag)
                        current_fragile_weight += bag.weight
                    else:
                        sorted_bags_set.append(fragile_set)
                        fragile_set = []
                        current_fragile_weight = bag.weight
                        fragile_set.append(bag)
                else:
                    if bag.weight + current_non_frag_weight <= max_weight:
                        non_fragile_set.append(bag)
                        current_non_frag_weight += bag.weight
                    else:
                        sorted_bags_set.append(non_fragile_set)
                        non_fragile_set = []
                        current_non_frag_weight = bag.weight
                        non_fragile_set.append(bag)
            sorted_bags_set.append(fragile_set)
            sorted_bags_set.append(non_fragile_set)
            print(sorted_bags_set)
        else:
            print('\nTHERE ARE NO BAGS')
    
    #TO DO: gen_routes more than once
    def gen_routes(self, routes, sorted_bags_set):
        num_routes = len(sorted_bags_set)
        if num_routes > 0:
            for x in range(num_routes):
                new_route = Route()
                routes.append(new_route)
                print(new_route)
        else:
            print('\nNO ROUTES WERE CREATED')

    def route_bags(self, routes, sorted_bags_set,ready_bag_sets):
        num_routes = len(routes)
        num_sorted_sets = len(sorted_bags_set)
        if num_routes > 0 and num_sorted_sets > 0:
            for x in range(num_routes):
                new_bag_set = Bag_Set(routes[x], sorted_bags_set[x])
                ready_bag_sets.append(new_bag_set)
                print(new_bag_set)
        else:
            print('\nNO SET OF BAGS AVAILABLE TO ROUTE')

    def display_bags(self, scanned_bags):
        num_bags = len(scanned_bags)
        if num_bags > 0:
            for bag in scanned_bags:
                print(bag)
        else:
            print('\nTHERE ARE NO BAGS')

    def display_routes(self, routes):
        if len(routes) > 0:
            for route in routes:
                print(route)
        else:
            print('\nNO ROUTES TO DISPLAY')