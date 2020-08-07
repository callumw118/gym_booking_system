import unittest
from tests.activity_test import Activity

class TestActivity(unittest.TestCase):

    def setUp(self):
        self.activity = Activity("HIIT (High Intensity Training)")