#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if isinstance(matrix, list):
        for i in range(len(matrix)):
            if isinstance(matrix[i], list):
                for j in matrix[i]:
                    print("{:d}".format(j), end=" ")
                print()
