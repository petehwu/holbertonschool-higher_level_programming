#!/usr/bin/python3
class Square:
    """Represents a square """
    def __init__(self, size=0):
        """Init method to initialize a square with a size"""
        if not (isinstance(size, int)):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """calculates area and return"""
        return self.__size * self.__size
