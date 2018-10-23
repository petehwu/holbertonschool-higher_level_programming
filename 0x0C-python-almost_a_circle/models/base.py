#!/usr/bin/python3
""" base class definition"""
import json


class Base:
    """base class definition"""

    __nb_objects = 0

    def __init__(self, id=None):
        """init method for Base class"""
        if id is None:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
        else:
            self.id = id

    @classmethod
    def save_to_file(cls, list_objs):
        """save string representation of json to file"""
        filename = cls.__name__ + ".json"
        if list_objs is None or list_objs == "":
            list_dict = None
        else:
            list_dict = [obj.to_dictionary() for obj in list_objs]
        with open(filename, mode="w", encoding="utf-8") as wf:
            wf.write(cls.to_json_string(list_dict))

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all the attributes set"""
        if (dictionary is None or not dictionary):
            raise TypeError("dictionary cannot be blank")
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """loads object from file"""
        il = []
        filename = cls.__name__+".json"
        try:
            with open(filename, mode="r", encoding="utf-8") as rf:
                jl = cls.from_json_string(rf.read())
                for d in jl:
                    il.append(cls.create(**d))
                return (il)
        except FileNotFoundError:
            return (il)

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns JSON string representation of list of dictionaries"""
        if list_dictionaries is None or list_dictionaries = []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """convert string of JSON to list of string of JSON"""
        if not json_string:
            return []
        else:
            return json.loads(json_string)
