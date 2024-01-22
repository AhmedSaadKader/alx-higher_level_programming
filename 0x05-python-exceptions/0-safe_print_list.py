#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    print_counter = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            print_counter += 1
        except IndexError:
            pass
    print()
    return print_counter
