#!/usr/bin/python3
import sys


def print_args():
    args_list = sys.argv
    args_len = len(args_list) - 1

    print("{} argument".format(args_len), end="")

    if args_len == 0:
        print("s.".format(args_len))
    else:
        if args_len > 1:
            print("s", end="")
        print(":")
        for index, argument in enumerate(args_list):
            if index == 0:
                continue
            print("{}: {}".format(index, argument))


print_args()
