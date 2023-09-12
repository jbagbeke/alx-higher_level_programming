#!/usr/bin/python3
"""
READS A TEXT FILE AND PRINTS TO STDOUT
"""


def read_file(filename=""):
    """
    Reads a text file and prints to stdout
    """

    with open(filename, 'r', encoding='UTF-8') as file:
        print("{}".format(file.read()), end='')
