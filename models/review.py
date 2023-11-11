#!/usr/bin/python3
""" state class """
from models.base_model import BaseModel


class Review(BaseModel):
    """
    initializing Review class
    """

    place_id = ""
    user_id = ""
    text = ""
