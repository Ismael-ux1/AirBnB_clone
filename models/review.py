#!/usr/bin/python3
""" Review class that inherits from BaseModel. """

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class that inherits from BaseModel.
    Public class attributes:
    - place_id: string (empty string by default, it will be the Place.id)
    - user_id: string (empty string by default, it will be the User.id)
    - text: string (empty string by default)
    """
    place_id = ""
    user_id = ""
    text = ""
