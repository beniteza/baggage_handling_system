import random
from sample_data import get_routes

class Route:
    def __init__(self):
        routes = get_routes()
        route_pos = random.randint(0,3)
        self.id = route_pos + 1
        self.first = routes[route_pos]['First']
        self.second = routes[route_pos]['Second']
        self.third = routes[route_pos]['Third']

    def __str__(self):
        return f"""
                ROUTE ID: {self.id},
                FIRST POINT: {self.first},
                SECOND POINT: {self.second},
                THIRD POINT: {self.third}
                """