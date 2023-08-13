#!/usr/bin/python3
""" Unittest for the class State """
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Test the State class"""

    def test_state_inheritance(self):
        """Test that State inherits from BaseModel"""
        self.assertTrue(issubclass(State, BaseModel))

    def test_state_attributes(self):
        """Test the attributes of State"""
        state = State()
        self.assertTrue(hasattr(state, 'name'))
        self.assertEqual(state.name, "")

    def test_state_to_dict(self):
        """Test the to_dict method of State"""
        state = State()
        state_dict = state.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertEqual(state_dict['__class__'], 'State')
        self.assertIsInstance(state_dict['created_at'], str)
        self.assertIsInstance(state_dict['updated_at'], str)


if __name__ == '__main__':
    unittest.main()
