#!/usr/bin/python3
"""
this module contains one function lookup
this function returns the list of available
attributes and methods of an object
"""


def lookup(obj):
    """
    this function returns the list of available
    attributes and methods of an object
    """
    return dir(obj)
