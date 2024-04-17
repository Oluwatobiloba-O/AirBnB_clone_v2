#!/usr/bin/python3
"""Testing user model"""
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """Class that test for user"""

    def __init__(self, *args, **kwargs):
        """Cponstructor"""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """First_name test"""
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """Last_name test"""
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """email test"""
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """Password test"""
        new = self.value()
        self.assertEqual(type(new.password), str)
