#!/usr/bin/python3
"""Defines class City"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Represents a city
    
    Attributes:
        state_id (str): The state id
        name (str): The name
    """
    
    state_id = ""
    name = ""