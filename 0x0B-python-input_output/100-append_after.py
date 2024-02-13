#!/usr/bin/python3
"""inserts a line of text to a file, after each
    line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file, after each
    line containing a specific string

    Args:
        filename (str, optional): filename. Defaults to "".
        search_string (str, optional): search string. Defaults to "".
        new_string (str, optional): new string. Defaults to "".
    """
    with open(filename, "r+", encoding="utf-8") as f:
        new_content = ""
        for line in f:
            new_content += line
            if search_string in line:
                new_content += new_string
        f.seek(0)
        f.write(new_content)
        f.truncate()
