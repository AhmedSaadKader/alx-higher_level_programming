#!/usr/bin/python3
"""appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file

    Args:
        filename (str, optional): filename. Defaults to "".
        text (str, optional): the text to append. Defaults to "".
    Return:
        the number of characters added
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
