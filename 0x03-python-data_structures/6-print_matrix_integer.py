#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for idx, val in enumerate(row):
            print("{:d}".format(val), sep=" ", end="")
            if (idx < len(row) - 1):
                print(" ", end="")
        print()
