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
        self.size = size

    def size(self):
        """
        Retrieves original value used for calculating the area
        """
        retrieved = self.__size
        return retrieved

    def self(self, value):
        """
        Instantiation and checks for valid input
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer\n")
        if value < 0:
            raise ValueError("size must be >= 0\n")
        self.__size = value

    def area(self):
        """
        Returns area of a square
        """
        result = self.__size ** 2
        return result
