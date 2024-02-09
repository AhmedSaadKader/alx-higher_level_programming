#!/usr/bin/python3
"""creates an object from a JSON file"""
import json


def load_from_json_file(filename):
    """creates an object from a JSON file

    Args:
        filename (file): file name
    """
    with open(filename, encoding="utf-8") as f:
        return json.loads(f.read())
