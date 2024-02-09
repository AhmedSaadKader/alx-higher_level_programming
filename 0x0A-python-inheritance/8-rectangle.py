#!/usr/bin/python3
"""Rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """_summary_

    Args:
        BaseGeometry (_type_): _description_
    """

    def __init__(self, width, height):
        try:
            self.integer_validator("width", width)
        except Exception as e:
            print("[{}] {}".format(e.__class__.__name__, e))
        try:
            self.integer_validator("height", height)
            self.__height = height
        except Exception as e:
            print("[{}] {}".format(e.__class__.__name__, e))
