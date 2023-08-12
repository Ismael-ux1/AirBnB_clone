#!/usr/bin/python3
"""Unittest module for the BaseModel Class."""
import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    """
    Unit tests for the BaseModel class.
    """



    def setUp(self):
        """
        Set up test instances.
        """
        self.base_model = BaseModel()

    def test_id_generation(self):
        """
        Test the generation of a unique ID for each instance.
        """
        self.assertTrue(hasattr(self.base_model, 'id'))
        self.assertIsInstance(self.base_model.id, str)

    def test_created_at(self):
        """
        Test the creation timestamp.
        """
        self.assertTrue(hasattr(self.base_model, 'created_at'))
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_updated_at_initial(self):
        """
        Test the initial updated_at timestamp.
        """
        self.assertTrue(hasattr(self.base_model, 'updated_at'))
        self.assertIsInstance(self.base_model.updated_at, datetime)
        self.assertEqual(self.base_model.created_at, self.base_model.updated_at)

    def test_str_representation(self):
        """
        Test the __str__ method.
        """
        expected_str = "[BaseModel] ({}) {}".format(self.base_model.id, self.base_model.__dict__)
        self.assertEqual(str(self.base_model), expected_str)

    def test_save_method(self):
        """
        Test the save method.
        """
        prev_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(prev_updated_at, self.base_model.updated_at)

    def test_to_dict_method(self):
        """
        Test the to_dict method.
        """
        obj_dict = self.base_model.to_dict()
        self.assertTrue(isinstance(obj_dict, dict))
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['id'], self.base_model.id)
        self.assertEqual(obj_dict['created_at'], self.base_model.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], self.base_model.updated_at.isoformat())

if __name__ == '__main__':
    unittest.main()
