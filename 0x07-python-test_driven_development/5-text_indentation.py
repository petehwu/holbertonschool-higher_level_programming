#!/usr/bin/python3
"""This file contains a function that replaces
the .?: charcters with 2 newline characters in a string
"""


def text_indentation(text):
    """This function replaces the .?: character with 2 newline characters

    Args:
        text:  the input text
    """
    strlist = []
    ostr = ""
    ops = [".", "?", ":"]
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    strlist = text.split("\n")
    strlist = [x.lstrip(" ") for x in strlist]
    text = "\n".join(strlist)
    for o in ops:
        strlist = text.split(o)
        ostr = o+"\n\n"
        strlist = [x.lstrip(" ") for x in strlist]
        text = ostr.join(strlist)
    print("{:s}".format(text.rstrip(" ")), end="")

