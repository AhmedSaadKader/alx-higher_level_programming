#!/usr/bin/python3
"""Reads a text file"""


def read_file(filename=""):
    """Reads a text file(UTF8) and prints it to stdout

    Args:
        filename (str, optional): the filename. Defaults to "".
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read())
