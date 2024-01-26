#!/usr/bin/python3
"""
contains add_integer function

to add integer to 98 or add two integers
"""


def add_integer(a, b=98):
    """
    add integer to 98 or add two integers
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
