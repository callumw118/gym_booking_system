import unittest
from models.member import Member
from models.activity import Activity
from models.booking import Booking

class TestBooking(unittest.TestCase):

    def setUp(self):
        self.member = Member("Callum Wolfe")
        self.activity = Activity("HIIT (High Intensity Training)", "Monday", "13:00", 10)
        self.booking = Booking(self.member, self.activity)

    def test_booking_has_member(self):
        self.assertEqual("Callum Wolfe", self.booking.member.full_name)

    def test_booking_has_activity(self):
        self.assertEqual("HIIT (High Intensity Training)", self.booking.activity.name)

    def test_booking_has_day_of_week(self):
        self.assertEqual("Monday", self.booking.activity.day_of_week)

    def test_booking_has_time(self):
        self.assertEqual("13:00", self.booking.activity.time)

    def test_booking_has_capacity(self):
        self.assertEqual(10, self.booking.activity.capacity)
