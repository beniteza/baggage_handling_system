import random
from sample_data import get_customers

class Customer:
    def __init__(self):
        customers = get_customers()
        customer_pos = random.randint(0,9)
        self.id = customer_pos + 1
        self.name = customers[customer_pos]['name']

    def __str__(self):
        return f"""
                CUSTOMER ID: {self.id},
                CUSTOMER NAME: {self.name}
                """