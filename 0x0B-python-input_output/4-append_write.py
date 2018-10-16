#!/usr/bin/python3


def append_write(filename="", text=""):
    """appends a string to the end of a file and
       return number of character appended
    """
    if not isinstance(filename, str):
        raise TypeError("filename must be a string")
    with open(filename, mode="a", encoding="utf-8") as appendFile:
        return(appendFile.write(str(text)))
