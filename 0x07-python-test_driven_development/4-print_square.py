#!/usr/bin/python3
"""This file contains a function that will print out a
square given a size
"""


def print_square(size):
    """This function will print out a square using # for the given size

    Args:
        size: positive integer of size of square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for r in range(size):
        print("{:s}".format("#" * size))
