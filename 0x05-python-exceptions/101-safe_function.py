#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    try:
        res = fct(*args)
    except Exception as e:
        res = None
        print("Exception: {:s}".format(str(e)), file=stderr)
    finally:
        return res
