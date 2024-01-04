#!/usr/bin/python3
import sys


def my_calculator():
    OPERATOR = ['+', '-', '*', '/']
    arg_list = sys.argv
    arg_len = len(arg_list) - 1

    if arg_len != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    if arg_list[2] not in OPERATOR:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)


if __name__ == "__main__":
    my_calculator()
