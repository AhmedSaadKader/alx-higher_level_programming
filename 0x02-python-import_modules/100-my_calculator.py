#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div


def my_calculator():
    OPERATOR = ['+', '-', '*', '/']
    arg_list = sys.argv
    arg_len = len(arg_list) - 1

    if arg_len != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = arg_list[1]
    operator = arg_list[2]
    b = arg_list[3]

    if operator not in OPERATOR:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    elif operator == "+":
        print("{} {} {} = {}".format(a, operator, b, add(int(a), int(b))))
    elif operator == "-":
        print("{} {} {} = {}".format(a, operator, b, sub(int(a), int(b))))
    elif operator == "*":
        print("{} {} {} = {}".format(a, operator, b, mul(int(a), int(b))))
    elif operator == "/":
        print("{} {} {} = {}".format(a, operator, b, div(int(a), int(b))))


if __name__ == "__main__":
    my_calculator()
