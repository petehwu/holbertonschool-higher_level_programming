#!/usr/bin/python3

class MyInt(int):
    """class MyInt definition"""
    def __init__(self, value):
        """init method for MyINt"""
        if not isinstance(value, int):
            raise TypeError("value must be an integer")
        self.value = value

    def __eq__(self, val):
        """overloading the equals method"""
        return not(str(self.value) == str(val))

    def __ne__(self, val):
        """overloading the not equals method"""
        return not(str(self.value) != str(val))
