#!/usr/bin/python3
""" City class that inherits from BaseModel. """


from models.base_model import BaseModel


class City(BaseModel):
    """
    City class that inherits from BaseModel.
    Public class attributes:
    - state_id: string (empty string by default, it will be the State.id)
    - name: string (empty string by default)
    """
    state_id = ""
    name = ""
