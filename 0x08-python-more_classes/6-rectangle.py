#!/usr/bin/python3

class Rectangle:
    """Rectangle class to represent a rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """init method"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @width.setter
    def width(self, value):
        """setter for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value 

    @height.setter
    def height(self, value):
        """setter for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of a rectangle"""
        return self.width * self.height

    def perimeter(self):
        """returns the perimeter of a rectangle"""
        if self.area() == 0:
            return 0
        else:
            return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """format rectangle for printing"""
        if self.area() == 0:
            return ""
        else:
            rect_list = [("#" * self.width) for i in range(self.height)]
            return "\n".join(rect_list)

    def __repr__(self):
        """return a string representation of the rectangle"""
        return self.__class__.__name__ + "(" +\
str(self.width) + ", " + str(self.height) + ")"
    
    def __del__(self):
        """destructor method"""
        type(self).number_of_instances -= 1
        print ("Bye rectangle...")
