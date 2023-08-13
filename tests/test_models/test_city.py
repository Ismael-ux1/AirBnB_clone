#!/usr/bin/python3
""" Unittest for the class city. """
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Test the City class"""

    def test_city_inheritance(self):
        """Test that City inherits from BaseModel"""
        self.assertTrue(issubclass(City, BaseModel))

    def test_city_attributes(self):
        """Test the attributes of the City class"""
        city = City()
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertEqual(city.state_id, "")
        self.assertTrue(hasattr(city, 'name'))
        self.assertEqual(city.name, "")

    def test_city_to_dict_method(self):
        """Test the to_dict method of City"""
        city = City()
        city_dict = city.to_dict()
        self.assertTrue(isinstance(city_dict, dict))
        self.assertEqual(city_dict['__class__'], 'City')
        self.assertTrue('to_dict' in dir(city))

    def test_city_instance_creation(self):
        """Test creating an instance of City"""
        city = City()
        self.assertIsInstance(city, City)


if __name__ == '__main__':
    unittest.main()
