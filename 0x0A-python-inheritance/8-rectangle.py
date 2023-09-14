#!/usr/bin/python3
"""
Class for geometry calcs
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class that inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """
        Instantiation with width and height
        """

        super().__init__()
        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height
