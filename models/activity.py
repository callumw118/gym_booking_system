class Activity:
    def __init__(self, name, day_of_week, time, capacity, id=None):
        self.name = name
        self.day_of_week = day_of_week
        self.time = time
        self.capacity = capacity
        self.id = id


    def reduce_capacity_by_1(self, capacity):
        self.capacity -= 1