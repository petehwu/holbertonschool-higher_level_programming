#!/usr/bin/python3


def read_file(filename=""):
    """reads a file and prints to screen"""
    if not isinstance(filename, str):
        raise TypeError("filename must be a string")
    with open(filename, mode="r", encoding="utf-8") as theFile:
        for line in theFile:
            print(line, end="")
