#!/usr/bin/python3
"""The module creates an Userclass"""

from models.base_model import BaseModel


class City(BaseModel):
    """Class for managing city objects"""

    state_id = ""
    name = ""
