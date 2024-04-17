#!/usr/bin/python3
"""The place model"""
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """Class that tests for Place"""

    def __init__(self, *args, **kwargs):
        """Contructor"""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """city test"""
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """user_id test"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """name tester"""
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """description test"""
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """room number test"""
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """bathroom number test"""
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """test for max number of guest"""
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """night pricing test"""
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """latitude test"""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """longitude test"""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """amenity id test"""
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
