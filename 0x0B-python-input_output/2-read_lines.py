#!/usr/bin/python3


def read_lines(filename="", nb_Lines=0):
    """Read nb_lines from file and print"""
    if not isinstance(filename, str):
        raise TypeError("filename must be a string")
    ctr = 0
    with open(filename, mode="r", encoding="utf-8") as theFile:
        for line in theFile:
            print(line, end="")
            nb_Lines -= 1
            if nb_Lines == 0:
                break
