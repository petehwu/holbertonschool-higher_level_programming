#!/usr/bin/python3


def write_file(filename="", text=""):
    """"writes text to a file and return number of bytes written"""
    if not isinstance(filename, str):
        raise TypeError("filename must be a string")
    with open(filename, mode="w", encoding="utf-8") as writeFile:
        return(writeFile.write(str(text)))
