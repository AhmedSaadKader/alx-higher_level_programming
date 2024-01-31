#!/usr/bin/python3
"""
This module contains print_square() function

It prints a square with the character #
"""


def print_square(size):
    """
	It prints a square with the character #
    """
    if (not isinstance(size, int)):
        raise TypeError("size must be an integer")
    if (size < 0):
        raise ValueError("size must be >= 0")
    for _ in range(size):
        for i in range(size):
            print("#", end="")
        print()
