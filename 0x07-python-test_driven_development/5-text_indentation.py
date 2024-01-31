#!/usr/bin/python3
"""
Module contains function `text_indentation` that prints
a text with 2 new lines after each of these characters:
., ?, :
"""


def text_indentation(text):
    """prints a text with 2 new lines after each of
    these characters: ., ?, :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        if text[i] in [".", "?", ":"]:
            print("{}\n".format(text[i]))
            i += 1
            if text[i] == " " or text[i] == "\t":
                i += 1
        else:
            print("{}".format(text[i]), end="")
            i += 1
