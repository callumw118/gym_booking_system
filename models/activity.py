class Activity:
    def __init__(self, name, day_of_week, time, capacity, id=None, members_booked=0):
        self.name = name
        self.day_of_week = day_of_week
        self.time = time
        self.capacity = capacity
        self.id = id
        self.members_booked = members_booked


    def reduce_capacity_by_1(self, capacity):
        self.capacity -= 1

    
    def get_capacity_left(self, capacity, members_booked):
        space_left = capacity - members_booked
        return space_left