#!/usr/bin/python3

"""
    An empty class that defines a rectangle
"""


class Rectangle:
    """
    Defines a rectangle and attributes
    """

    def __init__(self, width=0, height=0):
        """
        Instantiates the attributes of a rectangle
        Args 1: An int(width)
        Args 2: An int(height)
        """
        if width < 0 or height < 0:
            raise ValueError
        if not isinstance(width, int) or not isinstance(height, int):
            raise TypeError
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        Retrieves the width of a rectangle
        Args: None
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the value of the width of a rectangle
        Args: An int
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieves the height of a rectangle
        Args: None
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the value of the height of a rectangle
        Args: An int
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
