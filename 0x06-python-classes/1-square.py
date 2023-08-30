#!/usr/bin/python3
"""
    Purpose: A definition of a class 'Square' with a private instance 'size'
"""


class Square:
    """
    Class with an instantiation attribut 'size'.
    """
    def __init__(self, num=390):
        """
        Instantiation with a private attribute 'size'
        """
        self.__size = num
