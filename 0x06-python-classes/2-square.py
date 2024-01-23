#!/usr/bin/python3

"""Contains a class that defines a square"""


class Square:
    """creates a square"""
    def __init__(self, size=0):
        self.set_size(size)

    def get_size(self):
        return self.__size

    def set_size(self, size):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
