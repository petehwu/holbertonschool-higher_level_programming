#!/usr/bin/python3
class Square:
    """Represents a square """
    def __init__(self, size=0):
        """Init method to initialize a square with a size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """calculates area and return"""
        return self.__size * self.__size

    @property
    def size(self):
        """getter for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter for size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """prints out a square"""
        if self.__size == 0:
            print()
        for i in range(self.__size):
            print("#" * self.__size)
