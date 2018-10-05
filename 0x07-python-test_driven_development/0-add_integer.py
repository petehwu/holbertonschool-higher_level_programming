#!/usr/bin/python3
"""This file contains the add_integer function used to
add 2 integers together
"""


def add_integer(a, b=98):
    """function to add 2 integers together

    Args:
        a (int): First number to add
        b (int): Seconde number to add

    Returns:
        int: The sum of a and b
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
