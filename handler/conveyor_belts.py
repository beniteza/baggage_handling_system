class Conveyor_Belts:
    def load_bags(self, scanned_bags, num_ready_bag_sets):
        if len(scanned_bags) > 0 and num_ready_bag_sets > 0:
            scanned_bags.clear()
            print('\nBAGS LOADED INTO THE CONVEYOR SYSTEM')
        else:
            print('\nNO BAGS TO LOAD')

    def send_bags(self, sorted_bags_set, ready_bag_sets, routes):
        if len(sorted_bags_set) > 0:
            sorted_bags_set.clear()
            ready_bag_sets.clear()
            routes.clear()
            print('\nBAGS SENT INTO THE CONVEYOR SYSTEM')
        else:
            print('\nNO BAGS TO SEND')