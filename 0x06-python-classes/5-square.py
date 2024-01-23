#!/usr/bin/python3

"""contains a class Square that defines a square"""


class Square:
    """defines a square"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print("")
        for height in range(self.__size):
            for width in range(self.__size):
                print("#", end="")
            print()
