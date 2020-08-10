import unittest
from models.member import Member

class TestMember(unittest.TestCase):

    def setUp(self):
        self.member = Member("Callum Wolfe", "Premium")

    def test_member_has_name(self):
        self.assertEqual("Callum Wolfe", self.member.full_name)

    def test_member_has_membership(self):
        self.assertEqual("Premium", self.member.membership)