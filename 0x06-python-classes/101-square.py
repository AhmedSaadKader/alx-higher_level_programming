#!/usr/bin/python3
"""contains a class Square that defines a square"""


class Square:
    """defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    def __str__(self):
        print_string = ""
        if self.__size == 0:
            return print_string
        else:
            for _ in range(self.__position[1]):
                print_string += "\n"
            for height in range(self.__size):
                for _ in range(self.__position[0]):
                    print_string += " "
                for width in range(self.__size):
                    print_string += "#"
                if height != self.__size - 1:
                    print_string += "\n"
            return print_string

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        if (
            not isinstance(position, tuple) or
            len(position) != 2 or
            not all(isinstance(i, int) and i >= 0 for i in position)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__position[1]):
                print()
            for height in range(self.__size):
                for _ in range(self.__position[0]):
                    print(" ", end="")
                for width in range(self.__size):
                    print("#", end="")
                print()
