#!/usr/bin/python3
"""
Adds two integers and returns result of summation
"""


def add_integer(a, b=98):
    """
    Adds two integers and returns result

    Args:
    param1 (a): First number to be added
    param2 (b): Second number to be added

    Returns: Result of summation(Int)
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)


print(add_integer(2.3, -4.1))
