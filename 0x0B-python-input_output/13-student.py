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
        if age < 0:
            raise ValueError("age must not be negative")
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of student object"""
        if (attrs is None or not all(isinstance(key, str) for key in attrs)):
            return(dict(vars(self)))
        else:
            temp = dict()
            for key in attrs:
                try:
                    val = getattr(self, key)
                    temp[key] = val
                except AttributeError:
                    continue
            return(temp)

    def reload_from_json(self, json):
        """ replaces all attributes of the student instance"""
        for key, val in json.items():
            setattr(self, key, val)
