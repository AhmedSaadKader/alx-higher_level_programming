#!/usr/bin/python3
""" This module contains a class LockedClass. This class has
no class or object attribute. It prevents the user from
dynamically creating new instance attributes, except if the new
instance attribute is called first_name
"""


class LockedClass:
    """ This class has no class or object attribute. It prevents the
    user from dynamically creating new instance attributes,
    except if the new instance attribute is called first_name
    """
    def __init__(self):
        pass

    def __setattr__(self, name, value):
        if name == "first_name":
            object.__setattr__(self, name, value)
        else:
            raise AttributeError(
                f"'LockedClass' object has no attribute '{name}'")
