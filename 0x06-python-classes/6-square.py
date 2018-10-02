#!/usr/bin/python3
class Square:
    """Represents a square """
    def __init__(self, size=0, position=(0, 0)):
        """Init method to initialize a square with a size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size
        if (len(position) != 2 or
                not all(isinstance(i, int) for i in position) or
                not all(i >= 0 for i in position)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        """calculates area and return"""
        return self.__size * self.__size

    @property
    def position(self):
        """getter for position"""
        return self.__position

    @position.setter
    def position(self, pos):
        """setter for position"""
        if (len(position) != 2 or
                not all(isinstance(i, int) for i in position) or
                not all(i >= 0 for i in position)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

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
        """prints out a square with some additional spaces and blank lines"""
        print("\n" * self.__position[1], end="")
        if self.__size == 0:
            print()
        for i in range(self.__size):
            print("{}{}".format(" " * self.__position[0],
                  "#" * self.__size))
