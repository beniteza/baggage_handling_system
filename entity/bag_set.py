import random

class Bag_Set:
    def __init__(self, route, fragility_bag_set):
        self.id = random.randint(0,1000)
        self.bags = fragility_bag_set
        self.route = route

    def __str__(self):
        return f"""
                BAG_SET ID: {self.id},
                BAG_SET BAGS: {self.bags},
                BAG ROUTE: {self.route}
                """