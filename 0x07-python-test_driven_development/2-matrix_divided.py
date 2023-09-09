#!/usr/bin/python3
"""Divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """
    Divides each element of a matrix and rounds to 2 d.p

    Args:
        Arg1: A matrix with a list of lists(matrix)
        Arg2: What to divide each element with(div)

    Returns:
        A new matrix with result of division
    """

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if isinstance(matrix, list):
        for mat1 in matrix:
            if not isinstance(mat1, list):
                err = "matrix must be a matrix (list of lists) of integers/floats" 
                raise TypeError(err)
            for is_int in mat1:
                if not isinstance(is_int, int):
                    raise TypeError(err)
                if and not isinstance(is_int, float):
                    raise TypeError(err)

        for i in range(len(matrix)):
            if i + 1 < len(matrix):
                len1 = len(matrix[i])
                len2 = len(matrix[i + 1])
                if len1 != len2:
                    err = "Each row of the matrix must have the same size"
                    raise TypeError(err)

    new_matrix = []
    for mat_rix in matrix:
        temp_mat = []
        for index in range(len(mat_rix)):
            copy_mat = mat_rix.copy()
            copy_mat[index] = round((copy_mat[index] / div), 2)
            temp_mat.append(copy_mat[index])
        new_matrix.append(temp_mat)

    return (new_matrix)
