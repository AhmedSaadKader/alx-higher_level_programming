#!/usr/bin/python3
"""
This module contains function is_same_class
This function returns True if the object is
exactly an instance of the specified class.
"""


def is_same_class(obj, a_class):
    """This function returns True if the object is
    exactly an instance of the specified class."""
    return (type(obj).__name__ == a_class.__name__)
