#!/usr/bin/python3
"""
A class module that wil be the base of other classes
"""
import json

class Base:
    """
    Base class of other classes in this project
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialises id of a class if not None

        Args:
            Arg1: (id) An int representing the id of the instance/object
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries
        """

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return str([])

        return json.dumps(list_dictionaries)
