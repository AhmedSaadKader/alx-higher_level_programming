#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        printed_value = "{:d}".format(value)
    except ValueError as v:
        sys.stderr.write("Exception: {}\n".format(str(v)))
        sys.stderr.flush()
        return False
    else:
        print(printed_value)
        return True
