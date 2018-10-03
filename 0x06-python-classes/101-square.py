#!/usr/bin/python3
class Square:
    """Represents a square """
    def __init__(self, size=0, position=(0, 0)):
        """Init method to initialize a square with a size"""
        self.size = size
        self.position = position

    def area(self):
        """calculates area and return"""
        return self.__size * self.__size

    @property
    def position(self):
        """getter for position"""
        return self.__position

    @position.setter
    def position(self, value):
        """setter for position"""
        if (len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
        for i in range(self.__size):
            print("{}{}".format(" " * self.__position[0],
                  "#" * self.__size))

    def __str__(self):
        """format for printing"""
        tempstr = ""
        templist = []
        if self.__size == 0:
            tempstr = ""
        else:
            for i in range(self.__size):
                templist.append( "{}{}".format(" " * self.__position[0],
                                               "#" * self.__size))
            tempstr = "\n" * self.__position[1] + "\n".join(templist)
            return tempstr
