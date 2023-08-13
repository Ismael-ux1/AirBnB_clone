#!/usr/bin/python3
""" Unittest for the class Review. """
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Test the Review class"""

    def test_review_inheritance(self):
        """Test that Review inherits from BaseModel"""
        self.assertTrue(issubclass(Review, BaseModel))

    def test_review_attributes(self):
        """Test the attributes of Review class"""
        review = Review()
        self.assertTrue(hasattr(review, 'place_id'))
        self.assertTrue(hasattr(review, 'user_id'))
        self.assertTrue(hasattr(review, 'text'))

    def test_review_attributes_defaults(self):
        """Test the default values of attributes in Review class"""
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")


if __name__ == '__main__':
    unittest.main()
