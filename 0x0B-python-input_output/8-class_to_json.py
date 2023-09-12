#!/usr/bin/python3
"""
Returns the dictionary description with simple data structure
"""


def class_to_json(obj):
    """
    Returns the dictionary description

    Args:
        arg1: (obj) object to 'dictionalise'
    Return: Dictionary description of obj
    """

    return (obj.__dict__)
