#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """ returns if obj is either a_class or inherited from a_class """
    return isinstance(obj, a_class)
