#!/usr/bin/python3


def number_of_lines(filename=""):
    """counts number of lines in a file and returns the value"""
    if not isinstance(filename, str):
        raise TypeError("filename must be a string")
    ctr = 0
    with open(filename, mode="r", encoding="utf-8") as theFile:
        for line in theFile:
            ctr += 1
    return (ctr)
