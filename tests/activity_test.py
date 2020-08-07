import unittest
from models.activity import Activity

class TestActivity(unittest.TestCase):

    def setUp(self):
        self.activity = Activity("HIIT (High Intensity Training)")

    def test_activity_has_name(self):
        self.assertEqual("HIIT (High Intensity Training)", self.activity.name)