#!/usr/bin/python3
"""writes a string to a text file"""


def write_file(filename="", text=""):
    """writes a string to a text file

    Args:
        filename (str, optional): _description_. Defaults to "".
        text (str, optional): _description_. Defaults to "".
    Return:
        The number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
