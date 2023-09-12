#!/usr/bin/python3
"""
Creates object from json file
"""


import json


def load_from_json_file(filename):
    """
    Creates obj from JSON file
    
    Args:
        Arg1: (filename) file to create object from
    """

    with open(filename, "r", encoding="UTF-8") as file:
        my_object = json.load(file)
