#!/usr/bin/python3
"""
Purpose: A class definition with instantiation and assignment of integers
"""


class Square:
    """
    Assigns an integer to a private instance attibute
    """
    def __init__(self, size=0):
        """
        Instantiation with private 'size' attribute, and checks for valid input
        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def __getattr__(self, name):
        """
        Gets the name of attribute being assessed of the object
        """
        if name == 'size':
            raise AttributeError("'Square' object has no attribute 'size'")
        if name == '__size':
            raise AttributeError("'Square' object has no attribute '__size'")

        def area(self):
            """
            Returns area of a square
            """
            result = self._Square__size ** 2
            return result
