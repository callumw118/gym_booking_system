import unittest
from models.activity import Activity

class TestActivity(unittest.TestCase):

    def setUp(self):
        self.activity = Activity("HIIT (High Intensity Training)", "Monday", "13:00", 10)

    def test_activity_has_name(self):
        self.assertEqual("HIIT (High Intensity Training)", self.activity.name)

    def test_activity_has_day_of_week(self):
        self.assertEqual("Monday", self.activity.day_of_week)

    def test_activity_has_time(self):
        self.assertEqual("13:00", self.activity.time)
    
    def test_activity_has_capacity(self):
        self.assertEqual(10, self.activity.capacity)