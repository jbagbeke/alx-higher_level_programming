#!/usr/bin/python3
"""
Checks if an object is an instance of a class or inherited class
"""


def inherits_from(obj, a_class):
    """
    Checks if object is instance of class a_class or inherited class

    Args:
        Arg1: (obj) object in consideration
        Arg2: (a_class) class to compare with obj

    Return: True if obj is an instance, False otherwise
    """

    if type(obj) != a_class) and issubclass(type(obj), a_class):
        return True
    else:
        return False
