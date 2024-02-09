#!/usr/bin/python3
"""Rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle using BaseGeometry"""

    def __init__(self, width, height):
        """Initialize a new rectange

        Args:
            width (int): width of rectangle
            height (int): _description_
        """
        try:
            self.integer_validator("width", width)
            self.__width = width
        except Exception as e:
            print("[{}] {}".format(e.__class__.__name__, e))
        try:
            self.integer_validator("height", height)
            self.__height = height
        except Exception as e:
            print("[{}] {}".format(e.__class__.__name__, e))

    def area(self):
        """Calculates the area of rectangle"""

        return self.__width * self.__height

    def __str__(self):
        return f"[{self.__class__.__name__}] {self.__width}/{self.__height}"
