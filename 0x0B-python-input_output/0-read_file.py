#!/usr/bin/python3
"""
READS A TEXT FILE AND PRINTS TO STDOUT
"""


def read_file(filename=""):
    """
    Reads a text file and prints to stdout
    """

    with open(filename, encoding='UTF-8') as file:
        print(file.read())
