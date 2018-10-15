#!/usr/bin/python3


class BaseGeometry():
    """BaseGeometry class"""

    def area(self):
        """place holder for area calculation"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value is integer and >= 0 """
        if type(value) != int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
