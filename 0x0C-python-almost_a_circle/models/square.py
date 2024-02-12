#!/usr/bin/python3
"""A Square class that inherits from the rectangle class and creates a new square"""
from models.rectangle import Rectangle


class Square(Rectangle):
	"""Creates a new square"""
	def __init__(self, size, x=0, y=0, id=None):
		super().__init__(id=id, width=size, height=size, x=x, y=y)