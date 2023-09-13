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

    def to_json(self):
        """
        Returns the dictionary description
        """

        return (self.__dict__)
