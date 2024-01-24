#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except Exception:
        sys.stderr.write("Exception: {}\n".format(str(v)))
        sys.stderr.flush()
        return False
