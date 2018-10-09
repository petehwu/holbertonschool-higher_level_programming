#!/usr/bin/python3

class Rectangle:
    """Rectangle class to represent a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

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
        if self.area() == "":
            return ""
        else:
            rect_list = [ ("%s" % (self.print_symbol) * self.width)\
for i in range(self.height)]
            return "\n".join(rect_list)

    def __repr__(self):
        """return a string representation of the rectangle"""
        return self.__class__.__name__ + "(" +\
str(self.width) + ", " + str(self.height) + ")"
    
    def __del__(self):
        """destructor method"""
        type(self).number_of_instances -= 1
        print ("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        """compares area of rect_1 to rect_2 and return the bigger one"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """creates a square rectangle"""
        return cls(size, size)
