#!/usr/bin/python3
"""
Returns a list of lists of integers representing the Pascal’s triangle
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal’s triangle

    Arg1: (n) number of steps of Pascals triangle to represent
    """

    if n <= 0:
        return []

    pascal = [[1]]
    while len(pascal) != n:
        p_tmp = [1]
        pas = pascal[-1]
        for i in range(len(pas) - 1):
            p_tmp.append(pas[i] + pas[i + 1])
        p_tmp.append(1)
        pascal.append(p_tmp)
    return (pascal)
