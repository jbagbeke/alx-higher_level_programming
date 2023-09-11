#!/usr/bin/python3
"""
Returns list of available attributes and methods
"""


def lookup(obj):
    """
    Returns list of available attributes and methods of an object

    Args:
        Arg1: (obj) Object whose list of attributes and methods are to be returned

    Return: List of available attributes and methods of an object
    """
    return dir(obj)
