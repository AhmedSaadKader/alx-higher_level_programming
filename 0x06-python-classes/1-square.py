#!/usr/bin/python3

"""This module contains a class that creates a square"""


class Square:
    """creates a square
    Attributes:
        size: private attribute representing the size of the
        square
    """
    def __init__(self, size) -> None:
        self.__size = size
