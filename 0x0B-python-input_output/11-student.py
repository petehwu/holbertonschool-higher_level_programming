#!/usr/bin/python3


class Student():
    """Student class definition"""

    def __init__(self, first_name, last_name, age):
        """init method for Student class"""

        if not isinstance(first_name, str):
            raise TypeError("first_name must be a string")
        if not isinstance(last_name, str):
            raise TypeError("last_name must be a string")
        if not isinstance(age, (int, float)):
            raise TypeError("age must be numeric")
        if age <= 0:
            raise ValueError("age must be greater than 0")
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of student object"""
        return(dict(vars(self)))
