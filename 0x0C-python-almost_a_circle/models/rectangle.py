#!/usr/bin/python3
"""rectangle class definition"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class inherits from Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """init method for Rectangle class"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @property
    def x(self):
        """getter for x"""
        return self.__x

    @property
    def y(self):
        """getter for y"""
        return self.__y

    @width.setter
    def width(self, val):
        """setter for width"""
        if not isinstance(val, int):
            raise TypeError("width must be an integer")
        if val <= 0:
            raise ValueError("width must be > 0")
        self.__width = val

    @height.setter
    def height(self, val):
        """setter for height"""
        if not isinstance(val, int):
            raise TypeError("height must be an integer")
        if val <= 0:
            raise ValueError("height must be > 0")
        self.__height = val

    @x.setter
    def x(self, val):
        """setter for x"""
        if not isinstance(val, int):
            raise TypeError("x must be an integer")
        if val < 0:
            raise ValueError("x must be >= 0")
        self.__x = val

    @y.setter
    def y(self, val):
        """setter for y"""
        if not isinstance(val, int):
            raise TypeError("y must be an integer")
        if val < 0:
            raise ValueError("y must be >= 0")
        self.__y = val

    def area(self):
        """method to calculate area"""
        return self.width * self.height

    def display(self):
        """method to draw rectangle"""
        print("\n" * self.y, end="")
        for row in range(self.height):
            print(" " * self.x, end="")
            for col in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """method to format string for printing"""
        thestr = "[{:s}] ({:s}) {:d}/{:d} - ".\
                 format(type(self).__name__, str(self.id), self.x, self.y)
        if (type(self) == Rectangle):
            thestr += "{:d}/{:d}".format(self.width, self.height)
        else:
            thestr += "{:d}".format(self.width)
        return thestr

    def update(self, *args, **kwargs):
        """update values in object to specified values"""
        l1 = ['id', 'width', 'height', 'x', 'y']
        if (args and len(args) < 6 and args[0] is not None and args[0] != ""):
            for idx, val in enumerate(args):
                setattr(self, l1[idx], val)
        else:
            for key, val in kwargs.items():
                setattr(self, key, val)

    def to_dictionary(self):
        """make dictionary with instance attributes"""
        temp_dict = {}
        temp_dict['id'] = self.id
        temp_dict['width'] = self.width
        temp_dict['height'] = self.height
        temp_dict['x'] = self.x
        temp_dict['y'] = self.y
        return temp_dict
