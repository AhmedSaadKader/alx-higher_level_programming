#!/usr/bin/python3
"""Rectangle class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square using BaseGeometry"""

    def __init__(self, size):
        """Initialize a new square

        Args:
            width (int): width of rectangle
            height (int): _description_
        """
        try:
            self.integer_validator("size", size)
            super().__init__(size, size)
            self.__size = size
        except Exception as e:
            print("[{}] {}".format(e.__class__.__name__, e))
