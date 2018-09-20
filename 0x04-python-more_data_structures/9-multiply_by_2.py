#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newdict = dict(a_dictionary.items())
    keys = list(newdict.keys())
    for k in keys:
        newdict[k] = newdict[k] * 2
    return newdict
