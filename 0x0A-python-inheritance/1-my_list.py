#!/usr/bin/python3
"""
This module contains my_list function that inherits from list class -
public instance method: def print_sorted(self) that prints the list but
sorted. All the elements of the list will be of type int
"""


class MyList(list):
    """inherits from list class
    has public instance method: def print_sorted that
    prints the list sorted
    """
    def print_sorted(self):
        print(sorted(self))
