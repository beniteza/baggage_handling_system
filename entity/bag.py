import random
from sample_data import get_bags

class Bag:
    def __init__(self, customer):
        bags = get_bags()
        bag_pos = random.randint(0,9)
        self.id = bag_pos + 1
        self.isFragile = bags[bag_pos]['isFragile']
        self.weight = bags[bag_pos]['weight']
        self.customer = customer

    def __str__(self):
        return f"""
                BAG ID: {self.id},
                BAG IS FRAGILE: {self.isFragile},
                BAG WEIGHT: {self.weight},
                BAG OWNER: {self.customer.name}
                """