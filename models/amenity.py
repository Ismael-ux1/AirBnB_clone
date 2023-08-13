#!/usr/bin/python3
""" Amenity class that inherits from BasseModel. """

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class that inherits from BaseModel.
    Public class attributes:
    - name: string (empty string by default)
    """
    name = ""
