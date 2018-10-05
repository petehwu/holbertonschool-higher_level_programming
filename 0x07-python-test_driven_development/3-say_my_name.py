#!/usr/bin/python3
"""This file contains the say_my_name function
"""


def say_my_name(first_name, last_name=""):
    """say_my_name function.  This function will
    print the firstname and lastname in the input

    Args:
       first_name: first name to print
       last_name: last name to print
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
