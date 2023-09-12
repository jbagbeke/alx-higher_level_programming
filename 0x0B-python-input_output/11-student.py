#!/usr/bin/python3
"""
Defines a student class with public instance variables
"""


class Student:
    """
    Instantiates student class with instance vars
    """

    def __init__(self, first_name, last_name, age):
        """
        Student public method with instantiation
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns the dictionary description
        """
        if attrs is None:
            return self.__dict__

        new_self = {}
        for att in attrs:
            if att in self.__dict__:
                new_self[att] = self.__dict__[att]
        return (new_self)

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance

        Arg1: (json) dictionary with keys and their respective values
        """

        for key, val in json.items():
            setattr(self, key, val)
