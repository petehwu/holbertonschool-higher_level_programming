#!/usr/bin/python3


class Student():
    """Student class definition"""

    def __init__(self, first_name, last_name, age):
        """init method for Student class"""

        if age < 0:
            raise ValueError("age cannot be negative")
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of student object"""
        return(dict(vars(self)))
