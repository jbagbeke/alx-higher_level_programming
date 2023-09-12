#!/usr/bin/python3
"""
A class that inherits from a list
"""


class MyList(list):
    """
    Class to inherit from list
    """

    def __int__(self):
        """ Initialises list of parent class """

        super().__init__()

    def print_sorted(self):
        """ Prints the list of class but sorted """

        print(sorted(self))
