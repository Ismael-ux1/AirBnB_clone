#!/usr/bin/python3
""" Unittest for class User """
import unittest
from models.user import User
from datetime import datetime
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """
    Test cases for the User class.
    """

    def test_user_attributes(self):
        # Test if User instance has expected attributes
        user = User()
        self.assertTrue(hasattr(user, "email"))
        self.assertTrue(hasattr(user, "password"))
        self.assertTrue(hasattr(user, "first_name"))
        self.assertTrue(hasattr(user, "last_name"))
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_user_inheritance(self):
        # Test if User class inherits from BaseModel
        user = User()
        self.assertIsInstance(user, User)
        self.assertTrue(issubclass(User, BaseModel))

    def test_user_to_dict(self):
        # Test the to_dict method of User
        user = User()
        user_dict = user.to_dict()
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertIsInstance(user_dict['created_at'], str)
        self.assertIsInstance(user_dict['updated_at'], str)

    def test_user_str_representation(self):
        # Test the string representation (__str__) of User
        user = User()
        user_str = str(user)
        self.assertIn("[User]", user_str)
        self.assertIn("'id':", user_str)
        self.assertIn("'created_at':", user_str)
        self.assertIn("'updated_at':", user_str)


if __name__ == '__main__':
    unittest.main()
