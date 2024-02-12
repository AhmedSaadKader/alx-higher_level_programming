#!/usr/bin/python3
"""A Square class that inherits from the rectangle class and creates a new square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Creates a new square"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(id=id, width=size, height=size, x=x, y=y)

    @property
    def size(self):
        """size getter

        Returns:
            size: equals to self.width
        """
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """updates square attributes

        Returns:
            new_square: new_square
        """
        if args and len(args) != 0:
            attributes = ['id', 'size', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)
            return self
        if kwargs and len(kwargs) > 0:
            for key, value in kwargs.items():
                setattr(self, key, value)
            return self
        return self

    def to_dictionary(self):
        """returns the dictionary representation of a rectangle

        Returns:
            self.__dict__: dictionary of rectangle
        """
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
