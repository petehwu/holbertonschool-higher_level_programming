#!/usr/bin/python3


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class definition"""

    def __init__(self, size):
        """init method for square"""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """area calculation for Square"""
        return self.__size ** 2

    def __str__(self):
        """format for printing"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)

    def print(self):
        print(self.__str__())
