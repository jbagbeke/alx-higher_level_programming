#!/usr/bin/python3
"""
Appends a string to end of text file
"""


def append_write(filename="", text=""):
    """
    Appends a string to end of text file and returns # of chars added

    Args:
        Arg1: (filename) file to store string
        Arg2: (text) string to append to text file

    Return: # of chars added
    """

    with open(filename, 'a', encoding='UTF-8') as file:
        char_read = file.append(text)

    return char_read
