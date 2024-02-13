#!/usr/bin/python3
"""Base for all other classes"""
import json


class Base:
    """Base for all other classes. The goal is to manage
    id attribute all your future classes and to avoid duplicating the
    same code (by extension, same bugs)"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries

        Args:
            list_dictionaries (list): a list of dictionaries
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file

        Args:
            list_objs (list): list of instances who inherits of Base
        """
        with open(f"{cls.__name__}.json", "w", encoding="utf-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                f.write(cls.to_json_string([ls.to_dictionary()
                                            for ls in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string

        Args:
            json_string (json): json string
        """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set
        """
        new_instance = cls(2, 2)
        updated = new_instance.update(**dictionary)
        return (updated)
