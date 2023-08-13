#!/usr/bin/python3

import unittest
import json
import os
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        # Create an instance of FileStorage for testing
        self.storage = FileStorage()

    def tearDown(self):
        # Remove the test file if it exists
        if os.path.exists(self.storage._FileStorage__file_path):
            os.remove(self.storage._FileStorage__file_path)

    def test_all_method(self):
        # Test that the all method returns a dictionary
        result = self.storage.all()
        self.assertIsInstance(result, dict)

    def test_new_method(self):
        # Test the new method by adding a new object to __objects
        obj = BaseModel()
        self.storage.new(obj)
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertIn(key, self.storage._FileStorage__objects)

    def test_save_method(self):
        # Test the save method by saving an object to a file
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        with open(self.storage._FileStorage__file_path, 'r') as file:
            data = json.load(file)
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertIn(key, data)

    def test_reload_method(self):
        # Test the reload method by reloading objects from a file
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertIn(key, new_storage._FileStorage__objects)


if __name__ == '__main__':
    unittest.main()
