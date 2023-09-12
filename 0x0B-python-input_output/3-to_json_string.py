#!/usr/bin/python3
"""
Returns JSON representation of object
"""

import pickle


def to_json_string(my_obj):
    """
    Returns object representation in JSON

    Args:
        Arg1: (my_obj) object to serialize

    Return: JSON rep of my_obj
    """

    return (pickle.dumps(my_obj))
