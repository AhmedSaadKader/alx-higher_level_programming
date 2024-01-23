#!/usr/bin/python3

"""contains a class that defines a node of a singly linked
list
and a class that defines a singly linked list"""


class Node:
	"""defines a node of a singly linked list"""
	def __init__(self, data, next_node=None):
		self.data = data
		self.next_node = next_node
	
	@property
	def data(self):
		return self.__data
	
	@data.setter
	def data(self, value):
		self.__data = value
	
	@property
	def next_node(self):
		return self.__next_node
	
	@next_node.setter
	def next_node(self, value):
		self.__next_node = value

class SinglyLinkedList:
	"""defines a singly linked list"""
	def __init__(self):
		pass
	