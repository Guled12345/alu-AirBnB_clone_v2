#!/usr/bin/python3
"""Class User inheriting from BaseModel"""
from models.base_model import BaseModel


class user(BaseModel):
    """Represnt a user"""
    
    email = ""
    password = ""
    first_name = ""
    last_name = ""