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
    max_len = 1e-10
    if len([a, b]) not in (1, 2):
        raise TypeError("Invalid number of arguments passed")
    if not isinstance(a, int) and isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(a, int) and isinstance(b, float):
        raise TypeError("b must be an integer")
    if (a + 1 - a) < max_len or (b + 1 - b) < max_len:
        raise ValueError("Integer value too large")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return (a + b)


print(add_integer(, 89))
