#!/usr/bin/python3
""" this module contains function is_kind_of_class that
returns True if the object is an instance of, or if the
object is an instance of a class that inherited from,
the specified class; otherwise false
"""


def is_kind_of_class(obj, a_class):
    """returns True if the object is an instance of, or if the
    object is an instance of a class that inherited from,
    the specified class; otherwise false"""
    return (isinstance(obj, a_class))
