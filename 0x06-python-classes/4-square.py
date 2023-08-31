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

        Args: An int for assignment
        """
        self.__size = size

    def size(self):
        """
        Retrieves original value used for calculating the area
        """
        return self.__size

    def self(self, value):
        """
        Instantiation and checks for valid input
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Returns area of a square
        """
        return self.__size ** 2
