#!/usr/bin/python3
"""returns the JSON representation of an object"""
import json


def to_json_string(my_obj):
    """return the JSON representation of an object

    Args:
        my_obj (_type_): _description_
    Return:
        JSON representation of an object
    """
    return json.dumps(my_obj)
