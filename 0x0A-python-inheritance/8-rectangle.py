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

class Rectangle(BaseGeometry):
    """
    Instantiation with width and height
    """

    def __init__(self, width, height):
        self.__width = 0
        self.__height = 0
        super.__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
