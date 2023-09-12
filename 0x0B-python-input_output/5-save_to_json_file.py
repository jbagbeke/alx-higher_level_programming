#!/usr/bin/python3
"""
Writes object to text file using JSON representation
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Writes obj to text file using JSON rep

    Args:
        Arg1: (my_obj) object to write
        Arg2: File to store object rep in JSON
    """

    with open(filename, "a", encoding="UTF-8") as file:
        json.dump(my_obj, file)
