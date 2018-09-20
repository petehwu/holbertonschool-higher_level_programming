#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        return None
    return [[row[i] * row[i] for i in range(len(row))] for row in matrix]
