#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    if not isinstance(value, int):
        sys.stderr.write("Exception: {} is not an integer\n".format(value))
        sys.stderr.flush()
        return False
    try:
        printed_value = "{:d}".format(value)
        return True
    except ValueError as v:
        sys.stderr.write("Exception: {}\n".format(str(v)))
        sys.stderr.flush()
        return False
