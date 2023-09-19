#!/usr/bin/pythonw3
"""Defines class Amenity"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class inheriting from BaseModel
    Attributes:
        name (str): name of the amenity
    """
    name = ""
