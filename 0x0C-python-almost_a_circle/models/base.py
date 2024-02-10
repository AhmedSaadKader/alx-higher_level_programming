#!/usr/bin/python3
"""Base for all other classes"""


class Base:
	"""Base for all other classes. The goal is to manage
	id attribute all your future classes and to avoid duplicating the
	same code (by extension, same bugs)"""

	__nb_objects = 0

	def __init__(self, id=None):
		self.id = id
		if (id == None):
			Base.__nb_objects += 1
			self.id = Base.__nb_objects
