#!/usr/bin/python3
"""
Returns an object represented by a JSON string
"""


import json


def from_json_string(my_str):
    """
    Returns an object represented by a JSON string

    Args:
        Arg1: (my_str) string to deserialize

    Return: Obect repped by a JSON string
    """

    return (json.loads(my_str))
