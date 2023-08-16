#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if isinstance(matrix, list):
        m_len = len(matrix)
        new_matrix = []

        for index in range(m_len):
            id_len = len(matrix[index])
            mat_rix = matrix[index].copy()

            for idx in range(id_len):
                mat_rix[idx] **= 2
            new_matrix.append(mat_rix)

        return (new_matrix)
