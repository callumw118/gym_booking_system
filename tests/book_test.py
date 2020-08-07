import unittest
from models.member import Member
from models.activity import Activity
from models.booking import Booking

class TestBook(unittest.TestCase):

    def setUp(self):
        self.member = Member("Callum Wolfe")
        self.activity = Activity("HIIT (High Intensity Training)", "13:00")
        self.booking = Booking(self.member, self.activity)