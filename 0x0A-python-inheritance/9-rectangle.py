#!/usr/bin/python3


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class inherits form BaseGeometry"""

    def __init__(self, width, height):
        """init method for rectangle class"""

        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """calculates area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """format for printing"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
