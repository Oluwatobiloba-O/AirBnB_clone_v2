#!/usr/bin/python3
"""Test city model"""
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """Class that performs tests for city"""

    def __init__(self, *args, **kwargs):
        """Contructor"""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """state testing"""
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """name testing"""
        new = self.value()
        self.assertEqual(type(new.name), str)
