#!/usr/bin/python3
""" Unittest fot the class Amenity. """

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Test the Amenity class"""

    def test_amenity_inheritance(self):
        """Test that Amenity inherits from BaseModel"""
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_amenity_attributes(self):
        """Test the attributes of the Amenity class"""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'name'))
        self.assertEqual(amenity.name, "")

    def test_amenity_to_dict_method(self):
        """Test the to_dict method of Amenity"""
        amenity = Amenity()
        amenity_dict = amenity.to_dict()
        self.assertTrue(isinstance(amenity_dict, dict))
        self.assertEqual(amenity_dict['__class__'], 'Amenity')
        self.assertTrue('to_dict' in dir(amenity))

    def test_amenity_instance_creation(self):
        """Test creating an instance of Amenity"""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)


if __name__ == '__main__':
    unittest.main()
