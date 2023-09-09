#!/usr/bin/python3

"""
Divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    Divides each element of a matrix and rounds to 2 d.p

    Args:
        Arg1: A matrix with a list of lists(matrix)
        Arg2: What to divide each element with(div)

    Returns:
        A new matrix with result of division
    """
    err1 = "matrix must be a matrix (list of lists) of integers/floats"
    err2 = "Each row of the matrix must have the same size"

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if isinstance(matrix, list):
        for mat1 in matrix:
            if not isinstance(mat1, list):
                raise TypeError(err1)
            for pint in mat1:
                if not isinstance(pint, int) and not isinstance(pint, float):
                    raise TypeError(err1)

        for i in range(len(matrix)):
            if i + 1 < len(matrix):
                len1 = len(matrix[i])
                len2 = len(matrix[i + 1])
                if len1 != len2:
                    raise TypeError(err2)

    new_matrix = []
    for mat_rix in matrix:
        temp_mat = []
        for index in range(len(mat_rix)):
            copy_mat = mat_rix.copy()
            copy_mat[index] = round((copy_mat[index] / div), 2)
            temp_mat.append(copy_mat[index])
        new_matrix.append(temp_mat)

    return (new_matrix)
