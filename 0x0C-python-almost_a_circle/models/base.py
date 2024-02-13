#!/usr/bin/python3
"""Base for all other classes"""
import json
import csv
import os


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
        new_instance = cls(**dictionary)
        updated = new_instance.update(**dictionary)
        return (updated)

    @classmethod
    def load_from_file(cls):
        """returns a list of instances
        """
        filename = f"{cls.__name__}.json"
        if not os.path.exists(filename):
            return []
        with open(filename, encoding="utf-8") as f:
            list_input = f.read()
            from_json = Base.from_json_string(list_input)
            list_output = []
            for inst in from_json:
                list_output.append(cls.create(**inst))
            return list_output

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """saves json string to csv file

        Args:
            list_objs (list): list of objects
        """
        filename = f"{cls.__name__}.csv"
        with open(filename, "w", encoding="utf-8", newline='') as f:
            if list_objs is None:
                f.write([])
            else:
                outputWriter = csv.DictWriter(
                    f, list_objs[0].to_dictionary().keys())
                outputWriter.writeheader()
                for li in list_objs:
                    outputWriter.writerow(li.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """loads from csv file
        """
        filename = f"{cls.__name__}.csv"
        list_output = []
        with open(filename, encoding="utf-8", newline='') as f:
            outputReader = csv.DictReader(f)
            for row in outputReader:
                new_instance = cls.create(**{key: int(value)
                                             for key, value in row.items()})
                list_output.append(new_instance)
            return list_output
