#!/usr/bin/python3
"""rectangle class definition"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class definition"""

    def __init__(self, size, x=0, y=0, id=None):
        """init method for Square class"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter for size"""
        return self.width

    @size.setter
    def size(self, val):
        """setter for size of square"""
        self.width = val
        self.height = val

    def update(self, *args, **kwargs):
        """ updates attributes in the object"""
        l1 = ['id', 'size', 'x', 'y']
        if (args and len(args) < 5 and args[0] is not None and args[0] != ""):
            for idx, val in enumerate(args):
                setattr(self, l1[idx], val)
        else:
            for key, val in kwargs.items():
                setattr(self, key, val)

    def to_dictionary(self):
        temp_dict = {}
        temp_dict['id'] = self.id
        temp_dict['size'] = self.size
        temp_dict['x'] = self.x
        temp_dict['y'] = self.y
        return temp_dict
