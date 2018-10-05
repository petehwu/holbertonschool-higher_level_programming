#!/usr/bin/python3
"""This file has a function that will divide all elements in the
matrix by the spedificed number
"""


def matrix_divided(matrix, div):
    """This function will divide all numbers in the
    matrix by the value div

    Args:
        matrix: list of lists
        div: number to divide by
    Return:
        the result matrix after each value has been divided
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    if not matrix or not all(isinstance(l, list) for l in matrix):
        raise TypeError("matrix must be a matrix (\
list of lists) of integers/floats")
    nl = list(map(len, matrix))
    m2 = []
    mtemp = []
    res = 0
    if not all(l == nl[0] for l in nl):
        raise TypeError("Each row of the matrix must have the same size")
    for row in matrix:
        for val in row:
            if not isinstance(val, (int, float)):
                raise TypeError("matrix must be a matrix\
(list of lists) of integers/floats")
            else:
                res = val / div
                res = round(res, 2)
                mtemp.append(res)
        m2.append(mtemp)
        mtemp = []
    return m2
