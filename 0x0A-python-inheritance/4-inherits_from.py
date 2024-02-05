#!/usr/bin/python3
""" This module contains function inherits_from
that returns True if the object is an instance of
a class that inherits (directly or indirectly)
from the specified class; otherwise false
"""


def inherits_from(obj, a_class):
    """
    that returns True if the object is an instance of
    a class that inherits (directly or indirectly)
    from the specified class; otherwise false
    """
    return (issubclass(type(obj), a_class))
