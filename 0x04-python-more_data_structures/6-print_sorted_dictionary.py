#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is None:
        return None
    keys = list(a_dictionary.keys())
    keys.sort()
    for keyval in keys:
        print("{}: {}".format(keyval, a_dictionary[keyval]))
