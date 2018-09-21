#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary is None or not a_dictionary:
        return None
    keys = []
    for key in a_dictionary:
        if a_dictionary[key] == value:
            keys.append(key)
    for k in keys:
        a_dictionary.pop(k)
    return a_dictionary
