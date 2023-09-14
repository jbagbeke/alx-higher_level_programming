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
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


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

    def area(self):
        """
        Raises an exception
        """

        return self.__height * self.__width

    def __str__(self):
        """
        Prints to stdout/ Runs when print() is called
        """

        return str(("[Rectangle] {}/{}".format(self.__width, self.__height)))


class Square(Rectangle):
    """
    Inherits from Rectanlge class
    """

    def __init__(self, size):
        """
        Instantiation with size
        """

        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size
