#!/usr/bin/python3
"""class Student that defines a student"""


class Student:
    """class Student that defines a student
    """
    def __init__(self, first_name, last_name, age):
        """initialize a new student

        Args:
            first_name (str): first name
            last_name (str): first name
            age (int): age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of self
        """
        if isinstance(attrs, list) and all(
                isinstance(item, str) for item in attrs):
            return {key: value for key, value in self.__dict__.items()
                    if key in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance

        Args:
            json (dict): dictionary containing the attributes
        """
        self.first_name = json.get('first_name', None)
        self.last_name = json.get('last_name', None)
        self.age = json.get('age', None)
