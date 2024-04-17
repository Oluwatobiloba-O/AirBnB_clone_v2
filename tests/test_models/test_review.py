#!/usr/bin/python3
"""Testing the Review model"""
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """Class that performs review testing"""

    def __init__(self, *args, **kwargs):
        """Constructor"""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """Place_id test"""
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """user_id test"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """Text testing"""
        new = self.value()
        self.assertEqual(type(new.text), str)
