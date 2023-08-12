#!/usr/bin/python3
""" A class BaseModel that defines all common attribute/methods """
import uuid
from datetime import datetime


class BaseModel:
    """
    BaseModel class with public instance attributes and
    methods for serialization/deserialization.
    """

    def __init__(self):
        """
        Initializes a new instance of BaseModel.
        """
        # Generate a unique ID and convert to string
        self.id = str(uuid.uuid4())
        # Set the creation timestamp
        self.created_at = datetime.now()
        # Initialize updated_at with creation timestam
        self.updated_at = self.created_at

    def __str__(self):
        """
        Returns a string representation of the instance.
        Example: "[<class name>] (<self.id>) <self.__dict__>"
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """
        Updates the public instance attribute
        updated_at with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values
        of __dict__ of the instance.
        - A key "__class__" is added with the class name of the object.
        - created_at and updated_at are converted to
        string objects in ISO format.
        """
        # Copy the instance dictionary
        obj_dict = self.__dict__.copy()
        # Add class name
        obj_dict['__class__'] = self.__class__.__name__
        # Convert to ISO format
        obj_dict['created_at'] = self.created_at.isoformat()
        # Convert to ISO format
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
