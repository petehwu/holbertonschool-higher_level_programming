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
    ops = [".", "?", ":"]
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    for o in ops:
        text = text.replace(o, o+"\n")
    strlist = text.split("\n")
    strlist = [x for x.strip(" ") in strlist]
    print("{}".format("\n\n".join(strlist)), end="")
