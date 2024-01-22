#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    while True:
        try:
            for i in range(x):
                print("{:d}".format(my_list[i]), end="")
            print("")
            return i + 1
        except IndexError:
            pass
