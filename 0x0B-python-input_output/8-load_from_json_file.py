#!/usr/bin/python3
import json


def load_from_json_file(filename):
    """creates an object from JSON file"""
    if not isinstance(filename, str):
        raise typeError("filename must be a string")
    with open(filename, mode="r", encoding="utf-8") as readFile:
        return(json.load(readFile))
