#!/usr/bin/python3
import sys


def inifinite_add():
    args_list = sys.argv
    sum = 0

    for i in range(1, len(args_list)):
        sum += int(args_list[i])
    print("{}".format(sum))


if __name__ == "__main__":
    inifinite_add()
