#!/usr/bin/python3
def remove_char_at(str, n):
    str_cpy = ""
    for i, char in enumerate(str):
        if i != n:
            str_cpy += char
    return (str_cpy)
