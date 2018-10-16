#!/usr/bin/python3
import json


def save_to_json_file(my_obj, filename):
    """writes an object to a text file in JSON representation"""
    if not isinstance(filename, str):
        raise TypeError("filename must be a string")
    with open(filename, mode="w", encoding="utf-8") as writeFile:
        json.dump(my_obj, writeFile)
