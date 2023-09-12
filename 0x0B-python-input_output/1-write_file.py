#!/usr/bin/python3
"""
Writes a string to text file
"""


def write_file(filename="", text=""):
    """
    Writes a file to a text file and returns # of chars written

    Args:
        Arg1: (filename) file to store string
        Arg2: (text) string to write to text file

    Return: # of chars read
    """

    with open(filename, 'w', encoding='UTF-8') as file:
        file.write(text)
