#!/usr/bin/python3
"""
inherits_from module
"""

def inherits_from(obj, a_class):
    """Checks if an object is an instance of a
    class that inherited from the specified class

    Args:
        obj: The object to check
        a_class: the specified class
    Returns:
        True if object has inherited; false otherwise
    """
    return issubclass(type(obj), a_class)
