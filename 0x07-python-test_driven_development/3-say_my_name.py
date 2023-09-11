#!/usr/bin/python3

"""
Prints name of a user
"""


def say_my_name(first_name, last_name=""):
    """
    Prints name of user

    Args:
        Arg1: Firstname of user
        Arg2: Lastname of user

    Return: None
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
