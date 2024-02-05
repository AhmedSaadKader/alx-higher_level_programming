#!/usr/bin/python3
"""Add_attribute function"""


def add_attribute(class_instance, attrib, value):
    """adds a new attribute to a class instance

    Args:
        class_instance (class): the class instance
        attribute (string): new attribute
        value (any): value of the new attribute
    """
    if not hasattr(class_instance, "__dict__"):
        raise TypeError("can't add new attribute")

    setattr(class_instance, attrib, value)
