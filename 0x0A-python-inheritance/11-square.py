#!/usr/bin/python3
"""
Class for geometry calcs
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Inherits from Rectangle class
    """

    def __init__(self, size):
        """
        Instantiation with size
        """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        Returns str representation of deisred output
        """

        return (str("[Square] {}/{}".format(self.__size, self.__size)))
