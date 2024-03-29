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
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if type(value) is not Node:
            if value is not None:
                raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """defines a singly linked list"""
    def __init__(self):
        self.__head = None

    def __str__(self) -> str:
        if self.__head is None:
            return ""
        list_string = ""
        current = self.__head
        while current.next_node is not None:
            list_string += str(current.data) + "\n"
            current = current.next_node
        list_string += str(current.data)
        return list_string

    def sorted_insert(self, value):
        if self.__head is None or value < self.__head.data:
            new_node = Node(value, self.__head)
            self.__head = new_node
            return

        current = self.__head
        while (current.next_node is not None):
            if (current.data
                == value) or (
                    current.data < value < current.next_node.data):
                new_node = Node(value, current.next_node)
                current.next_node = new_node

                return
            else:
                current = current.next_node
        new_node = Node(value)
        current.next_node = new_node
