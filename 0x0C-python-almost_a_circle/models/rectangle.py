#!/usr/bin/python3
"""Rectangle class - inherits from base - creates a new rectangle"""
from models.base import Base


class Rectangle(Base):
    """Creates a new rectangle
    
    Attributes:
    width: width of the rectangle
    height: height of the rectangle
    x: x
    y: y
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize a new rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width

        Returns:
            width: width
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height

        Returns:
            height: height
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """rectangle x

        Returns:
            self.__x: the rectangle x
        """
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """rectangle

        Returns:
            self.__y: the rectangle y
        """
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """calculates area of rectangle

        Returns:
            area: the area
        """
        return self.__width * self.__height

    def display(self):
        """prints the rectangle in stdout
        """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            for _ in range(self.x):
                print(" ", end="")
            print("#" * self.width)

    def __str__(self):
        if self.__class__.__name__ == "Square":
            width_height = f"{self.width}"
        else:
            width_height = f"{self.width}/{self.height}"
        return f"[{self.__class__.__name__}] ({self.id}) {self.x}/{self.y} - {width_height}"

    def update(self, *args, **kwargs):
        """updates rectangle attributes

        Returns:
            new_rectangle: new_rectangle
        """
        # for i in range(len(args)):
        # 	attr = list(self.__dict__)[i]
        # 	setattr(self, attr, args[i])
        if args and len(args) != 0:
            attributes = ['id', 'width', 'height', 'x', 'y']
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
        return {key.rsplit('__', maxsplit=1)[-1]: value
                for key, value in self.__dict__.items()}
