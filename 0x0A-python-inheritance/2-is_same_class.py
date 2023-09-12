#!/usr/bin/python3
"""
Checks if an obect is an instance of a class
"""


def is_same_class(obj, a_class):
    """
    Checks if obect is instance of class a_class
    
    Args:
        Arg1: (obj) object in consideration
        Arg2: (a_class) class to compare with obj

    Return: True if obj is an instance, False otherwise
    """

    if type(obj) != a_class:
        return False
    else:
        return True
