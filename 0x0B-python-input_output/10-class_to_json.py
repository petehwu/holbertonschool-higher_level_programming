#!/usr/bin/python3


def class_to_json(obj):
    """returns the dictionary description for JSON"""
    return dict(vars(obj))
