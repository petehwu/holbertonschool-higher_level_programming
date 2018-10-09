#!/usr/bin/python3
class LockedClass:
    def __setattr__(self, key, value):
        if key != 'first_name':
            raise AttributeError("%r object has no attribute %r"
                                 % (self.__class__.__name__, key))
        object.__setattr__(self, key, value)
