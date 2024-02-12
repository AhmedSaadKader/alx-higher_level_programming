#!/usr/bin/python3
def uppercase(str):
    str_result = ""
    for c in str:
        if ord(c) > 96 and ord(c) < 123:
            c = chr(ord(c) - 32)
        str_result += c
    print("{}".format(str_result))
