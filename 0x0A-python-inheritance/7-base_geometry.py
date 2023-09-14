#!/usr/bin/python3
"""
Class for geometry calcs
"""


class BaseGeometry:
    """
    Class with geometry attributes
    """

    def area(self):
        """
        Raises an exception
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates value
        """

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(value))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(value))
